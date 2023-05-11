from pydantic import BaseModel
from typing import Optional

# A model for users
class User(BaseModel):
    id: str
    name: Optional[str] = None
    email: str
    password: str
    created_at: Optional[int]

# A model for tasks
class Task(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    isComplete: bool = False
    category: Optional[str] = None
    tags: Optional[list[str]] = []
    userId: str
    created_at: Optional[int]
    end_at: Optional[int]


# Create a token model with access token and token type
class Token(BaseModel):
    access_token: str
    token_type: str