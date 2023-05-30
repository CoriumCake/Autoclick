from pynput.mouse import Listener, Button, Controller
import tkinter as tk

x_val = 0
y_val = 0

class MouseListener:
    def __init__(self, root):
        self.listener = None
        self.root = root

    def pick_coords(self):
        self.root.iconify()  # Minimize the window
        self.listener = Listener(on_click=self.on_click)
        self.listener.start()

    def on_click(self, x, y, button, pressed):
        global x_val, y_val
        if pressed:
            print(f"Mouse position: {x}, {y}")
            x_val = x
            y_val = y
            update_label_text()

        else:
            self.listener.stop()
            self.root.deiconify()  # Restore the window
            self.root.lift()  # Bring the window to the front

    def perform_click(self):
        mouse = Controller()
        mouse.position = (x_val, y_val)
        amount = int(amount_entry.get("1.0", tk.END).strip())  # Get the amount of clicks from the Text widget
        for _ in range(amount):
            mouse.click(Button.left)

def update_label_text():
    label.config(text=f"x: {x_val} y: {y_val}")

root = tk.Tk()

root.geometry("600x400")
root.title("auto_click by catcode")

mouse_listener = MouseListener(root)

label = tk.Label(root, text=f"x: {x_val} y: {y_val}")
label.pack(padx=20, pady=20)

amount_entry = tk.Text(root, height=1, width=5, font=('Arial', 16))
amount_entry.pack(padx=10, pady=10)

pick_button = tk.Button(root, text="Pick", font=('Arial', 16), command=mouse_listener.pick_coords)
pick_button.pack()

start_button = tk.Button(root, text="Start", font=('Arial', 16), command=mouse_listener.perform_click)
start_button.pack()

root.mainloop()
