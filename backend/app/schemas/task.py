from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime
from app.models.task import TaskStatus

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=2000)
    status: TaskStatus = TaskStatus.PENDING
    due_date: Optional[datetime] = None

    @field_validator('due_date')
    @classmethod
    def due_date_not_past(cls, v):
        if v and v < datetime.utcnow():
            raise ValueError('Due date cannot be in the past')
        return v

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=2000)
    status: Optional[TaskStatus] = None
    due_date: Optional[datetime] = None

    @field_validator('due_date')
    @classmethod
    def due_date_not_past(cls, v):
        if v and v < datetime.utcnow():
            raise ValueError('Due date cannot be in the past')
        return v

class TaskResponse(BaseModel):
    id: str = Field(..., alias="_id")
    user_id: str
    title: str
    description: Optional[str] = None
    status: str
    due_date: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    model_config = {
        "populate_by_name": True
    }