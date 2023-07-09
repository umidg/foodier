from fastapi import FastAPI,  Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Dict, Any
import json

import toml
import time
import cohere

from send_mail import send_email

# FastAPI 
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="build")

# class SPAStaticFiles(StaticFiles):
#     async def get_response(self, path: str, scope):
#         response = await super().get_response(path, scope)
#         if response.status_code == 404:
#             response = await super().get_response('.', scope)
#         return response
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

def get_ingredients_from_response(_response):
    """
    This function cleans the response from the API, and get ingredients.
    :param _response: The response to be cleaned.
    :return: str
    """
    try:
        print(type(_response))
        if(type(_response)==str):
            _response = json.loads(_response)
        _response_clean = _response["Ingredients"]
        ingredients=",\n ".join(_response_clean)
    except Exception as e:
        print(e)
        ingredients="We were unable to send you all the Ingredients, but here is your weekly plan\n"+str(_response).replace("{","").replace("}","\n")
    return ingredients

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
@app.get("/")
async def serve_spa(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# serves api call to the chatgpt
@app.post("/api")
async def root(body: Dict[Any, Any]): #body
    #parse dictionary of data fields
    name, weight, height, age, diet, allergies, budget, gender , daysofweek, meals, favfood= parse_and_assign(body)
    prompt = create_prompt(name, weight, height, age, diet, allergies, budget, gender , daysofweek, meals, favfood)
    _response = send_prompt(prompt)
    print(_response)

    _response_clean = clean_response(_response)
    
    ingredients = get_ingredients_from_response(_response)
   
    send_email(name, ingredients)
    
    print(_response,"response")


    return {"message": _response}