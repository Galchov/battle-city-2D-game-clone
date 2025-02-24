import pygame
import random


from settings import enemy_tank_image


class EnemyTank(pygame.sprite.Sprite):
    WIDTH = 50
    HEIGHT = 50

    def __init__(self, x: int, y: int, speed: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = speed

        self.direction = 'DOWN'
        self.original_image = pygame.image.load(enemy_tank_image)
        self.image = pygame.transform.scale(self.original_image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        self.hitbox = (self.x - 1, self.y - 1, self.WIDTH + 2, self.HEIGHT + 2)

    def update(self) -> None:
        directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']

        if self.direction == 'DOWN':
            self.y += self.speed
            if self.y >= 550:
                self.direction = random.choice(directions)
                self.rotate(self.direction)
        elif self.direction == 'UP':
            self.y -= self.speed
            if self.y <= 0:
                self.direction = random.choice(directions)
                self.rotate(self.direction)
        elif self.direction == 'LEFT':
            self.x -= self.speed
            if self.x <= 0:
                self.direction = random.choice(directions)
                self.rotate(self.direction)
        elif self.direction == 'RIGHT':
            self.x += self.speed
            if self.x >= 750:
                self.direction = random.choice(directions)
                self.rotate(self.direction)
        
        self.rect.topleft = (self.x, self.y)


    def rotate(self, direction: str) -> None:
        if direction == 'UP':
            self.image = pygame.transform.rotate(self.original_image, 180)
        elif direction == 'DOWN':
            self.image = pygame.transform.rotate(self.original_image, 0)
        elif direction == 'LEFT':
            self.image = pygame.transform.rotate(self.original_image, 270)
        elif direction == 'RIGHT':
            self.image = pygame.transform.rotate(self.original_image, 90)

        # TODO: This scaling to be refactored, so it becomes more memory efficient
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect(center=self.rect.center)

    def hit_object(self, other_objects):
        hit_obects = pygame.sprite.spritecollide(self, other_objects, False)
        if hit_obects:
            enemy = hit_obects[0]

            # Calculate overlap on each side
            overlap_right = self.rect.right - enemy.rect.left
            overlap_left = enemy.rect.right - self.rect.left
            overlap_down = self.rect.bottom - enemy.rect.top
            overlap_up = enemy.rect.bottom - self.rect.top

            min_overlap = min(overlap_right, overlap_left, overlap_down, overlap_up)

            # Stop movement in the direction of the smallest overlap
            if min_overlap == overlap_right:
                self.x = enemy.x - self.rect.width  # Stop moving right
            elif min_overlap == overlap_left:
                self.x = enemy.x + enemy.rect.width  # Stop moving left
            elif min_overlap == overlap_down:
                self.y = enemy.y - self.rect.height  # Stop moving down
            elif min_overlap == overlap_up:
                self.y = enemy.y + enemy.rect.height  # Stop moving up

            directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
            self.direction = random.choice(directions)
            self.rotate(self.direction)
