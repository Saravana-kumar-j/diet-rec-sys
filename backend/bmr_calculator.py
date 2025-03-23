def calculate_calories_macros(gender, weight_kg, height_cm, age, activity_level, goal):
    if gender.lower() == "male":
        bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)

    activity_multipliers = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very active": 1.9
    }

    tdee = bmr * activity_multipliers.get(activity_level.lower(), 1.2)

    if goal.lower() == "weight loss":
        tdee -= 500
    elif goal.lower() == "weight gain":
        tdee += 500

    macros = {
        "Protein": (tdee * 0.30) / 4,
        "Carbs": (tdee * 0.40) / 4,
        "Fats": (tdee * 0.30) / 9
    }

    return {
        "BMR (kcal/day)": round(bmr),
        "TDEE (kcal/day)": round(tdee),
        "Protein (g/day)": round(macros["Protein"]),
        "Carbs (g/day)": round(macros["Carbs"]),
        "Fats (g/day)": round(macros["Fats"])
    }
