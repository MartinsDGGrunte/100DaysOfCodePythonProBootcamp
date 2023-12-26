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
canvas.grid(column=1, row=0)

# create Label "Website"
window_label = Label(text="Website:")
window_label.grid(column=0, row=1)

# create Entry for "Website"
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

# create Label for "Email/Username"
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

# create Entry for "Email/Username"
email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)

# create Label for "Password"
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# create Entry for "Password"
password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)

# create Generate Password Button
generate_password_button = Button(text="Generate Password", width=13)
generate_password_button.grid(column=2, row=3)

# create Add Button
add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)

# create a closing loop
window.mainloop()
