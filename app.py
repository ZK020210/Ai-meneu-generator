# =====================================
# AI MENU GENERATOR (TKS PROJECT)
# By: Grade 10 Student
# =====================================

from openai import OpenAI
import json

# Create OpenAI client
client = OpenAI(
api_key = "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"
)

# -----------------------------
# Function: Build AI Prompt
# -----------------------------
def build_prompt(
    restaurant_type,
    audience,
    diet,
    budget,
    cuisine,
    menu_categories
):
    prompt = f"""
You are an AI culinary assistant.

Create a restaurant menu using these rules:

Restaurant type: {restaurant_type}
Target audience: {audience}
Dietary focus: {diet}
Budget level: {budget}
Cuisine style: {cuisine}

Menu categories to include:
{menu_categories}

RULES:
- Make at least one dish per category
- Follow dietary restrictions strictly
- Keep dishes realistic
- Do not repeat dishes

Return ONLY valid JSON in this format:
{{
  "menu": [
    {{
      "dish_name": "",
      "category": "",
      "key_ingredients": [],
      "estimated_cost": "",
      "dietary_tags": []
    }}
  ]
}}
"""
    return prompt

# -----------------------------
# Function: Call AI
# -----------------------------
def call_ai(prompt):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        timeout=30
    )
    return response.output_text

# -----------------------------
# Main Program
# -----------------------------
print("🍽️ AI MENU GENERATOR\n")

restaurant_type = input("Enter cusine type, for example fast food etc.: ")
audience = input("Enter target audience: ")
diet = input("Enter dietary focus: ")
budget = input("Enter budget level: ")
cuisine = input("Enter cuisine style: ")

menu_input = input(
    "Enter menu categories (comma-separated, e.g. starters, mains, desserts): "
)

menu_categories = [item.strip() for item in menu_input.split(",")]

# Build prompt
prompt = build_prompt(
    restaurant_type,
    audience,
    diet,
    budget,
    cuisine,
    menu_categories
)

print("\n⏳ Generating menu...\n")

# Call AI
ai_output = call_ai(prompt)

# Clean and load JSON
clean_output = ai_output.replace("```json", "").replace("```", "").strip()
menu_data = json.loads(clean_output)

# Display menu
print("✅ GENERATED MENU:\n")

for dish in menu_data["menu"]:
    print(f"🍴 {dish['dish_name']} ({dish['category']})")
    print(f"   Ingredients: {', '.join(dish['key_ingredients'])}")
    print(f"   Cost Level: {dish['estimated_cost']}")
    print(f"   Dietary Tags: {', '.join(dish['dietary_tags'])}\n")
