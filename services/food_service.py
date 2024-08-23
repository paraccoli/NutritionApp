from database.models import Food
from database.db_connection import get_db
from sqlalchemy import or_

def get_food_list(search_term=None):
    db = next(get_db())
    query = db.query(Food)
    if search_term:
        query = query.filter(or_(Food.name.ilike(f'%{search_term}%'),
                                 Food.category.ilike(f'%{search_term}%') if hasattr(Food, 'category') else False))
    foods = query.all()
    return [food.name for food in foods]

def add_food(name: str, calories: float, protein: float, carbs: float, fat: float, category: str):
    db = next(get_db())
    new_food = Food(name=name, calories=calories, protein=protein, carbs=carbs, fat=fat, category=category)
    db.add(new_food)
    db.commit()
    db.refresh(new_food)
    return new_food

def get_food_by_name(name: str):
    db = next(get_db())
    return db.query(Food).filter(Food.name == name).first()

def search_food(search_term: str):
    db = next(get_db())
    return db.query(Food).filter(or_(Food.name.ilike(f'%{search_term}%'),
                                     Food.category.ilike(f'%{search_term}%'))).all()