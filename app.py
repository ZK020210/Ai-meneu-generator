from openai import OpenAI

# 🔐 PUT YOUR API KEY HERE
client = OpenAI(api_key="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"
)

print("🍽️ Welcome to Menu AI")
print("----------------------")

# Ask user questions
country = input("What country do you live in? ")
restaurant_type = input("What type of restaurant is this? (cafe, fast food, fine dining): ")
food_genre = input("What genre of food do you want? (Italian, Indian, Mexican, etc.): ")
diet = input("Any dietary preference? (none, vegetarian, halal, vegan): ")
budget = input("What is the budget level? (low, medium, high): ")
num_dishes = input("How many menu items do you want? ")

# Basic input check
if country == "" or food_genre == "" or restaurant_type == "":
    print("❌ Missing required information.")
    quit()

print("\n Generating menu...\n")

# -------------------------
# STEP 1: Get currency
# -------------------------
currency_prompt = f"""
What currency is used in {country}?
Reply ONLY in this format:
Currency Name - Symbol
Example:
US Dollar - $
"""

currency_response = client.responses.create(
    model="gpt-4.1-mini",
    input=currency_prompt
)

currency = currency_response.output_text.strip()

# -------------------------
# STEP 2: Generate menu
# -------------------------
menu_prompt = f"""
Create a menu with {num_dishes} items for a {restaurant_type} restaurant.

Details:
- Country: {country}
- Currency: {currency}
- Food genre: {food_genre}
- Dietary preference: {diet}
- Budget level: {budget}

For each item include:
- Dish name
- Short description
- Price using the correct currency

Keep it simple and realistic.
"""

menu_response = client.responses.create(
    model="gpt-4.1-mini",
    input=menu_prompt
)

menu = menu_response.output_text.strip()

# -------------------------
# OUTPUT
# -------------------------
print("🌍 Country:", country)
print("💰 Currency:", currency)
print("🍴 Restaurant Type:", restaurant_type)
print("🥘 Food Genre:", food_genre)
print("🥗 Diet:", diet)
print("💵 Budget:", budget)

print("\n📋 Generated Menu:\n")
print(menu)

