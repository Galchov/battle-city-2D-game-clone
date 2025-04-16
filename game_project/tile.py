import pygame
import settings as gs


class TileType(pygame.sprite.Sprite):
    def __init__(self, position, group, map_tile):
        super().__init__(group)
        self.group = group
        self.images = map_tile
        self.x_pos = position[0]
        self.y_pos = position[1]

    def update(self):
        pass

    def _get_rect_and_size(self, position):
        self.rect = self.image.get_rect(topleft=position)
        self.width, self.height = self.image.get_size()

    def draw(self, window):
        window.blit(self.image, self.rect)


class BrickTile(TileType):
    def __init__(self, position, group, map_tile):
        super().__init__(position, group, map_tile)
        self.health = 2
        self.name = "Brick"

        self.image = self.images["small"]
        self._get_rect_and_size((self.x_pos, self.y_pos))
