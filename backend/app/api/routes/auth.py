from fastapi import APIRouter, HTTPException, status, BackgroundTasks
from datetime import timedelta
from app.schemas.user import UserCreate, UserLogin, Token, UserResponse, EmailVerificationRequest
from app.services.user_service import UserService
from app.core.security import create_access_token
from app.core.config import settings
from bson import ObjectId

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user_data: UserCreate, background_tasks: BackgroundTasks):
    """Register a new user and send verification email."""
    try:
        user = await UserService.create_user(user_data, send_email=True)

        # Convert ObjectId to string and ensure is_verified is included
        user["_id"] = str(user["_id"])
        if "is_verified" not in user:
            user["is_verified"] = False

        return user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred during registration: {str(e)}"
        )

@router.post("/login", response_model=dict)
async def login(user_credentials: UserLogin):
    """Login user and return access token."""
    user = await UserService.authenticate_user(
        user_credentials.email, 
        user_credentials.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user.get("is_active", False):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )

    # Create access token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user["_id"]), "email": user["email"]},
        expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "_id": str(user["_id"]),
            "email": user["email"],
            "username": user["username"],
            "full_name": user["full_name"],
            "is_verified": user.get("is_verified", False)
        }
    }

@router.get("/verify-email")
async def verify_email(token: str):
    """Verify user's email using token from email link."""
    verified = await UserService.verify_user_email(token)

    if not verified:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired verification token"
        )

    return {
        "message": "Email verified successfully! You can now use all features."
    }

@router.post("/resend-verification")
async def resend_verification(request: EmailVerificationRequest):
    """Resend verification email to user."""
    try:
        await UserService.resend_verification_email(request.email)
        return {
            "message": "Verification email sent successfully"
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to send verification email: {str(e)}"
        )

@router.post("/logout")
async def logout():
    """Logout endpoint (client should remove token)."""
    return {"message": "Logged out successfully"}