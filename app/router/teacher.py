from datetime import datetime
from typing import List


import models, schemas , database, oauth2
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

router = APIRouter(
    tags=["teacher"],
    prefix="/teacher"
)
@router.get("/all",
            response_model=List[schemas.TeacherOut],
            status_code=200)
def get_teacher(db: Session = Depends(database.get_db),
                current_user:models.User = Depends(oauth2.get_current_user)):
    
    if current_user.role != "STUDENT":
        raise HTTPException(status_code=404, detail="error")
    
    teachers = db.query(models.Teacher).join(models.User).all()
    return teachers

@router.get("/{id}",
            response_model=schemas.TeacherOut,
            status_code=200)
def get_teacher(id:int,
                db: Session = Depends(database.get_db),
                current_user:models.User = Depends(oauth2.get_current_user)):
    if current_user.role != "STUDENT":
        raise HTTPException(status_code=404, detail="error")
    teacher = db.query(models.Teacher).join(models.User).filter(models.User.id == id).first()

    return teacher
    