from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.models import Course
from src.schemas.course_schemas import CourseCreate, Course as CourseSchema

router = APIRouter(prefix="/courses", tags=["courses"])



@router.post("/", response_model=CourseSchema)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(
        title=course.title,
        description=course.description,
        user_id=course.user_id
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course



@router.get("/", response_model=List[CourseSchema])
def get_courses(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return db.query(Course).offset(skip).limit(limit).all()



@router.get("/{course_id}", response_model=CourseSchema)
def get_course(course_id: int, db: Session = Depends(get_db)):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course



@router.put("/{course_id}", response_model=CourseSchema)
def update_course(course_id: int, course: CourseCreate, db: Session = Depends(get_db)):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    for key, value in course.dict().items():
        setattr(db_course, key, value)

    db.commit()
    db.refresh(db_course)
    return db_course



@router.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    db.delete(db_course)
    db.commit()
    return {"message": f"Course with id {course_id} has been deleted."}
