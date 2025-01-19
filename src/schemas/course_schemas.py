from pydantic import BaseModel

class CourseBase(BaseModel):
    title: str
    description: str

class CourseCreate(CourseBase):
    user_id: int

class Course(CourseBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
