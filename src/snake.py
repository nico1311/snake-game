import pygame

class Snake:
  def __init__(self, screen: pygame.Surface):
    self.screen = screen
    self.block_size = 24
    self.movement_size = 10
    self.x = 100
    self.y = 100
    self.current_direction = "right"
    self.block = pygame.transform.scale(pygame.image.load("resources/blocks/Blocks_01_64x64_Alt_00_005.png"), (self.block_size, self.block_size))

  def draw(self):
    self.screen.fill((255, 255, 255))
    self.screen.blit(self.block, (self.x, self.y))
    pygame.display.update()

  def move(self, direction: str):
    self.current_direction = direction

  def walk(self):
    if self.current_direction == "up":
      self.y -= self.movement_size
    elif self.current_direction == "down":
      self.y += self.movement_size
    elif self.current_direction == "left":
      self.x -= self.movement_size
    elif self.current_direction == "right":
      self.x += self.movement_size
    self.draw()
