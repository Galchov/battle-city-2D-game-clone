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

        # Tank position and direction
        self.spawn_pos = position
        self.x_pos, self.y_pos = self.spawn_pos
        self.direction = direction

        # Common tanks attributes
        self.active = True
        self.tank_level = tank_level
        self.color = color

        # Tank image, rectangle and frame index
        self.frame_index = 0
        self.image = self.tank_images[f"Tank_{self.tank_level}"][self.color][self.direction][self.frame_index]
        self.rect = self.image.get_rect(topleft=(self.spawn_pos))

    def input(self) -> None:
        pass

    def update(self) -> None:
        pass

    def draw(self, window) -> None:
        # If the tank is set to active, draw it on the screen
        if self.active:
            window.blit(self.image, self.rect)
