import tkinter as tk
import camera1 as c1
import camera2 as c2
import camera3 as c3

def button_click(button_number):
    print(f"Button {button_number} clicked!")

def on_enter(e):
    e.widget['background'] = '#2980b9'


def on_leave(e):
    e.widget['background'] = '#3498db'

root = tk.Tk()
root.title("Cool Buttons")
root.geometry("700x400")

sidebar = tk.Frame(root, width=230, bg="#2c3e50")
sidebar.pack(fill=tk.Y, side=tk.LEFT)


def create_heading(text):
    return tk.Label(
        root,
        text=text,
        font=("Arial", 16, "bold"),
        pady=10
    )



heading = create_heading("PARKING SLOT CHECKER 🚗")
heading.pack()


label = tk.Label(text="Cameras", font=("Arial", 15),pady=30)
label.pack()


button1 = button = tk.Button(
        root,
        text="Camera 1",
        font=("Arial", 12, "bold"),
        bg="#3498db",
        fg="white",
        padx=15,
        pady=8,
        command=lambda: c1.camera1_clicked("cameras/camera_1.mp4","camera_details/carparkdetails1"),
        activebackground = '#2980b9'
    )
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
button1.pack(side=tk.LEFT, padx=20)

button2 =button = tk.Button(
        root,
        text="Camera 2",
        font=("Arial", 12, "bold"),
        bg="#3498db",
        fg="white",
        padx=15,
        pady=8,
        command=lambda: c2.camera2_Clicked("cameras/camera_2.mp4","camera_details/carparkdetails2"),
        activebackground = '#2980b9'
    )
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
button2.pack(side=tk.LEFT, padx=20)

button3 = button = tk.Button(
        root,
        text="Camera 3",
        font=("Arial", 12, "bold"),
        bg="#3498db",
        fg="white",
        padx=15,
        pady=8,
        command=lambda: c3.camera3_Clicked("cameras/camera_3.mp4","camera_details/carparkdetails3"),
        activebackground = '#2980b9'
    )
button.bind("<Enter>", on_enter)  
button.bind("<Leave>", on_leave)
button3.pack(side=tk.LEFT, padx=20)

root.mainloop()

