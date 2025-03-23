from flask import Flask, request, jsonify
from flask_cors import CORS
from spacy_extraction import extract_preferences
from bmr_calculator import calculate_calories_macros
from gemini_integration import generate_meal_plan  # Add this import

app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.json
        user_data = data.get("user_data", {})
        text_input = data.get("text_input", "")

        # Extract values from user_data
        gender = user_data.get("gender")
        weight_kg = user_data.get("weight_kg")
        height_cm = user_data.get("height_cm")
        age = user_data.get("age")
        activity_level = user_data.get("activity_level")
        goal = user_data.get("goal")

        # Step 1: SpaCy Extraction
        preferences = extract_preferences(text_input)

        # Step 2: BMR Calculation
        nutrition_data = calculate_calories_macros(gender, weight_kg, height_cm, age, activity_level, goal)

        # Step 3: Generate Meal Plan
        meal_plan = generate_meal_plan(user_data, preferences, nutrition_data)

        # Combine results
        response_data = {
            "preferences": preferences,
            "nutrition_data": nutrition_data,
            "meal_plan": meal_plan
        }

        return jsonify(response_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)