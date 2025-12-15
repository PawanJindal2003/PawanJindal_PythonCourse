from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..models import model
from Week3.oauth.oauth2 import get_current_user
from ..repository import user
from Week3.scheme.schemes import ShowUser
from ..database import get_db

router = APIRouter(prefix="/user", tags=["Users"])


# Authorized path
@router.get('/me', response_model=ShowUser)
def my_info(db: Session = Depends(get_db), current_user: model.User = Depends(get_current_user)):
    return user.get_user_by_email(current_user.email, db)


# Unauthorized paths
@router.get('/all', response_model=List[ShowUser])
def show_user(db: Session = Depends(get_db)):
    return user.show_all_users(db)


@router.get('/{id}', response_model=ShowUser)
def show_user(id: int, db: Session = Depends(get_db)):
    return user.show_user(id, db)
