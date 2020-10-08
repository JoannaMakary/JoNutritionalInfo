import tkinter as tk

root = tk.Tk()
# The values I have set my window size to be
windowWidth = 600
windowHeight = 600

# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

# Name the window
root.title("Recipe Results - Jo's Nutrition Application")
# Change icon of window
root.iconbitmap('joicon.ico')
# Positions the window in the center of the page.
root.geometry("600x600+{}+{}".format(positionRight, positionDown))
root['background']='#b0bfff'

def print_something(field, value, ending):
    label = tk.Label(root, text = field + str(value) + ending)
    label.pack()