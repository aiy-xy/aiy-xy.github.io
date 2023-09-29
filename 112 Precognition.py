import tkinter as tk
import random

# Define the dimensions of your letter/number grid
grid_width = 10
grid_height = 10

# Define the possible colors for the cells, including black
colors = ["red", "green", "blue", "yellow", "purple", "orange", "black"]

# Create a tkinter window
root = tk.Tk()
root.title("Precognition Game")

# Function to randomly select a cell and color
def select_random_cell():
    x = random.randint(0, grid_width - 1)
    y = random.randint(0, grid_height - 1)
    color = random.choice(colors)
    return x, y, color

# Function to reveal and keep the color on the screen
def reveal_color():
    x, y, color = select_random_cell()
    canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill=color, outline=color)
    revealed_colors.append((x, y, color))
    root.after(2000, reveal_color)  # Schedule the next color reveal

# Create a canvas for drawing
canvas = tk.Canvas(root, width=grid_width * 20, height=grid_height * 20, bg="black")
canvas.pack()

# List to keep track of revealed colors
revealed_colors = []

# Start revealing colors endlessly
reveal_color()

# Run the tkinter main loop
root.mainloop()
