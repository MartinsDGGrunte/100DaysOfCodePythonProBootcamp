import tkinter

# we can create an instance of a window, but it won't show unless we initialise it.
window = tkinter.Tk()

# we can create a title of our window
window.title("Lesson 248 GUI")

# change the color of the window to "white"
window.config()

# we can create the minimum size of our window
window.minsize(width=500, height=300)

# we can add a label to our window, but it won't show unless we add it to our window
label = tkinter.Label(window, text="Lesson 248", font=("Arial", 24, "bold"))
label.pack()

# this is the way how the screen is initialised, and it should be the last line of our program.
window.mainloop()
