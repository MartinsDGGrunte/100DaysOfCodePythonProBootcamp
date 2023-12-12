from tkinter import *


# create a method which will be used for calculations
def convert_miles_to_km():
    miles = int(input_field.get())
    km = miles * 1.609
    end_value_label["text"] = str(km)


window = Tk()
window.title("Miles to Km converter")

# add field for getting user input
input_field = Entry(width=10)
input_field.grid(column=1, row=0, pady=10)

# add label which says that we are using entry section to provide Miles
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0, padx=15)

# add label which writes "is equal to"
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1, padx=15)

# add label which will change its value based on the input
end_value_label = Label(text="0")
end_value_label.grid(column=1, row=1)

# add label which says that our end value is represented as km
km_label = Label(text="Km")
km_label.grid(column=2, row=1, padx=15)

# add button which will be used to execute calculation
calculate_button = Button(text="calculate", command=convert_miles_to_km)
calculate_button.grid(column=1, row=2, pady=10)

window.mainloop()
