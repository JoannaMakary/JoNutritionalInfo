import tkinter as tk
from tkinter.scrolledtext import ScrolledText

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

# Declaring string variable for storing text
recipe_var = ScrolledText(root, font=("Calibre 15"), height=20, width=40)

# Defining function that will get the recipe and print them on the screen
def submit():
    recipe = recipe_var.get('1.0', 'end-1c')
    print("Your recipe: " + recipe)

# Creating a label for the recipe
recipe_label = tk.Label(root, fg='#424860', bg='#b0bfff', text = 'Enter your recipe', font=('calibre', 12, 'bold'))

# Creating an entry for input
recipe_entry = tk.Entry(root, width=35, textvariable = recipe_var, font=('calibre', 12, 'normal'))

# Creating a button that will submit the function
sub_btn = tk.Button(root, text = 'Submit', command = submit)

# Creating a button where you can submit ingredients
ing_btn = tk.Button(root, text = 'Add ingredient nutrition', command = submit)

# Placing the label, text area and submit button
recipe_label.pack()
recipe_var.pack()
sub_btn.pack(pady=5)
ing_btn.pack( pady=15 )

root.mainloop()