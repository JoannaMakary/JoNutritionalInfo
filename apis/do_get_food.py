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
daily_sugar = 100
daily_vitaminA = 1000
daily_vitaminC = 60
daily_potassium = 4700
daily_calcium = 1100
daily_iron = 14

total_amount = int()
total_calories = int()
total_fat = int()
total_fatPERCENT = int()
total_satfat = int()
total_satfatPERCENT = int()
total_transfat = int()
total_cholestrol = int()
total_cholestrolPERCENT = int()
total_sodium = int()
total_sodiumPERCENT = int()
total_carbs = int()
total_fibre = int()
total_fibrePERCENT = int()
total_sugar = int()
total_sugarPERCENT = int()
total_protein = int()
total_vitA = int()
total_vitAPERCENT = int()
total_vitC = int()
total_vitCPERCENT = int()
total_potassium = int()
total_potassiumPERCENT = int()
total_calcium = int()
total_calciumPERCENT = int()
total_iron = int()
total_ironPERCENT = int()

def get_food(recipe, amount):
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

    get_food_info(amount)

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


def get_food_info(amount):
    global total_amount, total_calories, total_fat, total_fatPERCENT, total_satfat, total_satfatPERCENT, total_transfat, total_cholestrol, total_cholestrolPERCENT, total_sodium, total_sodiumPERCENT, total_carbs, total_fibre, total_fibrePERCENT, total_sugar, total_sugarPERCENT, total_protein, total_vitA, total_vitAPERCENT, total_vitC, total_vitCPERCENT, total_potassium, total_potassiumPERCENT, total_calcium, total_calciumPERCENT, total_iron, total_ironPERCENT

    find_food_keys()

    # Adds to total recipe's amount
    total_amount = total_amount + amount

    # Gets Calories of requested food item based on amount
    food_calories = int((amount/100)*(data["foods"][0]["foodNutrients"][calorie_index]["value"]))
    # Adds to total recipe's calories
    total_calories += food_calories

    # Gets Fat of requested food item based on amount
    food_fat = int((amount/100)*(data["foods"][0]["foodNutrients"][fat_index]["value"]))
    # Divide food fat by daily fat and get % for daily value
    fat_percent = int(round((food_fat)/(daily_fat), 2) * 100)
    # Adds to total recipe's fat and fat percentage
    total_fat += food_fat
    total_fatPERCENT += fat_percent

    # Gets Saturated Fat of requested food item based on amount
    food_satFat = int((amount/100)*(data["foods"][0]["foodNutrients"][satFat_index]["value"]))
    # Divide food saturated fat by daily saturated fat and get % for daily value
    satFat_percent = int(round((food_satFat)/(daily_satFat), 2) * 100)
    # Adds to total recipe's saturated fat and saturated fat percentage
    total_satfat += food_satFat
    total_satfatPERCENT += satFat_percent

    # Gets Trans Fat of requested food item based on amount
    # Does not exist for most food items, check if it exists. If not, print 0.
    if(transFat_index != 99):
        food_transFat = int((amount/100)*(data["foods"][0]["foodNutrients"][transFat_index]["value"]))
    else:
        food_transFat = 0
    # Adds to total recipe's trans fat
    total_transfat += food_transFat

    # Gets Cholesterol of requested food item based on amount
    food_cholesterol = int((amount/100)*(data["foods"][0]["foodNutrients"][chlstrl_index]["value"]))
    # Divide food cholesterol by daily cholesterol and get % for daily value
    cholesterol_percent = int(round((food_cholesterol)/(daily_cholestrol), 2) * 100)
    # Adds to total recipe's cholesterol and cholesterol percentage
    total_cholestrol += food_cholesterol
    total_cholestrolPERCENT += cholesterol_percent

    # Gets Sodium of requested food item based on amount
    food_sodium = int((amount/100)*(data["foods"][0]["foodNutrients"][sodium_index]["value"]))
    # Divide food sodium by daily sodium and get % for daily value
    sodium_percent = int(round((food_sodium)/(daily_sodium), 2) * 100)
    # Adds to total recipe's sodium and sodium percentage
    total_sodium += food_sodium
    total_sodiumPERCENT += sodium_percent

    # Gets Carbohydrates of requested food item based on amount
    food_carbs = int((amount/100)*(data["foods"][0]["foodNutrients"][carb_index]["value"]))
    # Adds to total recipe's calories
    total_carbs += food_carbs

    # Gets Fibre of requested food item based on amount
    food_fibre = int((amount/100)*(data["foods"][0]["foodNutrients"][fibre_index]["value"]))
    # Divide food fibre by daily fibre and get % for daily value
    fibre_percent = int(round((food_fibre)/(daily_fibre), 2) * 100)
    # Adds to total recipe's fibre and fibre percentage
    total_fibre += food_fibre
    total_fibrePERCENT += fibre_percent

    # Gets Sugar of requested food item based on amount
    food_sugar = int((amount/100)*(data["foods"][0]["foodNutrients"][sugar_index]["value"]))
    # Divide food sugar by daily sugar and get % for daily value
    sugar_percent = int(round((food_sugar)/(daily_sugar), 2) * 100)
    # Adds to total recipe's sugar and sugar percentage
    total_sugar += food_sugar
    total_sugarPERCENT += sugar_percent

    # Gets Protein of requested food item based on amount
    food_protein = int((amount/100)*(data["foods"][0]["foodNutrients"][protein_index]["value"]))
    # Adds to total recipe's protein
    total_protein += food_protein

    # Gets Vitamin A of requested food item based on amount
    food_vitaminA = int((amount/100)*(data["foods"][0]["foodNutrients"][vitaminA_index]["value"]))
    # Divide food vitamin A by daily vitamin A and get % for daily value
    vitaminA_percent = int(round((food_vitaminA) / (daily_vitaminA), 2) * 100)
    # Adds to total recipe's vitamin A and vitamin A percentage
    total_vitA += food_vitaminA
    total_vitAPERCENT += vitaminA_percent

    # Gets Vitamin C of requested food item based on amount
    food_vitaminC = int((amount/100)*(data["foods"][0]["foodNutrients"][vitaminC_index]["value"]))
    # Divide food vitamin C by daily vitamin C and get % for daily value
    vitaminC_percent = int(round((food_vitaminC) / (daily_vitaminC), 2) * 100)
    # Adds to total recipe's vitamin C and vitamin C percentage
    total_vitC += food_vitaminC
    total_vitCPERCENT += vitaminC_percent

    # Gets Potassium of requested food item based on amount
    food_potassium = int((amount/100)*(data["foods"][0]["foodNutrients"][potassium_index]["value"]))
    # Divide food Potassium by daily Potassium and get % for daily value
    potassium_percent = int(round((food_potassium) / (daily_potassium), 2) * 100)
    # Adds to total recipe's Potassium and Potassium percentage
    total_potassium += food_potassium
    total_potassiumPERCENT += potassium_percent

    # Gets Calcium of requested food item based on amount
    food_calcium = int((amount/100)*(data["foods"][0]["foodNutrients"][calcium_index]["value"]))
    # Divide food Calcium by daily Calcium and get % for daily value
    calcium_percent = int(round((food_calcium)/(daily_calcium), 2) * 100)
    # Adds to total recipe's calcium and calcium percentage
    total_calcium += food_calcium
    total_calciumPERCENT += calcium_percent

    # Gets Iron of requested food item based on amount
    food_iron = int((amount/100)*(data["foods"][0]["foodNutrients"][iron_index]["value"]))
    # Divide food Iron by daily Iron and get % for daily value
    iron_percent = int(round((food_iron)/(daily_iron), 2) * 100)
    # Adds to total recipe's iron and iron percentage
    total_iron += food_iron
    total_ironPERCENT += iron_percent


