# Using the USDA FoodData Central API, obtain nutritional information needed for a Nutrition Facts Label

import requests
import json

name = input("Product name: ")
fdc_api = 'WZV2Zcwom2sdwtKdWuFOC5g5tabcgXbHqjLF6oA7'
data = 'Survey (FNDDS)'
PARAMS = {'api_key':fdc_api, 'query':name, 'dataType':data}

response = requests.get("https://api.nal.usda.gov/fdc/v1/foods/search", params = PARAMS)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# Prints all the data found
# jprint(response.json())

data = response.json()
# Print all data about the first result
jprint(data["foods"][0])

print("Nutrition Facts/Valeur nutritive")
print("Serving Size (100g)/portion (100g)")
print("===================================")


# Find the keys that contains each nutrition value
for x in range(0, len(data["foods"][0]["foodNutrients"])):
    transFat_index = 99
    if data["foods"][0]["foodNutrients"][x]["nutrientName"] == "Energy":
        calorie_index = x
    if data["foods"][0]["foodNutrients"][x]["nutrientName"] == "Total lipid (fat)":
        fat_index = x
    if data["foods"][0]["foodNutrients"][x]["nutrientName"] == "Fatty acids, total saturated":
        satFat_index = x
    if data["foods"][0]["foodNutrients"][x]["nutrientName"] == "Fatty acids, total trans":
        transFat_index = x
    if data["foods"][0]["foodNutrients"][x]["nutrientName"] == "Cholesterol":
        chlstrl_index = x
    if data["foods"][0]["foodNutrients"][x]["nutrientName"] == "Sodium, Na":
        sodium_index = x
    if data["foods"][0]["foodNutrients"][x]["nutrientName"] == "Carbohydrate, by difference":
        carb_index = x
    if data["foods"][0]["foodNutrients"][x]["nutrientName"] == "Fiber, total dietary":
        fibre_index = x
    if data["foods"][0]["foodNutrients"][x]["nutrientName"] == "Sugars, total including NLEA":
        sugar_index = x
    if data["foods"][0]["foodNutrients"][x]["nutrientName"] == "Protein":
        protein_index = x


print("Calories: ")
# Prints out the Calories of requested food item
jprint(data["foods"][0]["foodNutrients"][calorie_index]["value"])


print("Fat/Lipides: (g)")
# Prints out the Fat of requested food item
jprint(data["foods"][0]["foodNutrients"][fat_index]["value"])

# Prints out the Saturated Fat of requested food item
print("+ Saturated/Saturés (g): ")
jprint(data["foods"][0]["foodNutrients"][satFat_index]["value"])

# Prints out the Trans Fat of requested food item
print("+ Trans/trans (g): ")
# Does not exist for most food items, check if it exists. If not, print 0.
if(transFat_index != 99):
    jprint(data["foods"][0]["foodNutrients"][transFat_index]["value"])
else:
    print(0)

# Prints out the Cholestrol of requested food item
print("Cholesterol/Cholestérol: (mg)")
jprint(data["foods"][0]["foodNutrients"][chlstrl_index]["value"])

# Prints out the Sodium of requested food item
print("Sodium/Sodium: (mg)")
jprint(data["foods"][0]["foodNutrients"][sodium_index]["value"])

# Prints out the Carbohydrates of requested food item
print("Carbohydrate/Glucides: (g)")
jprint(data["foods"][0]["foodNutrients"][carb_index]["value"])

# Prints out the Fibre of requested food item
print("Fibre/Fibres: (g)")
jprint(data["foods"][0]["foodNutrients"][fibre_index]["value"])

# Prints out the Sugars of requested food item
print("Sugars/Sucres: (g)")
jprint(data["foods"][0]["foodNutrients"][sugar_index]["value"])

# Prints out the Protein of requested food item
print("Protein/Protéines: (g)")
jprint(data["foods"][0]["foodNutrients"][protein_index]["value"])