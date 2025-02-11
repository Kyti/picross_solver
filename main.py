# main.py

import pygame
import constants
from squareshape import SquareShape

# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Picross Solver")

# Set up font for clues and text
font = pygame.font.SysFont("Arial", constants.FONT_SIZE)

# Function to collect grid size from the user
def get_grid_size():
    # Prompt user for grid size (columns and rows)
    print("Enter the grid width (number of columns):")
    while True:
        try:
            width = int(input())
            if width > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    print("Enter the grid height (number of rows):")
    while True:
        try:
            height = int(input())
            if height > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    return width, height

# Get grid size from user
grid_width, grid_height = get_grid_size()

# Create grid squares based on user input
grid_squares = []
clue_squares = []

# Create main grid squares
for i in range(grid_height):
    row = []
    for j in range(grid_width):
        x = j * constants.SQUARE_SIZE
        y = i * constants.SQUARE_SIZE
        square = SquareShape(x, y, constants.SQUARE_SIZE)
        row.append(square)
    grid_squares.append(row)

# Create clue squares (for example, for now we leave them empty)
# Adjust this part later to dynamically generate clues if necessary
for i in range(grid_height):
    x = grid_width * constants.SQUARE_SIZE
    y = i * constants.SQUARE_SIZE
    clue_square = SquareShape(x, y, constants.SQUARE_SIZE, is_clue=True)
    clue_squares.append(clue_square)

# Game loop
running = True
while running:
    screen.fill(constants.BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the grid squares
    for row in grid_squares:
        for square in row:
            square.draw(screen, font)

    # Draw the clue squares
    for clue_square in clue_squares:
        clue_square.draw(screen, font)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
