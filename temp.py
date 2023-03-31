# import tkinter as tk

# root = tk.Tk()

# # Create a frame with a border
# frame = tk.Frame(root, bd=2, relief=tk.SOLID)
# frame.pack(padx=10, pady=10)

# # Create a label widget and place it inside the frame
# label = tk.Label(frame, text="Hello, World!", font=("Arial", 12))
# label.pack(padx=10, pady=10)

# root.mainloop()
import tkinter as tk

# Create a top level window
toplevel = tk.Toplevel()
toplevel.title("My Application")
toplevel.geometry("800x600")

# Create a frame inside the top level
frame = tk.Frame(toplevel, bg='white', bd=10)
frame.pack(expand=True, fill='both')

# Add a label inside the frame
label = tk.Label(frame, text="Hello, World!", font=("Arial", 24), bg='white', bd=5)
label.pack(expand=True, fill='both')

# Run the event loop
toplevel.mainloop()

