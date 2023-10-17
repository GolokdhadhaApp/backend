import models, database, utils, oauth2
from fastapi import Depends,HTTPException, APIRouter
from sqlalchemy.orm import Session
import schemas

import logging

logger = logging.getLogger(__name__)

tags = ['authentication']
router = APIRouter() 

@router.post('/signup',
             status_code= 201,
             response_model= schemas.UserOut)
def signup(request: schemas.UserSignup, db: Session = Depends(database.get_db)):

    logger.info(f"Received signup request: {request}")

    request.password = utils.hash(request.password)
    
    new_user = models.User(**request.dict())
    new_user.role = "STUDENT"
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post('/signin',
             status_code= 200,
             response_model= schemas.Token)
def signin(request: schemas.UserSignin, db: Session = Depends(database.get_db)):
    logger.info(f"Received signin request: {request}")
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="error")
    if not utils.verify(request.password, user.password):
        raise HTTPException(status_code=400, detail="error")
    access_token = oauth2.create_access_token(data={"id": user.id,
                                                   "email": user.email,
                                                   "role": user.role,
                                                   "phone": user.phone,
                                                   "name": user.name})
    tokenData = schemas.Token(id=user.id, accessToken= access_token, token_type="Bearer", email=user.email, role=user.role, phone=user.phone, name=user.name)
    return tokenData

@router.post('/teacher/signup')
def teacher_signup(request: schemas.TeacherSingnUp, db: Session = Depends(database.get_db)):
    logger.info(f"Received teacher signup request: {request}")

    user = models.User(**request.user.dict())
    user.password = utils.hash(user.password)
    user.role = "TEACHER"
    db.add(user)
    db.commit()
    db.refresh(user)

    teacher = models.Teacher(user = user, bio = request.bio, subject = request.subject, currentInstitution = request.currentInstitution, offlineFee = request.offlineFee, onlineFee = request.onlineFee)
    teacher.balance = 0
    teacher.rating = 0.0
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    
    raise HTTPException(status_code=201, detail="Teacher created")


