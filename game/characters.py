import pygame
import settings as gs


class Tank(pygame.sprite.Sprite):
    
    def __init__(self, game, assets, groups, position, direction, color="Silver", tank_level=0) -> None:
        super().__init__()
        # Game objects and assets
        self.game = game
        self.assets = assets
        self.groups = groups

        # Sprite groups that may interact with self
        self.tank_group = self.groups["All_Tanks"]

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

        # Tank image, rectangle and frame index
        self.frame_index = 0
        self.image = self.tank_images[f"Tank_{self.tank_level}"][self.color][self.direction][self.frame_index]
        self.rect = self.image.get_rect(topleft=(self.spawn_pos))

        # Spawn images
        self.spawn_image = self.spawn_images[f"star_{self.frame_index}"]
        self.spawn_timer = pygame.time.get_ticks()
        self.spawn_animation_timer = pygame.time.get_ticks()

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

    def draw(self, window) -> None:
        # If tank is spawning, draw the spawn star
        if self.spawning:
            window.blit(self.spawn_image, self.rect)

        # If the tank is set to active, draw it on the screen
        if self.active:
            window.blit(self.image, self.rect)
            pygame.draw.rect(window, gs.RED, self.rect, 1)

    def move_tank(self, direction) -> None:
        """Moves the tank in the given direction"""
        if self.spawning:
            return

        self.direction = direction

        if direction == "Up":
            self.y_pos -= self.tank_speed
        elif direction == "Down":
            self.y_pos += self.tank_speed
        elif direction == "Left":
            self.x_pos -= self.tank_speed
        elif direction == "Right":
            self.x_pos += self.tank_speed

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
    
    def spawn_animation(self) -> None:
        """Cycle through the spawning star images to simulate a spawning effect"""

        self.frame_index += 1
        self.frame_index = self.frame_index % len(self.spawn_images)
        self.spawn_image = self.spawn_images[f"star_{self.frame_index}"]
        self.spawn_animation_timer = pygame.time.get_ticks()
    
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
            