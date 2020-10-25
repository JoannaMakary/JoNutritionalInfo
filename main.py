import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import re

root = tk.Tk()
# The values I have set my window size to be
windowWidth = 600
windowHeight = 600

# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

# Name the window
root.title("Jo's Nutrition Application")
# Change icon of window
root.iconbitmap('joicon.ico')
# Positions the window in the center of the page.
root.geometry("600x600+{}+{}".format(positionRight, positionDown))
root['background']='#b0bfff'

# Declaring string variable for storing recipe text
recipe_var = ScrolledText(root, font=("Calibre 15"), height=20, width=40)

# Declaring string variable for storing user portion requested
portion_var = tk.Entry(root, font=("Calibre 15"), width=2)

# Defining function that will get the recipe and print them on the screen
def submit():
    # Get user input from the GUI
    recipe = recipe_var.get('1.0', 'end-1c')
    portion = portion_var.get()
    # Split each line into a list
    full_recipe = recipe.splitlines()

    import apis.do_get_food as api
    full_recipe_length = len(full_recipe)
    # For each list item, get food nutrition
    for i in range(full_recipe_length):
        amount = int(re.search('\d+(?=g)', full_recipe[i])[0])
        food_item = (re.search('(?<=\dg )(.*)', full_recipe[i])[0])
        api.get_food(food_item, amount)

    # If no portion is entered, assume to print full recipe
    if portion == "" or portion == "1":
        api.print_total()
    else:
        api.print_per_portion(portion)

# Creating a label for the recipe
recipe_label = tk.Label(root, fg='#424860', bg='#b0bfff', text = 'Enter your recipe', font=('calibre', 12, 'bold'))

# Creating a label for the user input portion
portion_text = tk.Label(root, fg='#424860', bg='#b0bfff', text="Number of portions", font=('calibre', 12, 'bold'))

# Creating an entry for input
recipe_entry = tk.Entry(root, width=35, textvariable = recipe_var, font=('calibre', 12, 'normal'))

# Creating a button that will submit the function
sub_btn = tk.Button(root, text = 'Submit', command = submit)

# Placing the label, text area and submit button
recipe_label.pack()
recipe_var.pack()
portion_text.pack()
portion_var.pack()
sub_btn.pack(pady=5)

root.mainloop()