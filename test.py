# TODO:
# TODO: parse different jsons 
# TODO: send email with ingredients
# TODO: 
# TODO: adapt summarizer for Q&A
# TODO: 



import toml
import time
import cohere
from utils.send_email import send_email



# COHERE

cohere_key = toml.load('secrets.toml')['COHERE_API_KEY']
co = cohere.Client(cohere_key) 

def send_prompt(prompt):
    print(f"================\nThis is the plan\n"+prompt)
    tic=time.time()
    response = co.generate(
    model='command',
    prompt=prompt,
    max_tokens=3058,
    temperature=0.5,
    k=0,
    stop_sequences=[],
    return_likelihoods='NONE')
    _plan=('{}'.format(response.generations[0].text))

    print("Took "+str(time.time()-tic))
    return _plan


# ====================
# Create Prompt
# ====================
def create_prompt(name, weight, height, age, diet, allergies, budget, gender , daysofweek, meals, favfood):

    if(daysofweek=="whole week"):
        number_of_meals=7
    elif(daysofweek=="weekend"):
        number_of_meals=2
    else:
        number_of_meals=5

    total_calories=(int)(weight*10)+(height/4)*6+(age*5)
    calories=total_calories/number_of_meals
        

    if(diet != None):
        if_diet= f"""Make all meals {diet}""" 
        if(allergies!=None):
            if_diet = if_diet + ", and"
    else:
        if_diet= ""

    if (len(meals)!=3):
        if_meals= " ("+(", ".join(meals))+")"
    else:
        if_meals=""

    # HARDCODED: removed the option on UI
    number_of_meals = 7 
    meals = "weekly" 

    is_allergic=f""" Avoid these ingredients: {allergies}. """ if allergies != None else ""
    json_format="\nUse this JSON Structure:\n{\n  Monday: {\n    Breakfast: str,\n    Lunch: str,\n    Dinner: str\n  },\n# repeat for all "+str(number_of_meals)+" days\nIngredients: list\n}"
    cohere_prompt=f'Create a {meals} meal plan for {number_of_meals} meals per day{if_meals}, for a {age} years {gender}, with {height} cm and {weight} kg, with {calories} calories daily, on a {budget} dollars budget. {if_diet}{is_allergic}And create a list of all ingredients.\nStructure the text in JSON format, including the name of the day, the name of the dish, and all ingredients together unsorted at the end\nDo not include extra text or descriptions. Provide different dishes on different days'+json_format
    return cohere_prompt
    # response = send_prompt(cohere_prompt)
    # print(response)




# ====================
# Parse data
# ====================
def parse_and_assign(data):
    """
    This function parses the data and assigns the values to variables.
    :param data: The data to be parsed.
    :return: The variables with the values assigned.
    """
    
    # Assign the values to variables
    daysofweek = data.get("daysofweek")
    name = data.get("name")
    weight = float(data.get("weight", 0))  # Convert to float if needed
    height = float(data.get("height", 0))  # Convert to float if needed
    age = int(data.get("age", 0))  # Convert to int if needed
    diet = data.get("diet")
    allergies = data.get("allergies")
    budget = float(data.get("budget", 0))  # Convert to float if needed
    gender = data.get("gender")
    favfood = data.get("favfood")
    meals = data.get("meals", [])

    return name, weight, height, age, diet, allergies, budget, gender , daysofweek, meals, favfood


# ====================
# Clean Response
# ====================
def clean_response(_response):
    """
    This function cleans the response from the API.
    :param _response: The response to be cleaned.
    :return: str
    """
    _response 

# Serves static react pages
# serves api call to the chatgpt
def test(body): #body
    #parse dictionary of data fields
    name, weight, height, age, diet, allergies, budget, gender , daysofweek, meals, favfood= parse_and_assign(body)
    prompt = create_prompt(name, weight, height, age, diet, allergies, budget, gender , daysofweek, meals, favfood)
    _response_clean=prompt# TeST delte
    # _response = send_prompt(prompt)
    # print(_response)

    # _response_clean = clean_response(_response)
    send_email(name, _response_clean)

    return {"message": _response_clean}






_json_test={
    "daysofweek": "whole week",
    "name": "Umid",
    "weight": "80",
    "height": "173.3",
    "age": "30",
    "diet": "Vegan",
    "allergies": "Peanut",
    "favfood": "Shushi",
    "budget": "100",
    "meals": [
        "breakfast",
        "lunch",
        "dinner"
    ],
    "gender": "male"
    }

