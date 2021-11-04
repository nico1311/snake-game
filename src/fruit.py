import glob
import pygame
import random

class Fruit:
  def __init__(self, screen: pygame.Surface):
    self.screen = screen
    self.block_size = 24
    self.image = pygame.Surface((self.block_size, self.block_size))
    self.x = 0
    self.y = 0

  def generate_new_fruit(self):
    image_path = random.choice(glob.glob('resources/fruits/*.png'))
    self.image = pygame.transform.smoothscale(pygame.image.load(image_path), (self.block_size, self.block_size))
    self.x = random.randint(0, self.screen.get_width() - self.block_size * 3)
    self.y = random.randint(0, self.screen.get_height() - self.block_size * 3)

  def draw(self):
    self.screen.blit(self.image, (self.x, self.y))
    pygame.display.update()
