import pygame


from base_tank import Tank
from settings import player_tank_image


class PlayerTank(Tank):

    def __init__(self, x: int, y: int, speed: int) -> None:
        super().__init__(x, y, speed)
        self.original_image = self.load_image()
        self.direction = 'UP'
        self.hitbox = (self.x - 1, self.y - 1, self.WIDTH + 2, self.HEIGHT + 2)

    def load_image(self):
        return pygame.image.load(player_tank_image)
    
    def move(self, keys) -> None:
        if keys[pygame.K_UP]:
            self.y -= self.speed
            self.direction = 'UP'
        elif keys[pygame.K_DOWN]:
            self.y += self.speed
            self.direction = 'DOWN'
        elif keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.direction = 'LEFT'
        elif keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.direction = 'RIGHT'

        self.rect.topleft = (self.x, self.y)

    def rotate(self) -> None:
        if self.direction == 'UP':
            self.image = pygame.transform.rotate(self.original_image, 0)
        elif self.direction == 'DOWN':
            self.image = pygame.transform.rotate(self.original_image, 180)
        elif self.direction == 'LEFT':
            self.image = pygame.transform.rotate(self.original_image, 90)
        elif self.direction == 'RIGHT':
            self.image = pygame.transform.rotate(self.original_image, 270)

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

    def draw(self, screen) -> None:
        # Hitbox is declared here additionally, so it sticks with the object
        self.hitbox = (self.x - 1, self.y - 1, 52, 52)
        pygame.draw.rect(screen, (0, 0, 255), self.hitbox, 2)

        if self.x <= 0:
            self.x = 0
        if self.y <= 0:
            self.y = 0
        if self.x >= 750:
            self.x = 750
        if self.y >= 550:
            self.y = 550
        
        screen.blit(self.image, (self.x, self.y))
