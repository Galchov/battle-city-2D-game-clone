import pygame
import settings as gs


class StartScreen:
    
    def __init__(self, main, assets):
        self.main = main
        self.assets = assets

        # Start screen coordinates
        self.start_y = gs.SCREEN_HEIGHT
        self.end_y = 0

        # Start screen images and rect
        self.image = self.assets.start_screen
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.x, self.y = self.rect.topleft

        # Options positions
        self.option_positions = [
            (4 * gs.IMAGE_SIZE, 7.75 * gs.IMAGE_SIZE),
            (4 * gs.IMAGE_SIZE, 8.75 * gs.IMAGE_SIZE),
            (4 * gs.IMAGE_SIZE, 9.75 * gs.IMAGE_SIZE),
        ]
        
        self.token_index = 0
        self.token_image = self.assets.start_screen_token
        self.token_rect = self.token_image.get_rect(topleft=self.option_positions[self.token_index])

        self.start_screen_active = True

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.main.run = False
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.main.run = False
                    return False
                
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self._choose_options_main_menu(-1)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self._choose_options_main_menu(1)

                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self._selection_option_action()
        
        return True
    
    def update(self):
        pass

    def draw(self, window):
        window.blit(self.image, self.rect)

        if self.start_screen_active:
            window.blit(self.token_image, self.token_rect)

    def _choose_options_main_menu(self, num):
        """Update the token's position to the chosen option"""

        self.token_index += num
        self.token_index = self.token_index % len(self.option_positions)
        self.token_rect.topleft = self.option_positions[self.token_index]

    def _selection_option_action(self):
        if self.token_index == 0:
            print("Start a new game with just 1 player")
        elif self.token_index == 1:
            print("Start a new game with 2 players")
        elif self.token_index == 2:
            print("Start a construction mode")
