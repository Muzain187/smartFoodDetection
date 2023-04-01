import tkinter as tk
import subprocess
import json 
import home

class Keyboard(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        # Launch Onboard keyboard
        subprocess.Popen(["onboard"])

        # Launch Matchbox-keyboard
        # subprocess.Popen(["matchbox-keyboard"])

        # Create Frame to hold the keyboard windows
        self.keyboard_frame = tk.Frame(self.master)
        self.keyboard_frame.pack()

        # Embed Onboard keyboard window
        self.onboard_window = tk.Frame(self.keyboard_frame, width=600, height=200)
        self.onboard_window.pack(side="left", padx=10, pady=10)
        onboard_id = self.onboard_window.winfo_id()
        subprocess.call(["wmctrl", "-i", "-r", str(onboard_id), "-b", "add,above"])
        subprocess.call(["xdotool", "windowsize", str(onboard_id), "600", "200"])
        subprocess.call(["xdotool", "windowmove", str(onboard_id), "0", "0"])

        # Embed Matchbox-keyboard window
        # self.matchbox_window = tk.Frame(self.keyboard_frame, width=600, height=200)
        # self.matchbox_window.pack(side="left", padx=10, pady=10)
        # matchbox_id = self.matchbox_window.winfo_id()
        # subprocess.call(["wmctrl", "-i", "-r", str(matchbox_id), "-b", "add,above"])
        # subprocess.call(["xdotool", "windowsize", str(matchbox_id), "600", "200"])
        # subprocess.call(["xdotool", "windowmove", str(matchbox_id), "620", "0"])

        # Create a label to display the text input
        self.text_label = tk.Label(self.master, text="", font=("Arial", 18))
        self.text_label.pack()

        # Create a button to close the keyboard
        self.close_button = tk.Button(self.master, text="Close Keyboard", command=self.close_keyboard)
        self.close_button.pack()

    def check_id(self):
        # print('ID ;'+ ID_input.get())
        id = ID_input.get()
        if(id == "123"):
            response = {
                "results": 
                    {
                        "id": 1234,
                        "name": "Paradise Hotel",
                        "address": "123 Main St",
                        "phone": "555-1234"
                    }     
            }

            # Write the response to a local file
            with open("Restaurent_data.json", "w") as f:
                json.dump(response, f)
            new_window = tk.Toplevel(root)
            new_window.title("Meat Freshness")
            new_window.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
            new_window.configure(bg='white')
            home.main(new_window)
            # home.meat_screen(root,new_window,tk)

    def close_keyboard(self):
        # pass
        # Close Onboard keyboard
        subprocess.Popen(["pkill", "onboard"])

        # Close Matchbox-keyboard
        # subprocess.Popen(["pkill", "matchbox-keyboard"])

        # Destroy Keyboard Frame
        # self.keyboard_frame.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    label = tk.Label(root, text="Enter your name:")
    label.pack()

    ID_input = tk.Entry(root,width=30,font=('Arial', 14), bd=5, relief='groove',borderwidth=0)
    # ID_input.config(height=5)
    ID_input.pack(fill=tk.X, padx=40, pady=40)
    print(ID_input)
    app = Keyboard(master=root)

    button1 = tk.Button( root,text="Save", height=2,command=app.check_id)
    button1.place(relx=0.50, rely=0.4, relwidth=0.4, anchor=tk.CENTER) 

    # root.protocol("WM_DELETE_WINDOW", app.close_keyboard)
    app.mainloop()