def print_total():
    global total_amount, total_calories, total_fat, total_fatPERCENT, total_satfat, total_satfatPERCENT, total_transfat, total_cholestrol, total_cholestrolPERCENT, total_sodium, total_sodiumPERCENT, total_carbs, total_fibre, total_fibrePERCENT, total_sugar, total_sugarPERCENT, total_protein, total_vitA, total_vitAPERCENT, total_vitC, total_vitCPERCENT, total_potassium, total_potassiumPERCENT, total_calcium, total_calciumPERCENT, total_iron, total_ironPERCENT
    import results

    results.print_table(total_amount)
    results.print_nutrition("Calories / Calories ", str(total_calories), "", "")
    results.print_nutrition("Fat / Lipides ", str(total_fat), " g", str(total_fatPERCENT) + " %")
    results.print_nutrition("    Saturated / Saturés ", str(total_satfat), " g", str(total_satfatPERCENT) + " %")
    results.print_nutrition("    + Trans / trans: ", str(total_transfat), " g", "")
    results.print_nutrition("Cholesterol / Cholestérol ", str(total_cholestrol), " g", str(total_cholestrolPERCENT) + " %")
    results.print_nutrition("Sodium / Sodium ", str(total_sodium), " mg", str(total_sodiumPERCENT) + " %")
    results.print_nutrition("Carbohydrate / Glucides ", str(total_carbs), " g", "")
    results.print_nutrition("    Fibre / Fibres ", str(total_fibre), " g", str(total_fibrePERCENT) + " %")
    results.print_nutrition("    Sugars / Sucres ", str(total_sugar), " g", str(total_sugarPERCENT) + " %")
    results.print_nutrition("Protein / Protéines ", str(total_protein), " g", "")
    results.print_nutrition("Vitamin A / Vitamine A ", str(total_vitA), " RAE", str(total_vitAPERCENT) + " %")
    results.print_nutrition("Vitamin C / Vitamine C ", str(total_vitC), " mg", str(total_vitCPERCENT) + " %")
    results.print_nutrition("Potassium ", str(total_potassium), " mg", str(total_potassiumPERCENT) + " %")
    results.print_nutrition("Calcium / Calcium ", str(total_calcium), " mg", str(total_calciumPERCENT) + " %")
    results.print_nutrition("Iron / Fer ", str(total_iron), " mg", str(total_ironPERCENT) + " %")

