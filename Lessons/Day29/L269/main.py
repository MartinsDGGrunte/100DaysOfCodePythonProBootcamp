from tkinter import *
from tkinter import messagebox
import Lessons.Day29.L269.password_generator_2 as password_generator
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def get_values_from_entries():
    entered_website = website_entry.get()
    entered_username_or_email = email_username_entry.get()
    entered_password = password_entry.get()

    message_for_askokcancel = ("Username: " + entered_username_or_email + "\nPassword: " + entered_password
                               + "\nAre the entered values correct?")

    if entered_username_or_email == "" or entered_password == "":
        messagebox.showerror(message="You must fill all fields!")
    else:
        is_ok = messagebox.askokcancel(title=entered_website, message=message_for_askokcancel)
        if is_ok:
            with open("passwords.txt", "a") as password_file:
                end_structure = entered_website + " | " + entered_username_or_email + " | " + entered_password + "\n"
                password_file.write(end_structure)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def generate_password():
    password_entry.delete(0, END)
    password = password_generator.generate_password()
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- UI SETUP ------------------------------- #

# create a window
window = Tk()
# create title
window.title("Password Manager")
# create padding
window.config(pady=50, padx=50)

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
email_username_entry.insert(0, "martins.g.grunte@gmail.com")

# create Label for "Password"
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# create Entry for "Password"
password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)

# create Generate Password Button
generate_password_button = Button(text="Generate Password", width=13, command=generate_password)
generate_password_button.grid(column=2, row=3)

# create Add Button
add_button = Button(text="Add", width=33, command=get_values_from_entries)
add_button.grid(column=1, row=4, columnspan=2)

# create a closing loop
window.mainloop()
