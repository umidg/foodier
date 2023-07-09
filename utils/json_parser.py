import json


json1= '''
{
  "Monday": {
    "breakfast": "Oatmeal with fruit",
    "lunch": "Grilled portobello mushroom sandwiches",
    "dinner": "Spaghetti with marinara sauce and roasted vegetables"
  },
  "Tuesday": {
    "breakfast": "Scrambled tofu with vegetables",
    "lunch": "Black bean and corn salad with avocado dressing",
    "dinner": "Spicy peanut sauce with rice and vegetables"
  },
  "Wednesday": {
    "breakfast": "Blueberry smoothie",
    "lunch": "Garlic herb roasted potatoes with salad",
    "dinner": "Vegetable stir fry with tofu and brown rice"
  },
  "Thursday": {
    "breakfast": "Pancakes with maple syrup and fruit",
    "lunch": "Hummus wrap with hummus, a handful of spinach, tomato and cucumber in a large whole wheat tortilla",
    "dinner": "Roasted cauliflower and chickpea burritos"
  },
  "Friday": {
    "breakfast": "cereal with milk",
    "lunch": "Lentil soup",
    "dinner": "Quinoa and black bean stuffed sweet potatoes"
  },
  "Saturday": {
    "breakfast": "avocado toast",
    "lunch": "Spinach and fruit smoothies",
    "dinner": "roasted vegetables and hummus wrap"
  },
  "Sunday": {
    "breakfast": "Tofu scramble",
    "lunch": "avocado toast",
    "dinner": "Spaghetti with marinara sauce and roasted vegetables"
  }
}
'''


json2 = """{
  "day": "Monday",
  "breakfast": "Oatmeal with fruit",
  "lunch": "Grilled portobello mushroom sandwiches",
  "dinner": "Spaghetti with marinara sauce and roasted vegetables",
  "ingredients": {
    "oatmeal": "Oats",
    "fruit": "Banana, strawberries, blueberries",
    "portobello mushroom": "Mushrooms",
    "sandwich": "Buns, tomatoes, lettuce, onion, cucumber",
    "spaghetti": "Spaghetti, marinara sauce, broccoli, zucchini, bell peppers, onion",
  }
}
{
  "day": "Tuesday",
  "breakfast": "Scrambled tofu with vegetables",
  "lunch": "Black bean and corn salad with avocado dressing",
  "dinner": "Roasted vegetable and bean burritos",
  "ingredients": {
    "tofu": "Tofu, onion, bell peppers, mushrooms, broccoli, zucchini",
    "dressing": "Avocado, lime, cilantro, salt, pepper",
    "burritos": " Tortillas, beans, corn, bell peppers, onions, cilantro, avocado",
  }
}
{
  "day": "Wednesday",
  "breakfast": "Smoothie with banana, spinach, protein powder, and almond milk",
  "lunch": "Lentil soup with carrots, onions, and celery",
  "dinner": "Spicy vegetable stir fry with tofu and brown rice",
  "ingredients": {
    "smoothie": "Banana, spinach, protein powder, almond milk",
    "soup": "Lentils, carrots, onions, celery",
    "stir-fry": "Tofu, bell peppers, mushrooms, broccoli, zucchini, brown rice",
  }
}
{
  "day": "Thursday",
  "breakfast": "Oatmeal with fruit",
  "lunch": "Grilled portobello mushroom sandwiches",
  "dinner": "Spaghetti with marinara sauce and roasted vegetables",
  "ingredients": {
    "oatmeal": "Oats",
    "fruit": "Banana, strawberries, blueberries",
    "portobello mushroom": "Mushrooms",
    "sandwich": "Buns, tomatoes, lettuce, onion, cucumber",
    "spaghetti": "Spaghetti, marinara sauce, broccoli, zucchini, bell peppers, onion",
  }
}
{
  "day": "Friday",
  "breakfast": "Scrambled tofu with vegetables",
  "lunch": "Black bean and corn salad with avocado dressing",
  "dinner": "Roasted vegetable and bean burritos",
  "ingredients": {
    "tofu": "Tofu, onion, bell peppers, mushrooms, broccoli, zucchini",
    "dressing": "Avocado, lime, cilantro, salt, pepper",
    "burritos": "Tortillas, beans, corn, bell peppers, onions, cilantro, avocado",
  }
}
{
  "day": "Saturday",
  "breakfast": "Smoothie with banana, spinach, protein powder, and almond milk",
  "lunch": "Lentil soup with carrots, onions, and celery",
  "dinner": "Spicy vegetable stir fry with tofu and brown rice",
  "ingredients": {
    "smoothie": "Banana, spinach, protein powder, almond milk",
    "soup": "Lentils, carrots, onions, celery",
    "stir-fry": "Tofu, bell peppers, mushrooms, broccoli, zucchini, brown rice",
  }
}
{
  "day": "Sunday",
  "breakfast": "Oatmeal with fruit",
  "lunch": "Grilled portobello mushroom sandwiches",
  "dinner": "Spaghetti with marinara sauce and roasted vegetables",
  "ingredients": {
    "oatmeal": "Oats",
    "fruit": "Banana, strawberries, blueberries",
    "portobello mushroom": "Mushrooms",
    "sandwich": "Buns, tomatoes, lettuce, onion, cucumber",
    "spaghetti": "Spaghetti, marinara sauce, broccoli, zucchini, bell peppers, onion",
  }
}"""




source_json_str = json1

# Load source JSON string into a Python dictionary
source_json = json.loads(source_json_str)

# Initialize your own JSON structure
your_json = {"Days": []}

# Extract data from the source JSON and fill your own JSON structure
for day, meals in source_json.items():
    day_data = {
        "Day": day,
        "Breakfast": meals["breakfast"],
        "Lunch": meals["lunch"],
        "Dinner": meals["dinner"]
    }
    your_json["Days"].append(day_data)

# Convert your JSON to a string
your_json_str = json.dumps(your_json, indent=2)

# Print your JSON
print(your_json_str)