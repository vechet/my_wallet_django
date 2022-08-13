from datetime import datetime
import sys
from sqlalchemy.orm import Session
from my_wallet_django.api_modules.category.models import Category
from my_wallet_django.api_modules.category.schemas import CategoryCreate, CategoryUpdate
from my_wallet_django.api_modules.status.models import Status
from my_wallet_django.api_modules.configuration.models import Configuration
from my_wallet_django.api_modules.base_schemas import Response


def get_category(db: Session, skip: int, limit: int, parent_id: int, name: str):
    try:
        print('1--')
        # filter name
        if(name != ''):
            filterName = db.query(Category).where(
                Category.name == name).order_by(Category.id).offset(skip).limit(limit).all()
            return Response(status="Ok", code="200", message="Fetch data successfully!", result=filterName)
        print('2--')
        # filter parent id
        if(parent_id != 0):
            filterParentId = db.query(Category).where(
                Category.parent_id == parent_id).order_by(Category.id).offset(skip).limit(limit).all()
            return Response(status="Ok", code="200", message="Fetch data successfully!", result=filterParentId)

        print('3--')

        # norma filter
        status = db.query(Status).filter(Status.key_name == "Active").first()
        results = db.query(Category).where(
            Category.status_id == status.id).order_by(Category.id).offset(skip).limit(limit).all()
        return Response(status="Ok", code="200", message="Fetch data successfully!", result=results)
    except:
        print("Error: ", sys.exc_info()[0])


def get_category_by_id(db: Session, id: int):
    return db.query(Category).filter(Category.id == id).first()


def create_category(db: Session, category: CategoryCreate):
    try:
        status = db.query(Status).filter(Status.key_name == "Active").first()

        new_category = Category(
            name=category.name,
            memo=category.memo,
            icon=category.icon,
            parent_id=category.parent_id,
            is_system_value=False,
            created_date=datetime.now(),
            created_by=1,
            status_id=status.id,
            version=1,
        )
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return {"_id": new_category.id}
    except:
        print("Error: ", sys.exc_info()[0])


def delete_category(db: Session, id: int):
    try:
        status = db.query(Status).filter(Status.key_name == "Inactive").first()
        _category = get_category_by_id(db=db, id=id)
        _category.status_id = status.id
        db.commit()
    except:
        print("Error: ", sys.exc_info()[0])


def update_category(db: Session, category: CategoryUpdate):
    try:
        current_category = get_category_by_id(
            db=db, id=category.id)
        current_category.name = category.name
        current_category.memo = category.memo
        current_category.icon = category.icon
        current_category.parent_id = category.parent_id
        current_category.modified_date = datetime.now(),
        current_category.modified_by = 1,
        current_category.version = current_category.version + 1,

        db.commit()
        db.refresh(current_category)
        return {"_id": current_category.id}
    except:
        print("Error: ", sys.exc_info()[0])
