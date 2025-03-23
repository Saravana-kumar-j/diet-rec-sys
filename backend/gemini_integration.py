# import google.generativeai as genai
# import os

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# def generate_meal_plan(user_data, preferences, nutrition_data):
#     prompt = f"""
#     User Information:
#     Age: {user_data['age']}
#     Gender: {user_data['gender']}
#     Height: {user_data['height_cm']} cm
#     Weight: {user_data['weight_kg']} kg
#     Activity Level: {user_data['activity_level']}
#     Goal: {user_data['goal']}
#     TDEE: {nutrition_data['TDEE (kcal/day)']}
#     Protein: {nutrition_data['Protein (g/day)']}
#     Carbs: {nutrition_data['Carbs (g/day)']}
#     Fats: {nutrition_data['Fats (g/day)']}
    
#     Dietary Preferences: {preferences.get('Diet', 'None')}
#     Allergies: {', '.join(preferences.get('Allergies', []))}
#     Meal Frequency: {preferences.get('Meal Frequency', '3 meals')}
    
#     Generate a personalized Tamil meal plan that meets their dietary needs.
#     """

#     response = genai.generate_text(prompt)
#     return response.text



import google.generativeai as genai
import markdown
import os

genai.configure(api_key="AIzaSyBCoiq4XolimIa4jfk7iXmQXhZjFbM2ooU")

def generate_meal_plan(user_data, preferences, nutrition_data):
    prompt = f"""User Information:
    Age: {user_data['age']}
    Gender: {user_data['gender']}
    Height: {user_data['height_cm']} cm
    Weight: {user_data['weight_kg']} kg
    Activity Level: {user_data['activity_level']}
    Goal: {user_data['goal']}
    TDEE: {nutrition_data['TDEE (kcal/day)']}
    Protein: {nutrition_data['Protein (g/day)']}
    Carbs: {nutrition_data['Carbs (g/day)']}
    Fats: {nutrition_data['Fats (g/day)']}
    
    Dietary Preferences: {preferences.get('Diet', 'None')}
    Allergies: {', '.join(preferences.get('Allergies', []))}
    Meal Frequency: {preferences.get('Meal Frequency', '3 meals')}
    
    Generate a personalized Tamil meal plan that meets their dietary needs. Just give me food item names."""  # Keep your existing prompt template

    try:
        # Initialize the model
        model = genai.GenerativeModel('gemini-1.5-pro-latest')
        
        # Generate content
        response = model.generate_content(prompt)
        html_content = markdown.markdown(response.text)
        return html_content
        
        # Return the generated text
        # return response.text
    except Exception as e:
        print(f"Error generating meal plan: {e}")
        return "Could not generate meal plan at this time."