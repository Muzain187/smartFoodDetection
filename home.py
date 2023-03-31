import tkinter as tk

import meat



def meat_screen():
    new_window = tk.Toplevel(root)
    meat.meat_screen(root,new_window,tk)


    
# Add four buttons
def Home_buttons():
    button1 = tk.Button(root, text="Meat", height=2,command=meat_screen)
    button1.place(relx=0.25, rely=0.4, relwidth=0.4, anchor=tk.CENTER)

    button2 = tk.Button(root, text="Button 2", height=2)
    button2.place(relx=0.75, rely=0.4, relwidth=0.4, anchor=tk.CENTER)

    button3 = tk.Button(root, text="Button 3", height=2)
    button3.place(relx=0.25, rely=0.6, relwidth=0.4, anchor=tk.CENTER)

    button4 = tk.Button(root, text="Button 4", height=2)
    button4.place(relx=0.75, rely=0.6, relwidth=0.4, anchor=tk.CENTER)



if __name__ == "__main__":
    # Create a root window
    root = tk.Tk()

    # Set the window title
    root.title("My Application")


    # Set the window size to a mobile size
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))


    # Set the background color of the window
    root.configure(bg='white')

    # Add a label with a message
    label = tk.Label(root, text="Smart Food Detection",bg="white",font=("bold",25))
    label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    Home_buttons()
    
    root.mainloop()


# Run the event loop


