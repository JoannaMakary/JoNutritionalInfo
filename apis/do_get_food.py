# Using the USDA FoodData Central API, obtain nutritional information needed for a Nutrition Facts Label

import requests
import json

# Daily values (https://www.canada.ca/en/health-canada/services/understanding-food-labels/percent-daily-value.html)
daily_fat = 65
daily_satFat = 20
daily_cholestrol = 300
daily_sodium = 2400
daily_carbs = 300
daily_fibre = 25
daily_vitaminA = 1000
daily_vitaminC = 60
daily_calcium = 1100
daily_iron = 14

def get_food(recipe):
    # name = input("Product name: ")
    fdc_api = 'WZV2Zcwom2sdwtKdWuFOC5g5tabcgXbHqjLF6oA7'
    data_type = 'Survey (FNDDS)'
    PARAMS = {'api_key':fdc_api, 'query':recipe, 'dataType':data_type}

    response = requests.get("https://api.nal.usda.gov/fdc/v1/foods/search", params = PARAMS)

    def jprint(obj):
        # create a formatted string of the Python JSON object
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    # Prints all the data found
    # jprint(response.json())
    global data
    data = response.json()
    # Print all data about the first result
    jprint(data["foods"][0])

    get_food_info()

def find_food_keys():
    # Find the keys that contains each nutrition value
    global calorie_index, fat_index, satFat_index, transFat_index, chlstrl_index, sodium_index, carb_index, fibre_index, sugar_index, protein_index, potassium_index, vitaminA_index, vitaminC_index, iron_index, calcium_index
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
        if data["foods"][0]["foodNutrients"][x]["nutrientName"] == "Potassium, K":
            potassium_index = x
        if data["foods"][0]["foodNutrients"][x]["nutrientName"] == "Vitamin A, RAE":
            vitaminA_index = x
        if data["foods"][0]["foodNutrients"][x]["nutrientName"] == "Vitamin C, total ascorbic acid":
            vitaminC_index = x
        if data["foods"][0]["foodNutrients"][x]["nutrientName"] == "Calcium, Ca":
            calcium_index = x
        if data["foods"][0]["foodNutrients"][x]["nutrientName"] == "Iron, Fe":
            iron_index = x

def get_food_info():

    print("Nutrition Facts/Valeur nutritive")
    print("Serving Size (100g)/portion (100g)")
    print("===================================")

    find_food_keys()

    print("Calories: ")
    # Prints out the Calories of requested food item
    food_calories = data["foods"][0]["foodNutrients"][calorie_index]["value"]
    print(food_calories)

    import results
    results.print_something("Calories: ", food_calories, "")

    print("Fat/Lipides: (g)")
    # Prints out the Fat of requested food item
    food_fat = data["foods"][0]["foodNutrients"][fat_index]["value"]
    print(food_fat)
    # Divide food fat by daily fat and get % for daily value
    print(str(round((food_fat)/(daily_fat), 2) * 100) + " %")
    results.print_something("Fat: ", food_fat, " g")

    # Prints out the Saturated Fat of requested food item
    print("+ Saturated/Saturés (g): ")
    food_satFat = data["foods"][0]["foodNutrients"][satFat_index]["value"]
    print(food_satFat)
    # Divide food saturated fat by daily saturated fat and get % for daily value
    print(str(round((food_satFat)/(daily_satFat), 2) * 100) + " %")
    results.print_something("    Saturated Fat: ", food_satFat, " g")

    # Prints out the Trans Fat of requested food item
    print("+ Trans/trans (g): ")
    # Does not exist for most food items, check if it exists. If not, print 0.
    if(transFat_index != 99):
        food_transFat = data["foods"][0]["foodNutrients"][transFat_index]["value"]
        print(food_transFat)
    else:
        food_transFat = 0
        print(food_transFat)
    results.print_something("    + Trans Fat: ", food_transFat, " g")

    # Prints out the Cholesterol of requested food item
    print("Cholesterol/Cholestérol: (mg)")
    food_cholesterol = data["foods"][0]["foodNutrients"][chlstrl_index]["value"]
    print(food_cholesterol)
    # Divide food cholesterol by daily cholesterol and get % for daily value
    print(str(round((food_cholesterol)/(daily_cholestrol), 2) * 100) + " %")
    results.print_something("Cholesterol: ", food_cholesterol, " g")

    # Prints out the Sodium of requested food item
    print("Sodium/Sodium: (mg)")
    food_sodium = data["foods"][0]["foodNutrients"][sodium_index]["value"]
    print(food_sodium)
    # Divide food sodium by daily sodium and get % for daily value
    print(str(round((food_sodium)/(daily_sodium), 2) * 100) + " %")
    results.print_something("Sodium: ", food_sodium, " mg")

    # Prints out the Carbohydrates of requested food item
    print("Carbohydrate/Glucides: (g)")
    food_carbs = data["foods"][0]["foodNutrients"][carb_index]["value"]
    print(food_carbs)
    # Divide food carbs by daily carbs and get % for daily value
    print(str(round((food_carbs)/(daily_carbs), 2) * 100) + " %")
    results.print_something("Carbohydrate: ", food_carbs, " g")

    # Prints out the Fibre of requested food item
    print("Fibre/Fibres: (g)")
    food_fibre = data["foods"][0]["foodNutrients"][fibre_index]["value"]
    print(food_fibre)
    # Divide food fibre by daily fibre and get % for daily value
    print(str(round((food_fibre)/(daily_fibre), 2) * 100) + " %")
    results.print_something("Fibre: ", food_fibre, " g")

    # Prints out the Sugars of requested food item
    print("Sugars/Sucres: (g)")
    food_sugar = data["foods"][0]["foodNutrients"][sugar_index]["value"]
    print(food_sugar)
    results.print_something("Sugars: ", food_sugar, " g")

    # Prints out the Protein of requested food item
    print("Protein/Protéines: (g)")
    food_protein = data["foods"][0]["foodNutrients"][protein_index]["value"]
    print(food_protein)
    results.print_something("Protein: ", food_protein, " g")

    # Prints out the Potassium of requested food item
    print("Potassium: (mg)")
    food_potassium = data["foods"][0]["foodNutrients"][potassium_index]["value"]
    print(food_potassium)
    results.print_something("Potassium: ", food_potassium, " mg")

    # Prints out the Daily Value of Vitamin A of requested food item
    print("Vitamin A")
    food_vitaminA = data["foods"][0]["foodNutrients"][vitaminA_index]["value"]
    print(str(round((food_vitaminA)/(daily_vitaminA), 2) * 100) + " %")

    # Prints out the Daily Value of VitaminC of requested food item
    print("Vitamin C")
    food_vitaminC = data["foods"][0]["foodNutrients"][vitaminC_index]["value"]
    print(str(round((food_vitaminC)/(daily_vitaminC), 2) * 100) + " %")

    # Prints out the Daily Value of Calcium of requested food item
    print("Calcium: (mg)")
    food_calcium = data["foods"][0]["foodNutrients"][calcium_index]["value"]
    print(food_calcium)
    print(str(round((food_calcium)/(daily_calcium), 2) * 100) + " %")
    results.print_something("Calcium: ", food_fat, " mg")

    # Prints out the Daily Value of Iron of requested food item
    print("Iron: (mg)")
    food_iron = data["foods"][0]["foodNutrients"][iron_index]["value"]
    print(food_iron)
    print(str(round((food_iron)/(daily_iron), 2) * 100) + " %")
    results.print_something("Iron: ", food_iron, " mg")