import pygame

import settings as gs
from levels import LevelData


class LevelEditor:

    def __init__(self, main, assets):
        self.main = main
        self.assets = assets
        self.active = True

        self.level_data = LevelData()
        self.all_levels = []
        for stage in self.level_data.level_data:
            self.all_levels.append(stage)

        self.overlay_screen = self.draw_screen()
        self.matrix = self.generate_level_matrix()

        self.tile_type = {
            432: self.assets.brick_tiles["small"],
            482: self.assets.steel_tiles["small"],
            483: self.assets.forest_tiles["small"],
            484: self.assets.ice_tiles["small"],
            533: self.assets.water_tiles["small_1"],
            999: self.assets.flag["Phoenix_Alive"],
        }

        self.inserts = [
            # Empty square
            [-1, -1, -1, -1],

            # Brick tiles
            [-1, 432, -1, 432],     # Right vertical brick
            [-1, -1, 432, 432],     # Bottom row brick
            [432, -1, 432, -1],     # Left vertical brick
            [432, 432, -1, -1],     # Top row brick
            [432, 432, 432, 432],   # Full brick

            # Steel tiles
            [-1, 482, -1, 482],     # Steel tile right vertical
            [-1, -1, 482, 482],     # Steel tile bottom row
            [482, -1, 482, -1],     # Steel tile left vertical
            [482, 482, -1, -1],     # Steel tile top row
            [482, 482, 482, 482],   # Steel tile full

            # Other tiles - Full blocks
            [483, 483, 483, 483],   # Forest tile
            [484, 484, 484, 484],   # Ice tile
            [533, 533, 533, 533],   # Water tile
        ]

        self.index = 0
        self.insert_tile = self.inserts[self.index]
        
        self.icon_image = self.assets.tank_images["Tank_4"]["Gold"]["Up"][0]
        self.icon_rect = self.icon_image.get_rect(topleft=(gs.SCREEN_BORDER_LEFT, gs.SCREEN_BORDER_TOP))

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.main.run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.main.run = False
                # Moving right
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.icon_rect.x += gs.IMAGE_SIZE
                    if self.icon_rect.x >= gs.SCREEN_BORDER_RIGHT:
                        self.icon_rect.x = gs.SCREEN_BORDER_RIGHT - gs.IMAGE_SIZE
                # Moving left
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.icon_rect.x -= gs.IMAGE_SIZE
                    if self.icon_rect.x <= gs.SCREEN_BORDER_LEFT:
                        self.icon_rect.x = gs.SCREEN_BORDER_LEFT
                # Moving up
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.icon_rect.y -= gs.IMAGE_SIZE
                    if self.icon_rect.y <= gs.SCREEN_BORDER_TOP:
                        self.icon_rect.y = gs.SCREEN_BORDER_TOP
                # Moving down
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.icon_rect.y += gs.IMAGE_SIZE
                    if self.icon_rect.y >= gs.SCREEN_BORDER_BOTTOM:
                        self.icon_rect.y = gs.SCREEN_BORDER_BOTTOM - gs.IMAGE_SIZE
                
                # Cycle through insert pieces
                if event.key == pygame.K_SPACE:
                    self.index += 1
                    if self.index >= len(self.inserts):
                        self.index = self.index % len(self.inserts)
                    self.insert_tile = self.inserts[self.index]

                # Save level
                if event.key == pygame.K_RETURN:
                    self.validate_level()
                    self.all_levels.append(self.matrix)
                    self.level_data.save_level_data(self.all_levels)
                    self.main.levels.level_data = self.all_levels
                    self.active = False
                
    def update(self):
        icon_grid_pos_col = (self.icon_rect.left - gs.SCREEN_BORDER_LEFT) // (gs.IMAGE_SIZE // 2)
        icon_grid_pos_row = (self.icon_rect.top - gs.SCREEN_BORDER_TOP) // (gs.IMAGE_SIZE // 2)

        self.matrix[icon_grid_pos_row][icon_grid_pos_col] = self.insert_tile[0]
        self.matrix[icon_grid_pos_row][icon_grid_pos_col + 1] = self.insert_tile[1]
        self.matrix[icon_grid_pos_row + 1][icon_grid_pos_col] = self.insert_tile[2]
        self.matrix[icon_grid_pos_row + 1][icon_grid_pos_col + 1] = self.insert_tile[3]

    def draw(self, window):
        window.blit(self.overlay_screen, (0, 0))
        self.draw_grid_to_screen(window)

        for i, row in enumerate(self.matrix):
            for j, tile in enumerate(row):
                if tile == -1:
                    continue
                else:
                    window.blit(self.tile_type[tile], (gs.SCREEN_BORDER_LEFT + (j * gs.IMAGE_SIZE // 2),
                                                       gs.SCREEN_BORDER_TOP + (i * gs.IMAGE_SIZE // 2)))

        window.blit(self.icon_image, self.icon_rect)
        pygame.draw.rect(window, gs.GREEN, self.icon_rect, 1)

    def draw_screen(self):
        """Generate the game screen"""

        overlay_screen = pygame.Surface((gs.SCREEN_WIDTH, gs.SCREEN_HEIGHT))
        overlay_screen.fill(gs.GREY)
        pygame.draw.rect(overlay_screen, gs.BLACK, (gs.GAME_SCREEN))

        return overlay_screen
    
    def draw_grid_to_screen(self, window):
        vertical_lines = (gs.SCREEN_BORDER_RIGHT - gs.SCREEN_BORDER_LEFT) // (gs.IMAGE_SIZE)
        horizontal_lines = (gs.SCREEN_BORDER_BOTTOM - gs.SCREEN_BORDER_TOP) // (gs.IMAGE_SIZE)

        for i in range(vertical_lines):
            pygame.draw.line(window, gs.RED, (gs.SCREEN_BORDER_LEFT + (i * gs.IMAGE_SIZE), gs.SCREEN_BORDER_TOP), 
                                             (gs.SCREEN_BORDER_LEFT + (i * gs.IMAGE_SIZE), gs.SCREEN_BORDER_BOTTOM))
        
        for i in range(horizontal_lines):
            pygame.draw.line(window, gs.RED, (gs.SCREEN_BORDER_LEFT, gs.SCREEN_BORDER_TOP + (i * gs.IMAGE_SIZE)), 
                                             (gs.SCREEN_BORDER_RIGHT, gs.SCREEN_BORDER_TOP + (i * gs.IMAGE_SIZE)))
            
    def generate_level_matrix(self):
        rows = (gs.SCREEN_BORDER_BOTTOM - gs.SCREEN_BORDER_TOP) // (gs.IMAGE_SIZE // 2)
        cols = (gs.SCREEN_BORDER_RIGHT - gs.SCREEN_BORDER_LEFT) // (gs.IMAGE_SIZE // 2)
        matrix = []

        for row in range(rows):
            line = []
            for col in range(cols):
                line.append(-1)
            matrix.append(line)
        
        return matrix
    
    def validate_level(self):
        for cell in gs.ENEMY_TANK_SPAWNS:
            self.matrix[cell[1]][cell[0]] = -1
        for cell in gs.PLAYER_TANK_SPAWNS:
            self.matrix[cell[1]][cell[0]] = -1
        for cell in gs.BASE:
            self.matrix[cell[1]][cell[0]] = -1
        
        self.matrix[24][12] = 999

        for cell in gs.FORT:
            if self.matrix[cell[1]][cell[0]] == -1:
                self.matrix[cell[1]][cell[0]] = 432
