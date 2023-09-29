import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Photon Spiral")

# Function to generate a random photon line
def generate_photon():
    color = random.choice(colors)
    x = screen_width // 2
    y = screen_height // 2
    angle = random.uniform(0, 2 * math.pi)
    speed = random.uniform(1, 5)
    return {"color": color, "x": x, "y": y, "angle": angle, "speed": speed}

# List to store photons
photons = []

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generate a random photon and add it to the list
    photons.append(generate_photon())

    # Clear the screen
    screen.fill(black)

    # Draw and move photons
    for photon in photons:
        pygame.draw.line(screen, photon["color"], (photon["x"], photon["y"]), (photon["x"] + 5, photon["y"]), 2)
        
        # Update photon position
        photon["x"] += photon["speed"] * math.cos(photon["angle"])
        photon["y"] += photon["speed"] * math.sin(photon["angle"])

    # Remove photons that go out of the screen
    photons = [photon for photon in photons if 0 <= photon["x"] <= screen_width and 0 <= photon["y"] <= screen_height]

    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
