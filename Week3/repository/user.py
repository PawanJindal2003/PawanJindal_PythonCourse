from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from Week3.models import model


def show_user(id: int, db: Session):
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id = {id} not found")
    return user


def show_all_users(db: Session, skip: int = 0, limit: int = 5):
    return db.query(model.User).offset(skip).limit(limit).all()


def get_user_by_email(email: str, db: Session):
    user = db.query(model.User).filter(model.User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with email = {email} not found")
    return user
