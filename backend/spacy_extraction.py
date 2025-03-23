import spacy
from spacy.pipeline import EntityRuler

nlp = spacy.load("en_core_web_sm")
ruler = nlp.add_pipe("entity_ruler", before="ner")

patterns = [
    # Diet Pattern
    {
        "label": "DIET",
        "pattern": [{"LOWER": {"REGEX": "ovo[- ]?vegetarian"}}]
    },
    
    # Allergies Patterns
    {
        "label": "ALLERGY",
        "pattern": [{"LOWER": {"REGEX": "peanut(s)?"}}]
    },
    {
        "label": "ALLERGY",
        "pattern": [{"LOWER": {"REGEX": "shellfish"}}]
    },
    
    # Enhanced Meal Frequency Patterns
    {
        "label": "MEAL_FREQ",
        "pattern": [
            {"LIKE_NUM": True},
            {"LOWER": {"REGEX": "meal(s)?"}},
            {"LOWER": {"IN": ["and", "+"]}, "OP": "?"},
            {"LIKE_NUM": True},
            {"LOWER": {"REGEX": "snack(s)?"}, "OP": "?"}
        ]
    },
    {
        "label": "MEAL_FREQ",
        "pattern": [
            {"LIKE_NUM": True},
            {"LOWER": {"REGEX": "snack(s)?"}}
        ]
    }
]

ruler.add_patterns(patterns)

def extract_preferences(text):
    """Process user input text and extract dietary preferences"""
    doc = nlp(text)
    results = {
        "Diet": None,
        "Allergies": [],
        "Meal Frequency": None
    }
    
    for ent in doc.ents:
        if ent.label_ == "DIET":
            results["Diet"] = ent.text
        elif ent.label_ == "ALLERGY":
            results["Allergies"].append(ent.text)
        elif ent.label_ == "MEAL_FREQ":
            results["Meal Frequency"] = ent.text
    
    return results

# Example usage with user input
if __name__ == "__main__":
    user_input = input("Enter your dietary preferences: ")
    preferences = extract_preferences(user_input)
    print("\nExtracted Preferences:")
    print(f"Diet: {preferences['Diet']}")
    print(f"Allergies: {preferences['Allergies']}")
    print(f"Meal Frequency: {preferences['Meal Frequency']}")