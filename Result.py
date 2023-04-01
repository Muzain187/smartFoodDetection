import tkinter as tk

import meat






    





def main(root):

    # Add a label with a message
    label = tk.Label(root, text="Tigertech Food Detection",bg="white",font=("bold",25))
    label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    line = tk.Frame(root, height=1, bg='black')
    line.pack(fill=tk.X,pady=100)

    

    
    root.mainloop()


if __name__ == "__main__":
    # Create a root window
    root = tk.Tk()

    # Set the window title
    root.title("My Application")


    # Set the window size to a mobile size
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))


    # Set the background color of the window
    root.configure(bg='white')
    main(root)

# Run the event loop


