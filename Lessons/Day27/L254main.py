from tkinter import *


# we can create a method which will be used by our button when we press on it.
def on_button_pressed():
    label["text"] = "My value has changed!"


def change_the_value_of_label_based_on_entry():
    label["text"] = usr_input.get()


# we can create an instance of a window, but it won't show unless we initialise it.
window = Tk()

# we can create a title of our window
window.title("Lesson 248 GUI")

# we can create the minimum size of our window
window.minsize(width=500, height=300)

# we can add a label to our window, but it won't show unless we add it to our window
label = Label(window, text="Lesson 248", font=("Arial", 24, "bold"))
# add them to our window
label.grid(column=0, row=0)


# we can also create buttons
button = Button(window, text="Click Me!", command=on_button_pressed)
# add the button to our window
button.grid(column=1, row=1)

# we can also register user entries
usr_input = Entry()
usr_input.grid(column=2, row=0)

# we can get the provided text from the Entry() field
usr_provided_value = usr_input.get()


new_button = Button(text="Change Label!", command=change_the_value_of_label_based_on_entry)
new_button.grid(column=3, row=2)

# this is the way how the screen is initialised, and it should be the last line of our program.
window.mainloop()
