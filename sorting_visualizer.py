import tkinter as tk
import random

root = tk.Tk()
root.title("Sorting Visualizer")
root.geometry("800x550")

canvas = tk.Canvas(root, width=900, height=400, bg='white')
canvas.pack(pady=10)

def draw_data(data, color_array):
    canvas.delete("all")
    c_height = 450
    c_width = 800
    bar_width = c_width / len(data)
    spacing = 0
    max_val = max(data)

    for i, val in enumerate(data):
        x0 = i * bar_width
        y0 = c_height - (val / max_val * 300)
        x1 = (i + 1) * bar_width - spacing
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])

speed = tk.DoubleVar()
bar_count = tk.IntVar()
speed.set(100)
bar_count.set(145)

slider_frame = tk.Frame(root)
slider_frame.pack(pady=10, fill='x')

speed_Label = tk.Label(root, text="Sorting Speed (ms delay)")
speed_Label.pack(side="left", padx=10)
speed_slider = tk.Scale(root, from_=1, to=200, orient=tk.HORIZONTAL, variable=speed)
speed_slider.pack(side="left", padx=10)

bar_Label = tk.Label(root, text="Number of Bars")
bar_Label.pack(side="right", padx=10)
bar_slider = tk.Scale(root, from_=10, to=300, orient=tk.HORIZONTAL, variable=bar_count)
bar_slider.pack(side="right", padx=10)

def generate():
    global data
    data = [random.randint(1, 100) for _ in range(bar_count.get())]
    draw_data(data, ["skyblue" for _ in range(len(data))])

btn = tk.Button(root, text="Generate Data", command=generate)
btn.pack(pady=10)

sort_btn = tk.Button(root, text="Start Bubble Sort", command=lambda: bubble_sort(data))
sort_btn.pack(pady=5)

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                #swap values
                data[j], data[j + 1] = data[j + 1], data[j]
                #draw after each swap
                draw_data(data, ["red" if x == j or x == j + 1 else "skyblue" for x in range(len(data))])
                root.update_idletasks()
                root.after(int(speed.get()))

data = []
root.mainloop()