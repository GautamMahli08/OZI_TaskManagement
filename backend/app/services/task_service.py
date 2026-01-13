from typing import List, Optional
from bson import ObjectId
from app.core.database import get_tasks_collection
from app.schemas.task import TaskCreate, TaskUpdate
from app.models.task import TaskStatus
from datetime import datetime

class TaskService:
    @staticmethod
    async def create_task(user_id: str, task_data: TaskCreate) -> dict:
        """Create a new task."""
        tasks_collection = await get_tasks_collection()

        task_dict = {
            "user_id": ObjectId(user_id),
            "title": task_data.title,
            "description": task_data.description,
            "status": task_data.status.value,
            "due_date": task_data.due_date,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }

        result = await tasks_collection.insert_one(task_dict)
        task_dict["_id"] = result.inserted_id

        return task_dict

    @staticmethod
    async def get_tasks(user_id: str, status: Optional[str] = None) -> List[dict]:
        """Get all tasks for a user, optionally filtered by status."""
        tasks_collection = await get_tasks_collection()

        query = {"user_id": ObjectId(user_id)}

        if status:
            query["status"] = status

        tasks = await tasks_collection.find(query).sort("created_at", -1).to_list(length=None)
        return tasks

    @staticmethod
    async def get_task_by_id(task_id: str, user_id: str) -> Optional[dict]:
        """Get a specific task by ID for a user."""
        tasks_collection = await get_tasks_collection()
        task = await tasks_collection.find_one({
            "_id": ObjectId(task_id),
            "user_id": ObjectId(user_id)
        })
        return task

    @staticmethod
    async def update_task(task_id: str, user_id: str, task_data: TaskUpdate) -> Optional[dict]:
        """Update a task."""
        tasks_collection = await get_tasks_collection()

        # Check if task exists and belongs to user
        existing_task = await TaskService.get_task_by_id(task_id, user_id)
        if not existing_task:
            return None

        update_data = {k: v for k, v in task_data.dict(exclude_unset=True).items()}

        if not update_data:
            return existing_task

        # Convert status enum to string if present
        if "status" in update_data and isinstance(update_data["status"], TaskStatus):
            update_data["status"] = update_data["status"].value

        update_data["updated_at"] = datetime.utcnow()

        await tasks_collection.update_one(
            {"_id": ObjectId(task_id), "user_id": ObjectId(user_id)},
            {"$set": update_data}
        )

        return await TaskService.get_task_by_id(task_id, user_id)

    @staticmethod
    async def delete_task(task_id: str, user_id: str) -> bool:
        """Delete a task."""
        tasks_collection = await get_tasks_collection()
        result = await tasks_collection.delete_one({
            "_id": ObjectId(task_id),
            "user_id": ObjectId(user_id)
        })
        return result.deleted_count > 0

    @staticmethod
    async def delete_all_user_tasks(user_id: str) -> int:
        """Delete all tasks for a user (called when user is deleted)."""
        tasks_collection = await get_tasks_collection()
        result = await tasks_collection.delete_many({"user_id": ObjectId(user_id)})
        return result.deleted_count