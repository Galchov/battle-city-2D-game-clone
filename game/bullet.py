import pygame
import settings as gs


class Bullet(pygame.sprite.Sprite):

    def __init__(self, groups, assets, owner, position, direction):
        super().__init__()
        self.group = groups
        self.assets = assets

        # Groups for collision detection
        self.tanks = self.group["All_Tanks"]
        self.bullet_group = self.group["Bullets"]

        # Bullet position and direction
        self.x_pos, self.y_pos = position
        self.direction = direction

        # Bullet attributes
        self.owner = owner

        # Bullet image
        self.images = self.assets.bullet_images
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

        # Add bullet to the bullets group
        self.bullet_group.add(self)

    def update(self):
        self.move()
        self.collide_edge_of_screen()

    def draw(self, window):
        window.blit(self.image, self.rect)
        pygame.draw.rect(window, gs.GREEN, self.rect, 1)
        
    def move(self):
        """Move the bullet in the direction indicated at the init method"""

        speed = gs.TANK_SPEED * 3
        if self.direction == "Up":
            self.y_pos -= speed
        elif self.direction == "Down":
            self.y_pos += speed
        elif self.direction == "Left":
            self.x_pos -= speed
        elif self.direction == "Right":
            self.x_pos += speed
        
        self.rect.center = (self.x_pos, self.y_pos)
    
    # Collisions
    def collide_edge_of_screen(self):
        """Check for collisions with screen edge"""

        if self.rect.top <= gs.SCREEN_BORDER_TOP or \
            self.rect.bottom >= gs.SCREEN_BORDER_BOTTOM or \
            self.rect.left <= gs.SCREEN_BORDER_LEFT or \
            self.rect.right >= gs.SCREEN_BORDER_RIGHT:
            self.update_owner()
            self.kill()

    def update_owner(self):
        if self.owner.bullet_sum > 0:
            self.owner.bullet_sum -= 1
