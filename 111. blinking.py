import tkinter as tk
import random
import time

# Define the dimensions of your pixel grid
grid_width = 10
grid_height = 10

# Define the possible colors for the pixels
colors = ["red", "green", "blue", "yellow", "purple", "orange"]

# Create a tkinter window
root = tk.Tk()
root.title("Flashing Multicolour Dots")  # Set the window title
canvas = tk.Canvas(root, width=grid_width * 20, height=grid_height * 20, bg="black")  # Set the background color to black
canvas.pack()

# Function to randomly turn on a pixel
def turn_on_random_pixel():
    x = random.randint(0, grid_width - 1)
    y = random.randint(0, grid_height - 1)
    color = random.choice(colors)
    radius = 10  # Adjust the radius as needed
    canvas.create_oval(x * 20 - radius, y * 20 - radius, x * 20 + radius, y * 20 + radius, fill=color, outline=color)

# Function to clear the grid
def clear_grid():
    canvas.delete("all")

# Function to simulate flashing pixels
def simulate_flashing_pixels():
    while True:
        turn_on_random_pixel()
        root.update()
        time.sleep(3)
        clear_grid()
        root.update()
        time.sleep(0.3)

# Start the simulation
simulate_flashing_pixels()

# Run the tkinter main loop
root.mainloop()
