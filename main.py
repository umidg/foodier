import toml
import time
import cohere

cohere_key = toml.load('secrets.toml')['COHERE_API_KEY']
co = cohere.Client(cohere_key) 


# Function to send prompt to Cohere
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





if(True):
    name="Ivan"
    age="30"
    height="165"
    weight="65"
    gender = "man"
    number_of_meals="3"
    days_of_week="weekly" #weekend full week
    calories="2000"
    budget="100"
    diet = "Vegan"
    allergies="peanuts"

else:
    name = input("What is your name? ")
    age = input("What is your age? ")
    height = input("What is your height? ")
    weight = input("What is your weight? ")
    gender = input("What is your gender?")
    number_of_meals=input("How many meals per day")
    calories = input("How many calories per day?")
    budget = input("What is your budget?")
    diet = input("What is your diet? ")
    allergies = input("What are your allergies? ")
    # intolerances = input("What are your intolerances? ")
    # dislikes = input("What are your dislikes? ")
    # likes = input("What are your likes? ")


# ====================
# Create Prompt
# ====================

if(diet != None):
    if_diet= f"""Make all meals {diet}""" 
    if(allergies!=None):
        if_diet = if_diet + ", and"
else:
    if_diet= ""

is_allergic=f""" Avoid these ingredients: {allergies}. """ if allergies != None else ""
json_format="\nUse this JSON Structure:\n{\n  Monday: {\n    Breakfast: str,\n    Lunch: str,\n    Dinner: str\n  },\n# repeat for all 5 days\nIngredients: list\n}"
cohere_prompt=f'Create a weekly meal plan for {number_of_meals} meals per day, for a {age} years {gender}, with {height} cm and {weight} kg, with {calories} calories daily, on a {budget} dollars budget. {if_diet}{is_allergic}And create a list of all ingredients.\nStructure the text in JSON format, including the name of the day, the name of the dish, and all ingredients together unsorted at the end\nDo not include extra text or descriptions. Provide different dishes on different days'+json_format

response = send_prompt(cohere_prompt)
print(response)


