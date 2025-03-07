
import pygame
import settings as gs


class GameHud:

    def __init__(self, game, assets) -> None:
        self.game = game
        self.assets = assets
        self.images = self.assets.hud_images
        self.hud_overlay = self.generate_hud_overlay_screen()

    def generate_hud_overlay_screen(self) -> object:
        """Generates fixed overlay screen image"""

        overlay_screen = pygame.Surface((gs.SCREEN_WIDTH, gs.SCREEN_HEIGHT))
        overlay_screen.fill(gs.DARK_GREY)
        pygame.draw.rect(overlay_screen, gs.BLACK, (gs.GAME_SCREEN))
        overlay_screen.blit(self.images["info_panel"], (gs.INFO_PANEL_X, gs.INFO_PANEL_Y))
        overlay_screen.set_colorkey(gs.BLACK)
        return overlay_screen
    
    def update(self) -> None:
        pass

    def draw(self, window) -> None:
        window.blit(self.hud_overlay, (0, 0))
        