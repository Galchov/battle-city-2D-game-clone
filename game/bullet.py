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
        self.collide_with_tank()
        self.collision_with_bullet()

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

    def collide_with_tank(self):
        """Check if the bullet collides with a tank"""

        tank_collisions = pygame.sprite.spritecollide(self, self.tanks, False)
        for tank in tank_collisions:
            if self.owner == tank or tank.spawning:
                continue

            # Friendly fire
            if not self.owner.enemy and not tank.enemy:
                self.update_owner()
                tank.paralyze_tank(gs.TANK_PARALYSIS)
                self.kill()
                break

            # Player bullet collision with AI tank or AI bullet collision with player tank
            if (not self.owner.enemy and tank.enemy) or (self.owner.enemy and not tank.enemy):
                self.update_owner()
                tank.destroy_tank()
                self.kill()
                break
    
    def collision_with_bullet(self):
        """Check for collision with other bullets and destroy self once detected"""

        bullet_hit = pygame.sprite.spritecollide(self, self.bullet_group, False)
        if len(bullet_hit) == 1:
            return
        for bullet in bullet_hit:
            if bullet == self:
                continue
            bullet.update_owner()
            bullet.kill()
            self.update_owner()
            self.kill()
            break

    def update_owner(self):
        if self.owner.bullet_sum > 0:
            self.owner.bullet_sum -= 1
