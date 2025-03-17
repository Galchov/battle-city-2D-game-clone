import pygame

import settings as gs


class LevelEditor:

    def __init__(self, main, assets):
        self.main = main
        self.assets = assets
        self.active = True

        self.level_data = None
        self.all_levels = []

        self.overlay_screen = self.draw_screen()
        self.matrix = self.generate_level_matrix()

        self.tile_type = {
            432: self.assets.brick_tiles["small"],
            482: self.assets.steel_tiles["small"],
            483: self.assets.forest_tiles["small"],
            484: self.assets.ice_tiles["small"],
            533: self.assets.water_tiles["small_1"],
            999: self.assets.flag["Phoenix_Alive"]
        }
        
        self.icon_image = self.assets.tank_images["Tank_4"]["Gold"]["Up"][0]
        self.icon_rect = self.icon_image.get_rect(topleft=(gs.SCREEN_BORDER_LEFT, gs.SCREEN_BORDER_TOP))

    def input(self):
        for event in pygame.event.get():
            print(event)  # For debugging
            if event == pygame.QUIT:
                self.main.run = False
            elif event == pygame.KEYDOWN:
                print(f"LEVEL EDITOR CLASS - KEY PRESSED: {event.key}")  # For debugging
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
                
    def update(self):
        pass

    def draw(self, window):
        window.blit(self.overlay_screen, (0, 0))
        self.draw_grid_to_screen(window)

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