from pydantic import BaseModel

class CategoryBase(BaseModel):
    label: str
    description: str | None = None


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True
