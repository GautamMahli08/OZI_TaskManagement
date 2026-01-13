from typing import Optional
from bson import ObjectId
from app.core.database import get_users_collection
from app.core.security import get_password_hash, verify_password, create_verification_token, verify_verification_token
from app.core.email import send_verification_email
from app.schemas.user import UserCreate, UserUpdate
from app.models.user import UserInDB
from datetime import datetime

class UserService:
    @staticmethod
    async def create_user(user_data: UserCreate, send_email: bool = True) -> dict:
        """Create a new user and send verification email."""
        users_collection = await get_users_collection()

        # Check if email already exists
        existing_user = await users_collection.find_one({"email": user_data.email})
        if existing_user:
            raise ValueError("Email already registered")

        # Check if username already exists
        existing_username = await users_collection.find_one({"username": user_data.username})
        if existing_username:
            raise ValueError("Username already taken")

        # Create user document
        user_dict = {
            "email": user_data.email,
            "username": user_data.username,
            "hashed_password": get_password_hash(user_data.password),
            "full_name": user_data.full_name,
            "is_active": True,
            "is_verified": False,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }

        result = await users_collection.insert_one(user_dict)
        user_dict["_id"] = result.inserted_id

        # Send verification email
        if send_email:
            try:
                verification_token = create_verification_token(user_data.email)
                await send_verification_email(
                    [user_data.email],
                    user_data.username,
                    verification_token
                )
            except Exception as e:
                # Log error but don't fail registration
                print(f"Failed to send verification email: {str(e)}")

        return user_dict

    @staticmethod
    async def verify_user_email(token: str) -> bool:
        """Verify user's email using token."""
        email = verify_verification_token(token)
        if not email:
            return False

        users_collection = await get_users_collection()
        result = await users_collection.update_one(
            {"email": email},
            {"$set": {"is_verified": True, "updated_at": datetime.utcnow()}}
        )

        return result.modified_count > 0

    @staticmethod
    async def resend_verification_email(email: str) -> bool:
        """Resend verification email to user."""
        users_collection = await get_users_collection()
        user = await users_collection.find_one({"email": email})

        if not user:
            raise ValueError("User not found")

        if user.get("is_verified", False):
            raise ValueError("Email already verified")

        # Send new verification email
        verification_token = create_verification_token(email)
        await send_verification_email(
            [email],
            user["username"],
            verification_token
        )

        return True

    @staticmethod
    async def authenticate_user(email: str, password: str) -> Optional[dict]:
        """Authenticate a user by email and password."""
        users_collection = await get_users_collection()
        user = await users_collection.find_one({"email": email})

        if not user:
            return None

        if not verify_password(password, user["hashed_password"]):
            return None

        return user

    @staticmethod
    async def get_user_by_id(user_id: str) -> Optional[dict]:
        """Get user by ID."""
        users_collection = await get_users_collection()
        user = await users_collection.find_one({"_id": ObjectId(user_id)})
        return user

    @staticmethod
    async def get_user_by_email(email: str) -> Optional[dict]:
        """Get user by email."""
        users_collection = await get_users_collection()
        user = await users_collection.find_one({"email": email})
        return user

    @staticmethod
    async def update_user(user_id: str, user_data: UserUpdate) -> Optional[dict]:
        """Update user information."""
        users_collection = await get_users_collection()

        update_data = {k: v for k, v in user_data.dict(exclude_unset=True).items()}

        if not update_data:
            return await UserService.get_user_by_id(user_id)

        # Check if username is being updated and if it's already taken
        if "username" in update_data:
            existing_username = await users_collection.find_one({
                "username": update_data["username"],
                "_id": {"$ne": ObjectId(user_id)}
            })
            if existing_username:
                raise ValueError("Username already taken")

        update_data["updated_at"] = datetime.utcnow()

        await users_collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": update_data}
        )

        return await UserService.get_user_by_id(user_id)

    @staticmethod
    async def delete_user(user_id: str) -> bool:
        """Delete a user."""
        users_collection = await get_users_collection()
        result = await users_collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0