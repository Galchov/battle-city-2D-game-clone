import pygame
import settings as gs


class GameAssets:
    def __init__(self) -> None:
        """Object containing all of the game's assets"""

        # Loading start screen images
        self.start_screen = self.load_individual_image("start_screen", True, (gs.SCREEN_WIDTH, gs.SCREEN_HEIGHT))
        self.start_screen_token = self.load_individual_image("token", True, (gs.IMAGE_SIZE, gs.IMAGE_SIZE))

        # Loading the sprite sheets
        self.sprite_sheet = self.load_individual_image("battle_city_sprites")
        self.number_image_black_white = self.load_individual_image("numbers_black_white")
        self.number_image_black_orange = self.load_individual_image("numbers_black_orange")

        # Loading score sheet images
        score_images = ["hi_score", "arrow", "player_1", "player_2", "pts", "stage", "total"]
        self.score_sheet_images = {}
        for image in score_images:
            self.score_sheet_images[image] = self.load_individual_image(image)

        # Characters images
        self.tank_images = self._load_tank_images()

    def _load_tank_images(self):
        """Get all the tank images from the sprite sheet and sort them into a dictionary"""
        tank_image_dict = {}

        tanks_types = ["Gold", "Silver", "Green", "Special"]
        directions = ["Up", "Down", "Left", "Right"]

        for tank in range(8):
            tank_image_dict[f"Tank_{tank}"] = {}
            for group in tanks_types:
                tank_image_dict[f"Tank_{tank}"][group] = {}
                for direction in directions:
                    tank_image_dict[f"Tank_{tank}"][group][direction] = []
        
        # Create a new image for each of the tank images
        for row in range(16):
            for col in range(16):
                surface = pygame.Surface((gs.SPRITE_SIZE, gs.SPRITE_SIZE))
                surface.fill(gs.BLACK)
                surface.blit(self.sprite_sheet, (0, 0), (col * gs.SPRITE_SIZE, row * gs.SPRITE_SIZE, 
                                                         gs.SPRITE_SIZE, gs.SPRITE_SIZE))
                surface.set_colorkey(gs.BLACK)

                # Resize each of the images
                surface = self.scale_image(surface, gs.IMAGE_SIZE)

                # Sort the tank's image into its correct level
                tank_level = self._sort_tanks_into_levels(row)

                # Sort the tank into its correct group
                tank_group = self._sort_tanks_into_groups(row, col)

                # Sort the tank images into the correct directions
                tank_direction = self._sort_tanks_by_direction(col)

                tank_image_dict[tank_level][tank_group][tank_direction].append(surface)

        return tank_image_dict

    # Sorting methods for getting tanks into the correct segments of the dictionary
    def scale_image(self, image, scale):
        """Scaling the image based on the given size"""

        image = pygame.transform.scale(image, (scale, scale))

        return image
    
    def _sort_tanks_into_levels(self, row):
        """Sort the tanks based on their row"""

        tank_levels = {0: "Tank_0", 1: "Tank_1", 2: "Tank_2", 3: "Tank_3",
                       4: "Tank_4", 5: "Tank_5", 6: "Tank_6", 7: "Tank_7"}
        
        return tank_levels[row % 8]
    
    def _sort_tanks_into_groups(self, row, col):
        """Sort the tank's image into its related colours group"""

        if 0 <= row <= 7 and 0 <= col <= 7:
            return "Gold"
        elif 8 <= row <= 16 and 0 <= col <= 7:
            return "Green"
        elif 0 <= row <= 7 and 8 <= col <= 16:
            return "Silver"
        else:
            return "Special"
        
    def _sort_tanks_by_direction(self, col):
        """Sort the tanks by their direction"""

        if col % 7 <= 1: return "Up"
        elif col % 7 <= 3: return "Left"
        elif col % 7 <= 5: return "Down"
        else: return "Right"

    # Loading an image from the assets folder
    def load_individual_image(self, path, scale=False, size=(0, 0)):
        """Loading individual image"""

        image = pygame.image.load(f"assets/{path}.png").convert_alpha()
        if scale:
            image = pygame.transform.scale(image, size)
        return image
