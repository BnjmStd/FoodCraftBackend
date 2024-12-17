from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime
from enum import Enum

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str # nombre
    country: str # pais de residencia
    email: str = Field(index=True, unique=True) # email unico 
    password: str # pwd 
    user_type: TypeUser = Field(sa_column_kwargs={"type": "VARCHAR"})   # Admin, normal, etc.

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relaciones
    foods: List["Food"] = Relationship(back_populates="user")

class TypeUser(str, Enum):
    ADMIN = 'ADMIN'
    NORMAL = 'NORMAL'
    VISUALIZADOR = 'VISUALIZADOR'
    
class SocialData(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", unique=True)
    education_level: Optional[str] = None
    occupation: Optional[str] = None
    income: Optional[float] = None
    marital_status: Optional[str] = None
    children: Optional[int] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relación inversa
    user: "User" = Relationship(back_populates="social_data")

class LifeStyleData(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", unique=True)
    alcohol_use: Optional[bool] = None
    smoking: Optional[bool] = None
    sleep_hours: Optional[float] = None
    activity_level: Optional[str] = None  # Sedentary, Moderate, Active
    height: Optional[float] = None
    weight: Optional[float] = None
    bmi: Optional[float] = None
    waist_circum: Optional[float] = None
    hip_circum: Optional[float] = None
    body_fat: Optional[float] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relación inversa
    user: "User" = Relationship(back_populates="lifestyle_data")

class Food(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    user_id: int = Field(foreign_key="user.id")

    # Relación inversa
    user: "User" = Relationship(back_populates="foods")
