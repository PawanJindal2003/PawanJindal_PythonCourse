from pydantic import BaseModel


# Request schemes
class UserRegister(BaseModel):
    name: str
    email: str
    password: str


# Response schemes
class ShowUser(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True


# JWT Token
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
