import joblib

# Load the trained model
bmr_model = joblib.load("bmr_random_forest_model.pkl")

def calculate_calories_macros(gender, weight_kg, height_cm, age, activity_level, goal):
    # Convert gender to numeric for model input (Male=1, Female=0)
    gender_numeric = 1 if gender.lower() == 'male' else 0
    
    # Predict BMR using the model
    input_data = [[age, weight_kg, height_cm, gender_numeric]]
    bmr = bmr_model.predict(input_data)[0]

    # Activity multipliers
    activity_multipliers = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very active": 1.9
    }
    tdee = bmr * activity_multipliers.get(activity_level.lower(), 1.2)

    # Adjust calories based on the goal
    if goal.lower() == "weight loss":
        tdee -= 500
    elif goal.lower() == "weight gain":
        tdee += 500

    # Macronutrient breakdown
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
