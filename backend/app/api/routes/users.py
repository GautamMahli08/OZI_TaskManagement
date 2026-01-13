from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import UserResponse, UserUpdate
from app.services.user_service import UserService
from app.services.task_service import TaskService
from app.api.deps import get_current_user

router = APIRouter()

@router.get("/me", response_model=UserResponse)
async def get_current_user_profile(current_user: dict = Depends(get_current_user)):
    """Get current user profile."""
    current_user["_id"] = str(current_user["_id"])
    # Ensure is_verified is included
    if "is_verified" not in current_user:
        current_user["is_verified"] = False
    return current_user

@router.put("/me", response_model=UserResponse)
async def update_user_profile(
    user_data: UserUpdate,
    current_user: dict = Depends(get_current_user)
):
    """Update current user profile."""
    try:
        user_id = str(current_user["_id"])
        updated_user = await UserService.update_user(user_id, user_data)

        if not updated_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        updated_user["_id"] = str(updated_user["_id"])
        # Ensure is_verified is included
        if "is_verified" not in updated_user:
            updated_user["is_verified"] = False
        return updated_user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )

@router.delete("/me", status_code=status.HTTP_200_OK)
async def delete_user_profile(current_user: dict = Depends(get_current_user)):
    """Delete current user profile and all associated tasks."""
    try:
        user_id = str(current_user["_id"])

        # Delete all user's tasks first
        await TaskService.delete_all_user_tasks(user_id)

        # Delete user
        deleted = await UserService.delete_user(user_id)

        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return {"message": "User and all associated tasks deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )