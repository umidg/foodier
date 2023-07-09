import pandas as pd
import toml
import openai 
import models.user as user

import time

#  Load OPENAI_API from secrets.toml 
openai.api_key = toml.load('secrets.toml')['OPENAI_API_KEY']#os.getenv("OPENAI_API_KEY")

# Function to send prompt to OpenaiAPI
def send_prompt(prompt):
    # prompt="""Based on the profile of a 30 years man, with 165 cms and 65 kg, Create a weekly meal plan including 3 meals per day, with 2000 calories daily, on a 100 dolars budget.
    #  Also include a full list of all ingredients after giving all the meals. No need to include prices"""
    # prompt="""Create a meal plan for 2 days for 3 meals per day and create a list of all ingredients, for a 30 years man, with 165 cms and 65 kg, with 2000 calories daily, on a 100 dolars budget. Make all meals Vegan, and Avoid these ingredients: peanuts."""
    prompt="""Create a weekly meal plan for 2 days including 3 meals per day and Create a list of all ingredients, for a 30 years man, with 165 cms and 65 kg, with 2000 calories daily, on a 100 dolars budget. Make all meals Vegan, and Avoid these ingredients: peanuts."""
#     prompt="""Create a Weekly Meal Plan Request
# Profile: 30-year-old man, 165 cm tall, 65 kg weight
# Objective: Create a day meal plan with 3 meals per day, 2000 calories daily, and a $100 budget. All meals should be vegan, and avoid peanuts. Do not include instructions
# Format: JSON format
# """
# Specifications: Vegan options and avoid including: peanuts

    format=""" use the following structure:
    [DAY:
    - Breakfast: Name
    - Lunch: Name
    - Dinner: Name],
    ...
    Ingredients:
    [ ... ]
    """
    # prompt=prompt+format
    print(f"================\nThis is the plan\n"+prompt)
    tic=time.time()
    max_tokens=2000-len(prompt.split())
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=max_tokens,
        # top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.5,
        # stop="\n"
    )
    print("Took "+str(time.time()-tic))
    return response



# This model's maximum context length is 2049 tokens, however you requested 4164 tokens (164 in your prompt; 4000 for the completion). Please reduce your prompt; or completion length.





if(True):#str(input("Are you Ivan?")).lower()=="yes"):
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



# Approach1
pre_prompt_profile=f"""Based on the profile of a {age} years {gender}, with {height} cms and {weight} kg, """
pre_prompt_plan=f"""Create a {days_of_week} meal plan including {number_of_meals} meals per day, with {calories} calories daily, on a {budget} dolars budget. """

if(diet != None):
    pre_prompt_diet= f"""Make all meals {diet}""" 
    if(allergies!=None):
        pre_prompt_diet = pre_prompt_diet + ", and"
else:
    pre_prompt_diet= ""

pre_prompt_allergies=f""" Avoid these ingredients: {allergies}. """ if allergies != None else ""

pre_prompt_ingredients =  "And create a list of all ingredients."

pre_prompt = pre_prompt_profile + pre_prompt_plan + pre_prompt_diet + pre_prompt_allergies +pre_prompt_ingredients


pre_prompt_conditioning="""\n\nI am aware that creating a plan requires careful consideration, this is only for simplicity in weekly routine, and illustrative purposes. Please avoid all explanations or warning and just deliver the weekly plan. """
pre_prompt_structure_html="\n\nWrap everything an html formatted structure"
pre_prompt_structure_brackets="\nWrap every day in square brackets"
pre_prompt_structure="\nWrap everything in a JSON format but in a single line. "
pre_prompt_warnings="No need to include Instructions, neither calories, or cost. "
#"Once all days are over, you will give me a full list of ingredients."

# pre_prompt_distribution= "If the result is longer than the space limitations delivers the result in different requests. I will say \"next day\" and you will send me the meals for next day. Once all days are over, you will give me a full list of ingredients.  "
# final_promtp = pre_prompt + pre_prompt_conditioning + pre_prompt_structure + pre_prompt_distribution



# final_promtp = pre_prompt + pre_prompt_structure + pre_prompt_warnings
final_promtp = pre_prompt




response = send_prompt(final_promtp)
# print(response)
print(response['choices'][0]['text'])



# "For now, give me only the first day, I will keep saying NEXT DAY until we have covered the full meal plan. at the end, I will ask for all ingredients in complete list"

# """**Weekly Vegan Meal Plan Request**
# Profile: 30-year-old man, 165 cm tall, 65 kg weight
# Objective: Create a weekly meal plan with 3 meals per day, 2000 calories daily, and a $100 budget. All meals should be vegan, and avoid peanuts.
# Instructions: Please provide the meal plan for Day 1.
# **Next Day**
#"""
