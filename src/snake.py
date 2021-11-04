import pygame

class Snake:
  def __init__(self, screen: pygame.Surface):
    self.screen = screen
    self.block_size = 24
    self.movement_size = 24
    self.length = 3
    self.x = [self.block_size] * self.length
    self.y = [self.block_size] * self.length

    self.current_direction = "right"
    self.block = pygame.transform.scale(pygame.image.load("resources/blocks/Blocks_01_64x64_Alt_00_005.png"), (self.block_size, self.block_size))

  def draw(self):
    self.screen.fill((255, 255, 255))
    # Draw all blocks
    for i in range(self.length):
      self.screen.blit(self.block, (self.x[i], self.y[i]))
    pygame.display.update()

  def grow(self):
    self.length += 1
    self.x.append(-1)
    self.y.append(-1)

  def move(self, direction: str):
    self.current_direction = direction

  def walk(self):
    # Iterate through all blocks in descending order
    for i in range(self.length-1, 0, -1):
      # Set the position of the block to the position of the block behind it
      self.x[i] = self.x[i-1]
      self.y[i] = self.y[i-1]
    # Move the first block
    if self.current_direction == "up":
      self.y[0] -= self.movement_size
    elif self.current_direction == "down":
      self.y[0] += self.movement_size
    elif self.current_direction == "left":
      self.x[0] -= self.movement_size
    elif self.current_direction == "right":
      self.x[0] += self.movement_size
    self.draw()
