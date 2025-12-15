from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import database
from ..database import get_db
from ..repository import auth
from Week3.scheme.schemes import UserRegister, ShowUser

router = APIRouter(prefix="/auth", tags=["Users"])


@router.post('/register', response_model=ShowUser)
def register(request: UserRegister, db: Session = Depends(get_db)):
    return auth.register(request, db)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    return auth.login(request, db)
