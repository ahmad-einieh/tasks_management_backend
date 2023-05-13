from pydantic import BaseModel,Field
from typing import Optional ,List
import uuid

# A model for users
class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4.__str__, alias='id')    
    name: Optional[str] = None
    email: str
    password: str
    created_at: Optional[float]

# A model for tasks
class Task(BaseModel):
    id: str = Field(default_factory=uuid.uuid4.__str__, alias='id')
    title: str
    description: Optional[str] = None
    isComplete: bool = False
    category: Optional[str] = None
    tags: Optional[List[str]] = []
    userId: str
    length: Optional[int] = None
    created_at: Optional[float]
    end_at: Optional[float]

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    isComplete: Optional[bool] = None
    category: Optional[str] = None
    tags: Optional[List[str]] = None
    add_length: Optional[int] = None
