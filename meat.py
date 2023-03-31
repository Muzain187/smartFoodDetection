sensor_result = 1.0
import threading
import time



def read_sensor():
    global sensor_result
    while True:
        # read the sensor value
        sensor_result += 6.5
        if sensor_result >= 40:
            break
        time.sleep(1) 





def meat_screen(root,new_window,tk):
    new_window.title("Meat Freshness")

    
    new_window.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    new_window.configure(bg='white')

    DisplayFrame = tk.Frame(new_window, bg='white',bd=2, relief=tk.SOLID, width=200, height=50)
    DisplayFrame.pack(expand=True, fill=tk.BOTH, padx=50, pady=50)

    label = tk.Label(DisplayFrame, text="Processing", font=("Arial", 20), bg='white')
    label.place(relx=0.5, rely=0.1, anchor=tk.CENTER,relwidth=0.5)

    global sensor_result
    label2 = tk.Label(DisplayFrame, text="Sensor Result: {}".format(sensor_result), font=("Arial", 20), bg='white')
    label2.place(relx=0.5, rely=0.2, anchor=tk.CENTER,relwidth=0.5)


    

    sensor_thread = threading.Thread(target=read_sensor, daemon=True)
    sensor_thread.start()



    buttonFrame = tk.Frame(new_window, bg='white',relief=tk.SOLID, width=200, height=100)
    buttonFrame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    button1 = tk.Button(buttonFrame, text="Save", height=2,command=meat_screen)
    button1.place(relx=0.50, rely=0.4, relwidth=0.4, anchor=tk.CENTER)


    # root.after(1000, update_display)
    def update_label():
        label2.config(text=f'PH Sensor Value: {sensor_result:.2f}')

        if sensor_result >= 40:
            Result = tk.Label(DisplayFrame, text="Finished", font=("Arial", 20), bg='white')
            Result.place(relx=0.5, rely=0.4, anchor=tk.CENTER,relwidth=0.5)
            return
        
        root.after(1000, update_label)

    update_label()
    # meat_screen(root,new_window,tk)
    

