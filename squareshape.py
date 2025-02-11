# squareshape.py

import pygame
from constants import WHITE, BLACK, GREY, FONT_SIZE

class SquareShape:
    def __init__(self, x, y, size, is_clue=False, clue_text=None):
        self.x = x
        self.y = y
        self.size = size
        self.is_clue = is_clue
        self.clue_text = clue_text
        self.rect = pygame.Rect(x, y, size, size)

    def draw(self, screen, font):
        if self.is_clue:
            # Draw the square for the clue (lighter background)
            pygame.draw.rect(screen, GREY, self.rect)
            # Draw the clue text (centered)
            if self.clue_text:
                text = font.render(self.clue_text, True, BLACK)
                screen.blit(text, (self.x + self.size // 4, self.y + self.size // 4))
        else:
            # Draw the regular grid square
            pygame.draw.rect(screen, WHITE, self.rect)
            pygame.draw.rect(screen, BLACK, self.rect, 2)  # Outline for the grid
