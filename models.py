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
    created_at: Optional[float]
    end_at: Optional[float] = None

class TaskDocument(BaseModel):
    id: str
    title: str
    description: Optional[str]
    isComplete: bool
    category: Optional[str]
    tags: Optional[List[str]]
    userId: str
    created_at: Optional[float]
    end_at: Optional[float]
