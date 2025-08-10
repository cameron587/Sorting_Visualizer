import tkinter as tk
import random
import time

root = tk.Tk()
root.title("Sorting Visualizer")
root.geometry("800x625")

canvas = tk.Canvas(root, width=900, height=400, bg='white')
canvas.pack(pady=10)

def draw_data(data, color_array):
    canvas.delete("all")
    c_height = 400
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

swaps = 0
speed = tk.DoubleVar()
bar_count = tk.IntVar()
speed.set(100)
bar_count.set(245)

swap_label = None
time_label = None

def labels_and_buttons():
    def labels():
        global swap_label, time_label
        swap_label = tk.Label(root, text="Swaps done: 0 swaps", font=("Arial", 12))
        swap_label.pack(pady=5, anchor="center")

        time_label = tk.Label(root, text="Time taken: 0.000 seconds", font=("Arial", 12))
        time_label.pack(pady=5, anchor="center")

    def slider_frame():
        slider_frame = tk.Frame(root)
        slider_frame.pack(fill='x')

        def sorting_speed():
            tk.Label(slider_frame, text="Sorting Speed (ms delay)").pack(side="left", padx=10)
            tk.Scale(slider_frame, from_=1, to=200, orient=tk.HORIZONTAL, variable=speed).pack(side="left", padx=10)

        def number_of_bars():
            tk.Label(slider_frame, text="Number of Bars").pack(side="right", padx=10)
            tk.Scale(slider_frame, from_=10, to=500, orient=tk.HORIZONTAL, variable=bar_count).pack(side="right", padx=10)

        sorting_speed()
        number_of_bars()
    
    def buttons():
            tk.Button(root, text="Generate Data", command=generate).pack(pady=5, anchor="center")
            tk.Button(root, text="Start Sorting", command=lambda: bubble_sort_step()).pack(pady=5, anchor="center")

    labels()
    slider_frame()
    buttons()

def generate():
    global data
    data = [random.randint(1, 100) for _ in range(bar_count.get())]
    draw_data(data, ["skyblue" for _ in range(len(data))])

start_time = None
data = []

def bubble_sort_step(i=0, j=0):
    global data, start_time, swaps
    n = len(data)

    if i == 0 and j == 0:
        start_time = time.time()
        swaps = 0
        swap_label.config(text="Swaps done: 0 swaps")

    if i < n:
        if j < n - i - 1:
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swaps += 1
                swap_label.config(text=f"Swaps done: {swaps} swaps")

            draw_data(data, ["red" if x == j or x == j + 1 else "skyblue" for x in range(len(data))])
            root.after(int(speed.get()), lambda: bubble_sort_step(i, j + 1))
        else:
            root.after(int(speed.get()), lambda: bubble_sort_step(i + 1, 0))
    else:
        elapsed_time = time.time() - start_time
        time_label.config(text=f"Time taken: {elapsed_time:.3f} seconds")
        draw_data(data, ["green" for _ in range(len(data))])

labels_and_buttons()
root.mainloop()
