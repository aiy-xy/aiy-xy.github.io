import numpy as np
import matplotlib.pyplot as plt

# Explain the game and its purpose to the kids
print("Welcome to the Expanding Universe Game!")
print("In this game, you can change the size and expansion of the universe.")
print("See how different values affect the outcome.")

# Gather user input for constants
num_points = int(input("Enter the number of points (e.g., 1000): "))
radius = float(input("Enter the initial radius of the universe (e.g., 1.0): "))
expansion_factor = float(input("Enter the expansion factor (e.g., 10.0): "))

# Generate data
theta = np.linspace(0, 2 * np.pi, num_points)
radii = np.linspace(0, radius, num_points)
x = radii * np.cos(theta)
y = radii * np.sin(theta)

# Apply expansion factor
x *= expansion_factor
y *= expansion_factor

# Plot the expanding universe
plt.figure(figsize=(8, 8))
plt.plot(x, y, 'b.')
plt.title("Expanding Universe")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis('equal')
plt.show()
