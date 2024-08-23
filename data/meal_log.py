from .food_database import get_food_nutrition

daily_meals = []

def add_meal(food_name, amount):
    nutrition = get_food_nutrition(food_name)
    meal = {
        "food": food_name,
        "amount": amount,
        "calories": nutrition["calories"] * amount / 100,
        "protein": nutrition["protein"] * amount / 100,
        "carbs": nutrition["carbs"] * amount / 100,
        "fat": nutrition["fat"] * amount / 100
    }
    daily_meals.append(meal)

def get_daily_nutrition():
    total = {"calories": 0, "protein": 0, "carbs": 0, "fat": 0}
    for meal in daily_meals:
        for key in total:
            total[key] += meal[key]
    return total