from typing import Optional
from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str
    memo: Optional[str]
    icon: Optional[str]


class CategoryUpdate(BaseModel):
    id: int
    name: str
    memo: Optional[str]
    icon: Optional[str]


class CategoryDelete(BaseModel):
    id: int
