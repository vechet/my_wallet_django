from fastapi import APIRouter, Depends, HTTPException
from my_wallet_django.api_modules.authentication.auth import AuthHandler
from my_wallet_django.api_modules.authentication.schemas import AuthDetails
from my_wallet_django.config import SessionLocal
from sqlalchemy.orm import Session
from my_wallet_django.api_modules.auth_user_models import AuthUser
from datetime import datetime
from my_wallet_django.api_modules.base_schemas import Response

router = APIRouter()
auth_handler = AuthHandler()
users = []


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/register', status_code=201)
def register(auth_details: AuthDetails, db: Session = Depends(get_db)):
    # check duplicate user
    user = db.query(AuthUser).filter(
        AuthUser.username == auth_details.username).first()
    if(user is not None):
        return Response(status="Ok",
                        code="200",
                        message="User with this name already exists.").dict(exclude_none=True)

    hashed_password = auth_handler.get_password_hash(auth_details.password)

    # create new user
    new_auth_user = AuthUser(
        password=hashed_password,
        is_superuser=True,
        username=auth_details.username,
        first_name='',
        last_name='',
        email=auth_details.username,
        is_staff=True,
        is_active=True,
        date_joined=datetime.now(),
    )
    db.add(new_auth_user)
    db.commit()
    return Response(status="Ok",
                    code="200",
                    message="User created successfully!").dict(exclude_none=True)


@router.post('/createToken')
def create_token(auth_details: AuthDetails, db: Session = Depends(get_db)):
    user = db.query(AuthUser).filter(
        AuthUser.username == auth_details.username).first()

    if (user is None) or (not auth_handler.verify_password(auth_details.password, user.password)):
        return Response(status="Error: Unauthorized",
                        code="401",
                        message="Invalid username and/or password!").dict(exclude_none=True)

    # generate token
    token = auth_handler.encode_token(user.username)
    token['user_id'] = user.id

    return Response(status="Ok", code="200", message="Create token successfully", result=token)


@router.get('/login')
def login(username: str, password: str, username_token=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    user = db.query(AuthUser).filter(
        AuthUser.username == username).first()

    if (user is None) or (not auth_handler.verify_password(password, user.password)):
        return Response(status="Error: Unauthorized",
                        code="401",
                        message="Invalid username and/or password!").dict(exclude_none=True)

    return Response(status="Ok",
                    code="200",
                    message="Login").dict(exclude_none=True)


@router.get('/unprotected')
def unprotected():
    return {'hello': 'world'}


@router.get('/protected')
def protected(username=Depends(auth_handler.auth_wrapper)):
    return {'name': username}
