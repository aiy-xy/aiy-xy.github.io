import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Big Bang")

# Function to generate random shapes
def generate_random_shape():
    shape_type = random.choice(["circle", "blob", "line"])
    color = random.choice(colors)
    size = random.randint(10, 100)
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    return {"type": shape_type, "color": color, "size": size, "x": x, "y": y}

# List to store shapes
shapes = []

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generate a random shape and add it to the list
    shapes.append(generate_random_shape())

    # Clear the screen
    screen.fill(black)

    # Draw and move shapes
    for shape in shapes:
        if shape["type"] == "circle":
            pygame.draw.circle(screen, shape["color"], (shape["x"], shape["y"]), shape["size"])
        elif shape["type"] == "blob":
            pygame.draw.rect(screen, shape["color"], (shape["x"], shape["y"], shape["size"], shape["size"]))
        elif shape["type"] == "line":
            pygame.draw.line(screen, shape["color"], (shape["x"], shape["y"]), (shape["x"] + shape["size"], shape["y"] + shape["size"]), 5)
        
        shape["x"] += random.randint(-5, 5)
        shape["y"] += random.randint(-5, 5)

    # Remove shapes that go out of the screen
    shapes = [shape for shape in shapes if 0 <= shape["x"] <= screen_width and 0 <= shape["y"] <= screen_height]

    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
