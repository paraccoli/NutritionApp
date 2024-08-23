from database.models import Meal, Food
from database.db_connection import get_db
from datetime import datetime, timedelta
from sqlalchemy import func

def add_meal(user_id: int, food_name: str, amount: float, meal_time: str):
    db = next(get_db())
    food = db.query(Food).filter(Food.name == food_name).first()
    if not food:
        raise ValueError(f"Food '{food_name}' not found in the database")
    new_meal = Meal(user_id=user_id, food_id=food.id, amount=amount, meal_time=meal_time)
    db.add(new_meal)
    db.commit()
    db.refresh(new_meal)
    return new_meal

def get_user_meals(user_id: int, date=None):
    db = next(get_db())
    query = db.query(Meal).filter(Meal.user_id == user_id)
    if date:
        query = query.filter(func.date(Meal.date) == date)
    return query.order_by(Meal.date.desc()).all()

def get_daily_nutrition(user_id: int):
    db = next(get_db())
    today = datetime.now().date()
    meals = db.query(Meal).join(Food).filter(
        Meal.user_id == user_id,
        func.date(Meal.date) == today
    ).all()

    total_nutrition = {"calories": 0, "protein": 0, "carbs": 0, "fat": 0}
    for meal in meals:
        factor = meal.amount / 100  # Assuming food nutrition is per 100g
        total_nutrition["calories"] += meal.food.calories * factor
        total_nutrition["protein"] += meal.food.protein * factor
        total_nutrition["carbs"] += meal.food.carbs * factor
        total_nutrition["fat"] += meal.food.fat * factor

    return total_nutrition

def get_weekly_nutrition(user_id: int):
    db = next(get_db())
    week_ago = datetime.now().date() - timedelta(days=7)
    meals = db.query(Meal).join(Food).filter(
        Meal.user_id == user_id,
        func.date(Meal.date) > week_ago
    ).all()

    total_nutrition = {"calories": 0, "protein": 0, "carbs": 0, "fat": 0}
    for meal in meals:
        factor = meal.amount / 100  # Assuming food nutrition is per 100g
        total_nutrition["calories"] += meal.food.calories * factor
        total_nutrition["protein"] += meal.food.protein * factor
        total_nutrition["carbs"] += meal.food.carbs * factor
        total_nutrition["fat"] += meal.food.fat * factor

    # Calculate daily average
    for key in total_nutrition:
        total_nutrition[key] /= 7

    return total_nutrition