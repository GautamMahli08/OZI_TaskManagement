from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Optional
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.services.task_service import TaskService
from app.api.deps import get_current_user

router = APIRouter()

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(
    task_data: TaskCreate,
    current_user: dict = Depends(get_current_user)
):
    """Create a new task."""
    try:
        user_id = str(current_user["_id"])
        task = await TaskService.create_task(user_id, task_data)

        # Convert ObjectIds to strings
        task["_id"] = str(task["_id"])
        task["user_id"] = str(task["user_id"])

        return task
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )

@router.get("/", response_model=List[TaskResponse])
async def get_tasks(
    status: Optional[str] = Query(None, description="Filter by status: pending, in-progress, completed"),
    current_user: dict = Depends(get_current_user)
):
    """Get all tasks for the current user, optionally filtered by status."""
    try:
        user_id = str(current_user["_id"])

        # Validate status if provided
        if status and status not in ["pending", "in-progress", "completed"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid status. Must be one of: pending, in-progress, completed"
            )

        tasks = await TaskService.get_tasks(user_id, status)

        # Convert ObjectIds to strings
        for task in tasks:
            task["_id"] = str(task["_id"])
            task["user_id"] = str(task["user_id"])

        return tasks
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )

@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: str,
    current_user: dict = Depends(get_current_user)
):
    """Get a specific task by ID."""
    try:
        user_id = str(current_user["_id"])
        task = await TaskService.get_task_by_id(task_id, user_id)

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        # Convert ObjectIds to strings
        task["_id"] = str(task["_id"])
        task["user_id"] = str(task["user_id"])

        return task
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )

@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: str,
    task_data: TaskUpdate,
    current_user: dict = Depends(get_current_user)
):
    """Update a task."""
    try:
        user_id = str(current_user["_id"])
        updated_task = await TaskService.update_task(task_id, user_id, task_data)

        if not updated_task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        # Convert ObjectIds to strings
        updated_task["_id"] = str(updated_task["_id"])
        updated_task["user_id"] = str(updated_task["user_id"])

        return updated_task
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )

@router.delete("/{task_id}", status_code=status.HTTP_200_OK)
async def delete_task(
    task_id: str,
    current_user: dict = Depends(get_current_user)
):
    """Delete a task."""
    try:
        user_id = str(current_user["_id"])
        deleted = await TaskService.delete_task(task_id, user_id)

        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        return {"message": "Task deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )