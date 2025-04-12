import pygame
import settings as gs

from bullet import Bullet


class Tank(pygame.sprite.Sprite):
    
    def __init__(self, game, assets, groups, position, direction, enemy=True, color="Silver", tank_level=0) -> None:
        super().__init__()
        # Game objects and assets
        self.game = game
        self.assets = assets
        self.groups = groups

        # Sprite groups that may interact with self
        self.tank_group = self.groups["All_Tanks"]
        self.player_group = self.groups["Player_Tanks"]

        # Add tank object to sprite group
        self.tank_group.add(self)

        # Tank images
        self.tank_images = self.assets.tank_images
        self.spawn_images = self.assets.spawn_star_images

        # Tank position and direction
        self.spawn_pos = position
        self.x_pos, self.y_pos = self.spawn_pos
        self.direction = direction

        # Tank spawning / Active
        self.spawning = True
        self.active = False

        # Common tanks attributes
        self.tank_level = tank_level
        self.color = color
        self.tank_speed = gs.TANK_SPEED
        self.enemy = enemy
        self.tank_health = 1

        # Tank image, rectangle and frame index
        self.frame_index = 0
        self.image = self.tank_images[f"Tank_{self.tank_level}"][self.color][self.direction][self.frame_index]
        self.rect = self.image.get_rect(topleft=(self.spawn_pos))
        self.width, self.height = self.image.get_size()

        # Shoot cooldown and bullet limit
        self.bullet_limit = 1
        self.bullet_sum = 0

        # Tank paralysis
        self.paralyzed = False
        self.paralysis = gs.TANK_PARALYSIS
        self.paralysis_timer = pygame.time.get_ticks()

        # Spawn images
        self.spawn_image = self.spawn_images[f"star_{self.frame_index}"]
        self.spawn_timer = pygame.time.get_ticks()
        self.spawn_animation_timer = pygame.time.get_ticks()

        # Tank image mask dictionary
        self.mask_dict = self.get_various_masks()
        self.mask = self.mask_dict[self.direction]
        # self.mask_image = self.mask.to_surface()
        self.mask_direction = self.direction

    def input(self) -> None:
        pass

    def update(self) -> None:
        # Update the spawning animation
        if self.spawning:

            # Update the spawning animation if the required amount of time has passed
            if pygame.time.get_ticks() - self.spawn_animation_timer >= 50:
                self.spawn_animation()
            if pygame.time.get_ticks() - self.spawn_timer > 2000:
                self.frame_index = 0
                self.spawning = False
                self.active = True
            
            return

        if self.paralyzed:
            if pygame.time.get_ticks() - self.paralysis_timer >= self.paralysis:
                self.paralyzed = False

    def draw(self, window) -> None:
        # If tank is spawning, draw the spawn star
        if self.spawning:
            window.blit(self.spawn_image, self.rect)

        # If the tank is set to active, draw it on the screen
        if self.active:
            window.blit(self.image, self.rect)
            # window.blit(self.mask_image, self.rect)
            pygame.draw.rect(window, gs.RED, self.rect, 1)

    def move_tank(self, direction) -> None:
        """Moves the tank in the given direction"""
        if self.spawning:
            return

        self.direction = direction

        if self.paralyzed:
            self.image = self.tank_images[f"Tank_{self.tank_level}"][self.color][self.direction][self.frame_index]
            return

        if direction == "Up":
            self.y_pos -= self.tank_speed
            if self.y_pos < gs.SCREEN_BORDER_TOP:
                self.y_pos = gs.SCREEN_BORDER_TOP
        elif direction == "Down":
            self.y_pos += self.tank_speed
            if self.y_pos + self.height > gs.SCREEN_BORDER_BOTTOM:
                self.y_pos = gs.SCREEN_BORDER_BOTTOM - self.height
        elif direction == "Left":
            self.x_pos -= self.tank_speed
            if self.x_pos < gs.SCREEN_BORDER_LEFT:
                self.x_pos = gs.SCREEN_BORDER_LEFT
        elif direction == "Right":
            self.x_pos += self.tank_speed
            if self.x_pos + self.width > gs.SCREEN_BORDER_RIGHT:
                self.x_pos = gs.SCREEN_BORDER_RIGHT - self.width

        # Update the tank rectangle position
        self.rect.topleft = (self.x_pos, self.y_pos)

        # Update the tank animanion
        self.tank_movement_animation()

        # Detect tank collision with other tanks
        self.tank_to_tank_collisions()

    ##### Tank animations #####
    def tank_movement_animation(self) -> None:
        """Updates the animation images while the tank is moving"""

        self.frame_index += 1
        image_list_length = len(self.tank_images[f"Tank_{self.tank_level}"][self.color][self.direction])
        self.frame_index = self.frame_index % image_list_length
        self.image = self.tank_images[f"Tank_{self.tank_level}"][self.color][self.direction][self.frame_index]
        if self.mask_direction != self.direction:
            self.mask_direction = self.direction
            self.mask = self.mask_dict[self.mask_direction]
            self.mask_image = self.mask.to_surface()

    def spawn_animation(self) -> None:
        """Cycle through the spawning star images to simulate a spawning effect"""

        self.frame_index += 1
        self.frame_index = self.frame_index % len(self.spawn_images)
        self.spawn_image = self.spawn_images[f"star_{self.frame_index}"]
        self.spawn_animation_timer = pygame.time.get_ticks()

    def get_various_masks(self):
        """Creates and returns a dictionary of masks for all directions"""

        images = {}
        directions = ["Up", "Down", "Left", "Right"]
        for direction in directions:
            image_to_mask = self.tank_images[f"Tank_{self.tank_level}"][self.color][direction][0]
            images.setdefault(direction, pygame.mask.from_surface(image_to_mask))
        
        return images
    
    ##### Tank collisions #####
    def tank_to_tank_collisions(self):
        """Checks if tank collides with another tank"""

        tank_collision = pygame.sprite.spritecollide(self, self.tank_group, False)
        if len(tank_collision) == 1:
            return
        
        for tank in tank_collision:
            # Skip the current tank
            if tank == self:
                continue

            if self.direction == "Right":
                if self.rect.right >= tank.rect.left and \
                    self.rect.bottom > tank.rect.top and self.rect.top < tank.rect.bottom:
                    self.rect.right = tank.rect.left
                    self.x_pos = self.rect.x
            elif self.direction == "Left":
                if self.rect.left <= tank.rect.right and \
                    self.rect.bottom > tank.rect.top and self.rect.top < tank.rect.bottom:
                    self.rect.left = tank.rect.right
                    self.x_pos = self.rect.x
            elif self.direction == "Up":
                if self.rect.top <= tank.rect.bottom and \
                    self.rect.left < tank.rect.right and self.rect.right > tank.rect.left:
                    self.rect.top = tank.rect.bottom
                    self.y_pos = self.rect.y
            elif self.direction == "Down":
                if self.rect.bottom >= tank.rect.top and \
                    self.rect.left < tank.rect.right and self.rect.right > tank.rect.left:
                    self.rect.bottom = tank.rect.top
                    self.y_pos = self.rect.y
            
    ##### Tank shooting #####
    def shoot(self):
        if self.bullet_sum >= self.bullet_limit:
            return
        
        bullet = Bullet(self.groups, self.assets, self, self.rect.center, self.direction)
        self.bullet_sum += 1

    ##### Actions affecting tanks #####
    def paralyze_tank(self, paralysis_time):
        """If the player tank gets hit by other player tank, 
        or if the freeze power up is used"""

        self.paralysis = paralysis_time
        self.paralyzed = True
        self.paralysis_timer = pygame.time.get_ticks()

    def destroy_tank(self):
        """Damage the tank and reduce its health. 
        If health goes to 0, destroy the tank"""
        
        self.tank_health -= 1

        if self.tank_health <= 0:
            self.kill()
            return
