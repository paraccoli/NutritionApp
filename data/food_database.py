# 簡易的な食品データベース
FOOD_DATABASE = {
    "Apple": {"calories": 52, "protein": 0.3, "carbs": 14, "fat": 0.2},
    "Banana": {"calories": 89, "protein": 1.1, "carbs": 23, "fat": 0.3},
    "Chicken Breast": {"calories": 165, "protein": 31, "carbs": 0, "fat": 3.6},
    # 他の食品を追加...
}

def get_food_list():
    return list(FOOD_DATABASE.keys())

def get_food_nutrition(food_name):
    return FOOD_DATABASE.get(food_name, {})