from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# create a window
window = Tk()
# create title
window.title("Password Manager")
# create padding
window.config(pady=20, padx=20)

# create Canvas
canvas = Canvas(height=200, width=200)
# create image reference
logo_reference = PhotoImage(file="../password-manager-start/logo.png")
# create image in canvas
logo_image = canvas.create_image(100, 100, image=logo_reference)
# add canvas
canvas.pack()

# create a closing loop
window.mainloop()
