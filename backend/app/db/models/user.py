from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True): 
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str = Field(index=True, nullable=False, unique=True)
    is_active: bool = Field(default=True)
