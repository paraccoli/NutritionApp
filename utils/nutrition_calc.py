def calculate_calories(protein, carbs, fat):
    return protein * 4 + carbs * 4 + fat * 9

def calculate_macro_percentages(protein, carbs, fat):
    total_calories = calculate_calories(protein, carbs, fat)
    return {
        "protein": (protein * 4 / total_calories) * 100,
        "carbs": (carbs * 4 / total_calories) * 100,
        "fat": (fat * 9 / total_calories) * 100
    }