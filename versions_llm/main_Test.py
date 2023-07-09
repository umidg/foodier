import pandas as pd
import toml
import openai 
import models.user as user

#  Load OPENAI_API from secrets.toml 
openai.api_key = toml.load('secrets.toml')['OPENAI_API_KEY']#os.getenv("OPENAI_API_KEY")

# Function to send prompt to OpenaiAPI
def send_prompt(prompt):
    prompt="""Based on the profile of a 30 years man, with 165 cms and 65 kg, Create a weekly meal plan including 3 meals per day, with 2000 calories daily, on a 100 dolars budget.
     Also include a full list of all ingredients after giving all the meals. No need to include prices"""
    print(f"================\nThis is the plan\n"+prompt)
    
    max_tokens=1000-len(prompt.split())
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.5,
        # stop=["\n"]
    )
    return response



# This model's maximum context length is 2049 tokens, however you requested 4164 tokens (164 in your prompt; 4000 for the completion). Please reduce your prompt; or completion length.

# model="text-ada-001",language="", verbose=True):
#     tokens=int(1000) if int(len(prompt)/4)>250 else int(len(prompt)/4)
# try:
#              openai.Completion.create( 
#                 model =  model,  
#                 prompt = augmented_prompt,
#                 temperature=.5,
#                 max_tokens= tokens,
#             )['choices'][0]['text'].strip()

#     except Exception as e:
#         error="There was an error", str(e) if verbose else ""
#         print(error)
#         st.session_state['summary'] = error
#         st.session_state['saving']=True





if(True):#str(input("Are you Ivan?")).lower()=="yes"):
    name="Ivan"
    age="30"
    height="165"
    weight="65"
    gender = "man"
    number_of_meals="3"
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
pre_prompt_plan=f"""Create a weekly meal plan including {number_of_meals} meals per day, with {calories} calories daily,
on a {budget} dolars budget. """

if(diet != None):
    pre_prompt_diet= f"""Make all meals {diet} """ 
    if(allergies!=None):
        pre_prompt_diet = pre_prompt_diet + ", and "
else:
    pre_prompt_diet= ""

pre_prompt_allergies=f"""Avoid these ingredients: {allergies}. """ if allergies != None else ""

pre_prompt_ingredients =  "And create a list of all ingredients."

pre_prompt = pre_prompt_profile + pre_prompt_plan + pre_prompt_diet + pre_prompt_allergies +pre_prompt_ingredients


pre_prompt_conditioning="""\n\nI am aware that creating a plan requires careful consideration, this is only for simplicity in weekly routine, and illustrative purposes. Please avoid all explanations or warning and just deliver the weekly plan. """
pre_prompt_structure="\n\nWrap everything an html formatted structure"
pre_prompt_distribution= "If the result is longer than the space limitations delivers the result in different requests. I will say \"next day\" and you will send me the meals for next day. Once all days are over, you will give me a full list of ingredients.  "
final_promtp = pre_prompt + pre_prompt_conditioning + pre_prompt_structure + pre_prompt_distribution



final_promtp2 = pre_prompt_profile+pre_prompt_plan
response = send_prompt(final_promtp2)
print(response)
print(response['choices'][0]['text'])



# "For now, give me only the first day, I will keep saying NEXT DAY until we have covered the full meal plan. at the end, I will ask for all ingredients in complete list"

# """**Weekly Vegan Meal Plan Request**
# Profile: 30-year-old man, 165 cm tall, 65 kg weight
# Objective: Create a weekly meal plan with 3 meals per day, 2000 calories daily, and a $100 budget. All meals should be vegan, and avoid peanuts.
# Instructions: Please provide the meal plan for Day 1.
# **Next Day**
#"""


# Approach 2. request a meal , and its shopping list

# if user doesnt exists call set_user()


# def set_user():


#     """Set the user for the session"""
#     name = input("What is your name? ")
#     # get age, height, weight, gender
#     age = input("What is your age? ")
#     height = input("What is your height? ")
#     weight = input("What is your weight? ")
#     gender = input("What is your gender?")
#     # get diet
#     diet = input("What is your diet? ")
#     # get allergies
#     allergies = input("What are your allergies? ")
#     # get intolerances
#     intolerances = input("What are your intolerances? ")
#     # get dislikes
#     dislikes = input("What are your dislikes? ")
#     # get likes
#     likes = input("What are your likes? ")
#     # get cuisine
#     cuisine = input("What is your cuisine? ")
    

#     # newUser= User(name,age,weight,height,gender,diet,allergies)
#     mainUser = user()
#     mainUser.set_name(name)
#     mainUser.set_age(age)
#     mainUser.set_weight(weight)
#     mainUser.set_height(height)
#     mainUser.set_gender(gender)
#     mainUser.set_diet(diet)
#     mainUser.set_allergies(allergies)
#     mainUser.set_intolerances(intolerances)
#     mainUser.set_dislikes(dislikes)
#     mainUser.set_likes(likes)
#     mainUser.set_cuisine(cuisine)
#     # mainUser.set_plan_calories(plan_calories)
#     return mainUser



    

#     return 

