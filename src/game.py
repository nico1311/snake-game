import pygame
import time

from snake import Snake


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.screen.fill((255, 255, 255))
        self.snake = Snake(self.screen)
        self.snake.draw()

    def run(self):
        pygame.display.set_caption("Snake")
        running = True
        while running:
            for event in pygame.event.get():
                # Quit if the window is closed
                if event.type == pygame.QUIT:
                    running = False
                # Quit if the user presses escape key
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    # Move block up if the up arrow key is pressed
                    if event.key == pygame.K_UP:
                        self.snake.move("up")
                    # Move block down if the down arrow key is pressed
                    if event.key == pygame.K_DOWN:
                        self.snake.move("down")
                    # Move block left if the left arrow key is pressed
                    if event.key == pygame.K_LEFT:
                        self.snake.move("left")
                    # Move block right if the right arrow key is pressed
                    if event.key == pygame.K_RIGHT:
                        self.snake.move("right")
            self.snake.walk()
            time.sleep(0.2)
