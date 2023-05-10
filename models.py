from pydantic import BaseModel
from typing import Optional

# A model for users
class User(BaseModel):
    id: str
    name: Optional[str] = None
    email: str
    password: str

# A model for tasks
class Task(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    # owner: list[User] # A task can have multiple owners need to edit code letter to make it work
    owner : User
    date: int
    status: bool = False
    priority: Optional[int] = 1
    category: Optional[str] = None
    tags: Optional[list[str]] = []


# Create a token model with access token and token type
class Token(BaseModel):
    access_token: str
    token_type: str