def print_per_portion(portion):
    global total_amount, total_calories, total_fat, total_fatPERCENT, total_satfat, total_satfatPERCENT, total_transfat, total_cholestrol, total_cholestrolPERCENT, total_sodium, total_sodiumPERCENT, total_carbs, total_fibre, total_fibrePERCENT, total_sugar, total_sugarPERCENT, total_protein, total_vitA, total_vitAPERCENT, total_vitC, total_vitCPERCENT, total_potassium, total_potassiumPERCENT, total_calcium, total_calciumPERCENT, total_iron, total_ironPERCENT

    # portion_calc = (user_input/total_amount)
    # Calculating based on portion size for each
    total_amount = round(total_amount / int(portion))
    total_calories = round(total_calories / int(portion))
    total_fat = round(total_fat / int(portion))
    total_fatPERCENT = round(total_fatPERCENT / int(portion))
    total_satfat = round(total_satfat / int(portion))
    total_satfatPERCENT = round(total_satfatPERCENT / int(portion))
    total_transfat = round(total_transfat / int(portion))
    total_cholestrol = round(total_cholestrol / int(portion))
    total_cholestrolPERCENT = round(total_cholestrolPERCENT / int(portion))
    total_sodium = round(total_sodiumPERCENT / int(portion))
    total_carbs = round(total_carbs / int(portion))
    total_fibre = round(total_fibre / int(portion))
    total_fibrePERCENT = round(total_fibrePERCENT / int(portion))
    total_sugar = round(total_sugar / int(portion))
    total_sugarPERCENT = round(total_sugarPERCENT / int(portion))
    total_protein = round(total_protein / int(portion))
    total_vitA = round(total_vitA / int(portion))
    total_vitAPERCENT = round(total_vitAPERCENT / int(portion))
    total_vitC = round(total_vitC / int(portion))
    total_vitCPERCENT = round(total_vitCPERCENT / int(portion))
    total_potassium = round(total_potassium / int(portion))
    total_potassiumPERCENT = round(total_potassiumPERCENT / int(portion))
    total_calcium = round(total_calcium / int(portion))
    total_calciumPERCENT = round(total_calciumPERCENT / int(portion))
    total_iron = round(total_iron / int(portion))
    total_ironPERCENT = round(total_ironPERCENT / int(portion))

    import results
    results.print_table(total_amount)
    results.print_nutrition("Calories / Calories ", str(total_calories), "", "")
    results.print_nutrition("Fat / Lipides ", str(total_fat), " g", str(total_fatPERCENT) + " %")
    results.print_nutrition("    Saturated / Saturés ", str(total_satfat), " g", str(total_satfatPERCENT) + " %")
    results.print_nutrition("    + Trans / trans: ", str(total_transfat), " g", "")
    results.print_nutrition("Cholesterol / Cholestérol ", str(total_cholestrol), " g", str(total_cholestrolPERCENT) + " %")
    results.print_nutrition("Sodium / Sodium ", str(total_sodium), " mg", str(total_sodiumPERCENT) + " %")
    results.print_nutrition("Carbohydrate / Glucides ", str(total_carbs), " g", "")
    results.print_nutrition("    Fibre / Fibres ", str(total_fibre), " g", str(total_fibrePERCENT) + " %")
    results.print_nutrition("    Sugars / Sucres ", str(total_sugar), " g", str(total_sugarPERCENT) + " %")
    results.print_nutrition("Protein / Protéines ", str(total_protein), " g", "")
    results.print_nutrition("Vitamin A / Vitamine A ", str(total_vitA), " RAE", str(total_vitAPERCENT) + " %")
    results.print_nutrition("Vitamin C / Vitamine C ", str(total_vitC), " mg", str(total_vitCPERCENT) + " %")
    results.print_nutrition("Potassium ", str(total_potassium), " mg", str(total_potassiumPERCENT) + " %")
    results.print_nutrition("Calcium / Calcium ", str(total_calcium), " mg", str(total_calciumPERCENT) + " %")
    results.print_nutrition("Iron / Fer ", str(total_iron), " mg", str(total_ironPERCENT) + " %")