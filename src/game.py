import pygame
import time

from snake import Snake
from fruit import Fruit

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((720, 480))
        self.screen.fill((255, 255, 255))
        self.block_size = 24
        self.snake = Snake(self.screen)
        self.fruit = Fruit(self.screen)
        self.clock = pygame.time.Clock()
        self.running = False

    def detect_collision(self, x1: int, y1: int, x2: int, y2: int):
        if x1 < x2 + self.block_size and x1 + self.block_size > x2 and y1 < y2 + self.block_size and self.block_size + y1 > y2:
            return True
        return False

    def display_score(self):
        font = pygame.font.SysFont("arial", 24)
        text = font.render("Puntos: " + str(self.snake.length - 3), True, (0, 0, 0))
        self.screen.blit(text, (580, 20))

    def game_over_screen(self):
        self.screen.fill((255, 255, 255))
        font = pygame.font.SysFont("arial", 30)
        line1 = font.render("Game Over!", True, (0, 0, 0))
        line2 = font.render("Puntos: " + str(self.snake.length - 3), True, (0, 0, 0))
        line3 = font.render("Enter para volver a jugar", True, (0, 0, 0))
        self.screen.blit(line1, (100, 100))
        self.screen.blit(line2, (100, 140))
        self.screen.blit(line3, (100, 200))
        pygame.display.update()

    def reset_game_state(self):
        self.snake = Snake(self.screen)
        self.fruit.generate_new_fruit()

    def main_loop(self):
        self.snake.walk()
        self.display_score()
        self.fruit.draw()
        pygame.display.update()

        # Grow snake if collision with fruit
        if self.detect_collision(self.snake.x[0], self.snake.y[0], self.fruit.x, self.fruit.y):
            self.fruit.generate_new_fruit()
            self.snake.grow()

        # Check if snake has collided with itself
        for i in range(3, self.snake.length):
            if self.detect_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise ValueError("Game over")

        # Check if snake head has collided with the wall
        if self.snake.x[0] < 0 or self.snake.x[0] > self.screen.get_width() - self.block_size or self.snake.y[0] < 0 or self.snake.y[0] > self.screen.get_height() - self.block_size:
            raise ValueError("Game over")

    def run(self):
        pygame.display.set_caption("Snake")
        game_running = True
        self.fruit.generate_new_fruit()
        self.running = True
        while self.running:
            # Delay time based on current score
            pygame.time.delay(200 - (self.snake.length - 3) * 5)
            self.clock.tick(10)
            for event in pygame.event.get():
                # Quit if the window is closed
                if event.type == pygame.QUIT:
                    self.running = False
                # Quit if the user presses escape key
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                if game_running:
                    if event.type == pygame.KEYDOWN:
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
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            game_running = True
            try:
                if game_running:
                    self.main_loop()
            except ValueError:
                game_running = False
                self.game_over_screen()
                self.reset_game_state()
                    