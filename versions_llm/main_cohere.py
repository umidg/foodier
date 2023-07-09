#Generate a JSON object representing a weekly meal plan and list of ingredients.
# A for loop, asking for a Single day of the week. 

_prompt='Create a weekly meal plan for 3 meals per day, for a 30 years man, with 165 cm and 65 kg, with 2000 calories daily, on a 100 dollars budget. Make all meals Vegan, and Avoid these ingredients: peanuts. And create a list of all ingredients.\nStructure the text in JSON format, including the name of the day, the name of the dish, and all ingredients together unsorted at the end\nDo not include extra text or descriptions. Provide different dishes on different days'

import cohere
co = cohere.Client('dOsQbNVpPcIncdDvTBecyzdK1a7zupSgYJghCqV3') # This is your trial API key

response = co.generate(
  model='command',
  prompt=_prompt,
  max_tokens=3058,
  temperature=0.5,
  k=0,
  stop_sequences=[],
  return_likelihoods='NONE')

print('Prediction: {}'.format(response.generations[0].text))


# import cohere
# co = cohere.Client('dOsQbNVpPcIncdDvTBecyzdK1a7zupSgYJghCqV3') # This is your trial API key
# response = co.generate(
#   model='command',
#   prompt='Create a weekly days meal plan for 3 meals per day, provide different dishes on different days, for a 30 years man, with 165 cm and 65 kg, with 2000 calories daily, on a 100 dollars budget. Make all meals Vegan, and Avoid these ingredients: peanuts. And create a list of all ingredients.\nStructure the text in JSON format, including the name of the day, the name of the dish, and all ingredients together at the end\nDo not include extra text or descriptions.',
#   max_tokens=3506,
#   temperature=0.8,
#   k=0,
#   stop_sequences=["\'\n\'"],
#   return_likelihoods='GENERATION')
# print('Prediction: {}'.format(response.generations[0].text))


# import cohere
# co = cohere.Client('dOsQbNVpPcIncdDvTBecyzdK1a7zupSgYJghCqV3') # This is your trial API key
# response = co.generate(
#   model='command',
#   prompt='Create a 2 days meal plan for 3 meals per day, for a 30 years man, with 165 cms and 65 kg, with 2000 calories daily, on a 100 dolars budget. Make all meals Vegan, and Avoid these ingredients: peanuts.  and create a list of all ingredients',
#   max_tokens=2034,
#   temperature=0.8,
#   k=0,
#   stop_sequences=["\'\n\'"],
#   return_likelihoods='NONE')
# print('Prediction: {}'.format(response.generations[0].text))