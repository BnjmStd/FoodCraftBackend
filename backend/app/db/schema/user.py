from typing import Optional
from pydantic import BaseModel

# Entrada: lo que el cliente envía
class UserCreate(BaseModel):
    name: str
    email: str

# Salida: lo que devuelves
class UserRead(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool
