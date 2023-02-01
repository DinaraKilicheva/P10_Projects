import tkinter as tk
from .labels import task_name

window = tk.Tk()
window.title("To do application")
width, height = 400, 500
window.geometry(f"{width}x{height}")

if __name__ == "__main__":
    window.mainloop()
