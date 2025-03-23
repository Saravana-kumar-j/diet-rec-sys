document.getElementById("user-form").addEventListener("submit", async function(e) {
    e.preventDefault();
  
    // Collecting Form Data
    const user_data = {
      gender: document.getElementById("gender").value,
      weight_kg: parseFloat(document.getElementById("weight_kg").value),
      height_cm: parseFloat(document.getElementById("height_cm").value),
      age: parseInt(document.getElementById("age").value),
      activity_level: document.getElementById("activity_level").value,
      goal: document.getElementById("goal").value
    };
  
    const text_input = document.getElementById("chatbox").value;
  
    try {
      // Sending Data to Backend
      const response = await fetch("http://localhost:5000/recommend", {
        method: "POST",
        body: JSON.stringify({ user_data, text_input }),
        headers: { "Content-Type": "application/json" }
      });
  
      const result = await response.json();
  
      // Displaying Results
      document.getElementById("nutrition-data").innerHTML = `
        <h3>Nutrition Data</h3>
        <p>BMR: ${result.nutrition_data["BMR (kcal/day)"]} kcal/day</p>
        <p>TDEE: ${result.nutrition_data["TDEE (kcal/day)"]} kcal/day</p>
        <p>Protein: ${result.nutrition_data["Protein (g/day)"]} g</p>
        <p>Carbs: ${result.nutrition_data["Carbs (g/day)"]} g</p>
        <p>Fats: ${result.nutrition_data["Fats (g/day)"]} g</p>
      `;
  
      document.getElementById("preferences").innerHTML = `
        <h3>Preferences</h3>
        <p>Diet: ${result.preferences.Diet || "Not specified"}</p>
        <p>Allergies: ${result.preferences.Allergies.length > 0 ? result.preferences.Allergies.join(", ") : "None"}</p>
        <p>Meal Frequency: ${result.preferences["Meal Frequency"] || "Not specified"}</p>
      `;
  
      document.getElementById("meal-plan").innerHTML = `
        <h3>Generated Meal Plan</h3>
        <p>${result.meal_plan}</p>
      `;
    } catch (error) {
      console.error("Error:", error);
      alert("An error occurred. Please try again.");
    }
  });

document.getElementById("meal-plan").innerHTML = `
  <h3>Generated Meal Plan</h3>
  <div class="meal-plan-content">${DOMPurify.sanitize(marked.parse(result.meal_plan))}</div>
`;
  