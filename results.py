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

frame = tk.Frame(root, bg='#ffffff', width=400, height=400, bd=1, highlightthickness=2,
    highlightcolor="#000000",
    highlightbackground="#000000",
    borderwidth=2)
frame.pack()

def print_table():
    nutrition_facts = tk.Label(frame, fg='#000000', bg='#ffffff', justify=tk.LEFT, width=20, anchor=tk.NW, font=('helvetica', 20, 'bold'), text="Nutrition Facts")
    valeur_nutritive = tk.Label(frame, fg='#000000', bg='#ffffff', justify=tk.LEFT, width=20, anchor=tk.NW, font=('helvetica', 20, 'bold'), text="Valeur nutritive")
    serving_size = tk.Label(frame, fg='#000000', bg='#ffffff', justify=tk.LEFT, width=38, anchor=tk.NW, font=('helvetica', 13, 'normal'), text="Per 100 g / par 100 g")
    nutrition_facts.pack()
    valeur_nutritive.pack()
    serving_size.pack()

    main_line = tk.Canvas(frame, width=340, height=4, bg='#000000', bd=0, highlightthickness=0)
    main_line.pack()

    amount_label = tk.Label(frame, fg='#000000', bg='#ffffff', justify=tk.LEFT, width=42, anchor=tk.NW,
                     font=('helvetica', 10, 'bold'), text="Amount\t\t\t\t       % Daily Value\nTeneur\t\t\t         % valeur quotidienne")
    amount_label.pack()

    second_line = tk.Canvas(frame, width=340, height=3, bg='#000000', bd=0, highlightthickness=0)
    second_line.pack()

def print_nutrition(field, value, ending, percentage):
    # label = tk.Label(frame, fg='#000000', bg='#ffffff', justify=tk.LEFT, width=37, anchor=tk.NW,
    #                  font=('helvetica', 13, 'normal'), text=field + str(value) + ending + " \t\t" + percentage)
    # label.pack()

    nutrition_text = tk.Text(frame, width=37, height=1, font=('helvetica', 13, 'normal'), bd=0, highlightthickness=0)
    nutrition_text.insert("end", field + str(value) + ending + " \t\t\t\t " + percentage)
    nutrition_text.config(state='disabled')
    nutrition_text.pack()
    nutrition_text.tag_configure("BOLD", font=('helvetica', 13, 'bold'))

    if (field == "Calories / Calories "):
        nutrition_text.tag_add("BOLD", "1.0", "end")
    if (field == "Fat / Lipides "):
        nutrition_text.tag_add("BOLD", "1.0", "1.13")
        nutrition_text.tag_add("BOLD", "1.25", "end")
    if (field == "    Saturated / Saturés "):
        nutrition_text.tag_add("BOLD", "1.30", "end")
    if (field == "Cholesterol / Cholestérol "):
        nutrition_text.tag_add("BOLD", "1.0", "1.25")
        nutrition_text.tag_add("BOLD", "1.36", "end")
    if (field == "Sodium / Sodium "):
        nutrition_text.tag_add("BOLD", "1.0", "1.15")
        nutrition_text.tag_add("BOLD", "1.28", "end")
    if (field == "Carbohydrate / Glucides "):
        nutrition_text.tag_add("BOLD", "1.0", "1.23")
    if (field == "    Fibre / Fibres " or field == "    Sugars / Sucres "):
        nutrition_text.tag_add("BOLD", "1.30", "end")
    if (field == "Protein / Protéines "):
        nutrition_text.tag_add("BOLD", "1.0", "1.19")

    if (field == "Vitamin A / Vitamine A " or field == "Vitamin C / Vitamine C " or field == "Calcium / Calcium "):
        nutrition_text.tag_add("BOLD", "1.30", "end")
    if (field == "Potassium " or field == "Iron / Fer "):
        nutrition_text.tag_add("BOLD", "1.20", "end")

    if (field != "    Saturated / Saturés " and field != "    Fibre / Fibres " and field != "Protein / Protéines " and field != "Iron / Fer "):
        general_line = tk.Canvas(frame, width=340, height=2, bg='#000000', bd=0, highlightthickness=0)
        general_line.pack()

    if (field == "    Fibre / Fibres "):
        general_line = tk.Canvas(frame, width=322, height=1, bg='#000000', bd=0, highlightthickness=0)
        general_line.pack(anchor="e")

    if (field == "Protein / Protéines "):
        main_line = tk.Canvas(frame, width=340, height=4, bg='#000000', bd=0, highlightthickness=0)
        main_line.pack()