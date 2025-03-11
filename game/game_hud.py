
import pygame
import settings as gs


class GameHud:

    def __init__(self, game, assets) -> None:
        self.game = game
        self.assets = assets
        self.images = self.assets.hud_images
        self.hud_overlay = self.generate_hud_overlay_screen()

        # Player lives and Display
        self.player_1_active = False
        self.player_1_lives = 0
        self.player_1_lives_image = self.display_player_lives(self.player_1_lives, self.player_1_active)

        self.player_2_active = False
        self.player_2_lives = 0
        self.player_2_lives_image = self.display_player_lives(self.player_2_lives, self.player_2_active)

        # Level information
        self.level = 1
        self.level_image = self.display_stage_number(self.level)
        self.level_image_rect = self.level_image.get_rect(topleft=(14.5 * gs.IMAGE_SIZE, 13 * gs.IMAGE_SIZE))

    def generate_hud_overlay_screen(self) -> object:
        """Generates fixed overlay screen image"""

        overlay_screen = pygame.Surface((gs.SCREEN_WIDTH, gs.SCREEN_HEIGHT))
        overlay_screen.fill(gs.GREY)
        pygame.draw.rect(overlay_screen, gs.BLACK, (gs.GAME_SCREEN))
        overlay_screen.blit(self.images["info_panel"], (gs.INFO_PANEL_X, gs.INFO_PANEL_Y))
        overlay_screen.set_colorkey(gs.BLACK)
        return overlay_screen
    
    # Generate the player's lives image on the HUD
    def display_player_lives(self, player_lives, player_active):
        width, height = gs.IMAGE_SIZE, gs.IMAGE_SIZE // 2
        surface = pygame.Surface((width, height))
        surface.fill(gs.BLACK)

        if player_lives > 99:
            player_lives = 99
        if not player_active:
            surface.blit(self.images["grey_square"], (0, 0))
            surface.blit(self.images["grey_square"], (gs.IMAGE_SIZE // 2, 0))
            return surface
        if player_lives < 10:
            image = pygame.transform.rotate(self.images["life"], 180)
        else:
            num = str(player_lives)[0]
            image = self.images(f"num_{num}")
        
        surface.blit(image, (0, 0))
        num = str(player_lives)[-1]
        image_2 = self.images[f"num_{num}"]
        surface.blit(image_2, (gs.IMAGE_SIZE // 2, 0))
        return surface
    
    # Generate the stage level image
    def display_stage_number(self, level):
        width, height = gs.IMAGE_SIZE, gs.IMAGE_SIZE // 2
        surface = pygame.Surface((width, height))
        surface.fill(gs.BLACK)

        if level < 10:
            image_1 = self.images["num_0"]
        else:
            num = str(level)[0]
            image_1 = self.images[f"num_{num}"]

        surface.blit(image_1, (0, 0))
        num = str(level)[-1]
        image_2 = self.images[f"num_{num}"]
        surface.blit(image_2, (gs.IMAGE_SIZE // 2, 0))
        return surface
    
    def update(self) -> None:
        # Updat the number of player's lives available
        self.player_1_active = self.game.player_1_active

        if self.player_1_active:
            if self.player_1_lives != self.game.player_1.lives:
                self.player_1_lives = self.game.player_1.lives
                self.player_1_lives_image = self.display_player_lives(self.player_1_lives, self.player_1_active)

        self.player_2_active = self.game.player_2_active
        if self.player_2_active:
            if self.player_2_lives != self.game.player_2.lives:
                self.player_2_lives = self.game.player_2.lives
                self.player_2_lives_image = self.display_player_lives(self.player_2_lives, self.player_2_active)

        # Update the stage number image
        if self.level != self.game.level_num:
            self.level = self.game.level_num
            self.level_image = self.display_stage_number(self.level)

    def draw(self, window) -> None:
        window.blit(self.hud_overlay, (0, 0))

        window.blit(self.player_1_lives_image, (14.5 * gs.IMAGE_SIZE, 9.5 * gs.IMAGE_SIZE))
        window.blit(self.player_2_lives_image, (14.5 * gs.IMAGE_SIZE, 11 * gs.IMAGE_SIZE))

        window.blit(self.level_image, self.level_image_rect)
        