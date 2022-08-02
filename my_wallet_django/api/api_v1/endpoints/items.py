from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get("/item")
def get_items():
    return "hello"