test(_json_test)









# import json

# # Define a mapping to extract data from the source JSON to your own JSON
# mapping = {
#     "day": "Day",
#     "breakfast": "Breakfast",
#     "lunch": "Lunch",
#     "dinner": "Dinner",
# }

# # Your source JSON
# source_json_str = '''
# {
#   "meal_plan": [
#     {
#       "day": "Monday",
#       "breakfast": "Oatmeal with fruit",
#       "lunch": "Grilled portobello mushroom sandwiches",
#       "dinner": "Spaghetti with marinara sauce and roasted vegetables"
#     },
#     {
#       "day": "Tuesday",
#       "breakfast": "Scrambled tofu with vegetables",
#       "lunch": "Black bean and corn salad with avocado dressing",
#       "dinner": "Spicy peanut sauce with rice and vegetables"
#     },
#     {
#       "day": "Wednesday",
#       "breakfast": "Blueberry smoothie",
#       "lunch": "Garlic herb roasted potatoes with salad",
#       "dinner": "Vegetable stir fry with tofu and brown rice"
#     },
#     {
#       "day": "Thursday",
#       "breakfast": "Pancakes with maple syrup and fruit",
#       "lunch": "Hummus wrap with hummus, a handful of spinach, tomato and cucumber in a large whole wheat tortilla",
#       "dinner": "Roasted cauliflower and chickpea burritos"
#     },
#     {
#       "day": "Friday",
#       "breakfast": "cereal with milk",
#       "lunch": "Lentil soup",
#       "dinner": "Quinoa and black bean stuffed sweet potatoes"
#     },
#     {
#       "day": "Saturday",
#       "breakfast": "avocado toast",
#       "lunch": "Spinach and fruit smoothies",
#       "dinner": "roasted vegetables and hummus wrap"
#     },
#     {
#       "day": "Sunday",
#       "breakfast": "Tofu scramble",
#       "lunch": "avocado toast",
#       "dinner": "Spaghetti with marinara sauce and roasted vegetables"
#     }
#   ]
# }
# '''
# from models.json_struct import base_structure
# # Load source JSON string into a Python dictionary
# # source_json = json.loads(source_json_str)
# source_json = base_structure
# # Initialize your own JSON structure
# your_json = {"Days": []}

# # Extract data from the source JSON and fill your own JSON structure
# for meal_data in source_json["meal_plan"]:
#     day_data = {}
#     for source_key, target_key in mapping.items():
#         day_data[target_key] = meal_data[source_key]
#     your_json["Days"].append(day_data)

# # Convert your JSON to a string
# your_json_str = json.dumps(your_json, indent=2)

# # Print your JSON
# print(your_json_str)







# def ap2():
#     from models.json_struct import base_structure

#     def has_specific_structure(json_data):
#         # Define the expected structure
#         expected_structure = base_structure
#         # Check if the JSON structure matches the expected structure
#         try:
#             for day, meals in json_data.items():
#                 if day not in expected_structure:
#                     return False
#                 for meal, meal_data in meals.items():
#                     if meal not in expected_structure[day]:
#                         return False
#                     for key, value_type in expected_structure[day][meal].items():
#                         if not isinstance(meal_data.get(key), value_type):
#                             return False
#         except AttributeError:
#             return False

#         return True





# import cohere
# co = cohere.Client('dOsQbNVpPcIncdDvTBecyzdK1a7zupSgYJghCqV3') # This is your trial API key
# response = co.generate(
#   model='command',
#   prompt='Create a weekly meal plan for 3 meals per day, for a 30 years man, with 165 cm and 65 kg, with 2000 calories daily, on a 100 dollars budget. Make all meals Vegan, and Avoid these ingredients: peanuts. And create a list of all ingredients.\nStructure the text in JSON format, including the name of the day, the name of the dish, and all ingredients together unsorted at the end\nDo not include extra text or descriptions. Provide different dishes on different days\nUse this JSON Structure:\n{\n  Monday: {\n    Breakfast: str,\n    Lunch: str,\n    Dinner: str\n  },\n# repeat for all 5 days\nIngredients: list\n}',
#   max_tokens=3058,
#   temperature=0.5,
#   k=0,
#   stop_sequences=[],
#   return_likelihoods='NONE')
# print('Prediction: {}'.format(response.generations[0].text))