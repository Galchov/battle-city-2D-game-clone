import pygame
import settings as gs


class GameAssets:
    
    def __init__(self) -> None:
        """Object containing all of the game's assets"""

        ### Loading start screen images ###
        self.start_screen = self.load_individual_image("start_screen", True, (gs.SCREEN_WIDTH, gs.SCREEN_HEIGHT))
        self.start_screen_token = self.load_individual_image("token", True, (gs.IMAGE_SIZE, gs.IMAGE_SIZE))

        ### Loading the sprite sheets ###
        self.spritesheet = self.load_individual_image("battle_city_sprites")
        self.number_image_black_white = self.load_individual_image("numbers_black_white")
        self.number_image_black_orange = self.load_individual_image("numbers_black_orange")

        ### Characters images ###
        self.tank_images = self._load_tank_images()
        self.bullet_images = self._get_specified_images(self.spritesheet, gs.BULLETS, gs.BLACK)
        self.shield_images = self._get_specified_images(self.spritesheet, gs.SHIELD, gs.BLACK)
        self.spawn_star_images = self._get_specified_images(self.spritesheet, gs.SPAWN_STAR, gs.BLACK)

        ### Game related images ###
        self.power_up = self._get_specified_images(self.spritesheet, gs.POWER_UPS, gs.BLACK)
        self.flag = self._get_specified_images(self.spritesheet, gs.FLAG, gs.BLACK)
        self.explosions = self._get_specified_images(self.spritesheet, gs.EXPLOSIONS, gs.BLACK)
        self.score = self._get_specified_images(self.spritesheet, gs.SCORE, gs.BLACK)

        ### Game HUD images ###
        self.hud_images = self._get_specified_images(self.spritesheet, gs.HUD_INFO, gs.BLACK, transparent=False)
        self.context = self._get_specified_images(self.spritesheet, gs.CONTEXT, gs.BLACK)

        ### Tile images ###
        self.brick_tiles = self._get_specified_images(self.spritesheet, gs.MAP_TILES[432], gs.BLACK)
        self.steel_tiles = self._get_specified_images(self.spritesheet, gs.MAP_TILES[482], gs.BLACK)
        self.forest_tiles = self._get_specified_images(self.spritesheet, gs.MAP_TILES[483], gs.BLACK)
        self.ice_tiles = self._get_specified_images(self.spritesheet, gs.MAP_TILES[484], gs.BLACK)
        self.water_tiles = self._get_specified_images(self.spritesheet, gs.MAP_TILES[533], gs.BLACK)

        ### Number images ###
        self.number_black_white = self._get_specified_images(self.number_image_black_white, gs.NUMS, gs.BLACK)
        self.number_black_orange = self._get_specified_images(self.number_image_black_orange, gs.NUMS, gs.BLACK)

        ### Score sheet images ###
        score_images = ["hi_score", "arrow", "player_1", "player_2", "pts", "stage", "total"]
        self.score_sheet_images = {}
        for image in score_images:
            self.score_sheet_images[image] = self.load_individual_image(image)

    ##### Loading only the tanks images #####
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
                surface.blit(self.spritesheet, (0, 0), (col * gs.SPRITE_SIZE, row * gs.SPRITE_SIZE, 
                                                         gs.SPRITE_SIZE, gs.SPRITE_SIZE))
                surface.set_colorkey(gs.BLACK)

                # Resize each of the images
                surface = self.scale_image(surface, gs.SPRITE_SCALE)

                # Sort the tank's image into its correct level
                tank_level = self._sort_tanks_into_levels(row)

                # Sort the tank into its correct group
                tank_group = self._sort_tanks_into_groups(row, col)

                # Sort the tank images into the correct directions
                tank_direction = self._sort_tanks_by_direction(col)

                tank_image_dict[tank_level][tank_group][tank_direction].append(surface)

        return tank_image_dict

    ##### Sorting methods for getting tanks into the correct segments of the dictionary #####
    def scale_image(self, image, scale):
        """Scaling the image based on the given size"""

        width, height = image.get_size()
        image = pygame.transform.scale(image, (scale * width, scale * height))

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

    ##### Load specified images from the spritesheet #####
    def _get_specified_images(self, spritesheet, image_coordinates_dict, color, transparent=True):
        """Adding the specified images form the spritesheet as per the 
        coordinates received from the image dictionary"""

        image_dictionary = {}

        for key, pos in image_coordinates_dict.items():
            image = self.get_image(spritesheet, pos[0], pos[1], pos[2], pos[3], color, transparent)
            image_dictionary.setdefault(key, image)
        
        return image_dictionary

    def get_image(self, spritesheet, x_pos, y_pos, width, height, color, transparent=True):
        """Get specified image from the spritesheet"""

        surface = pygame.Surface((width, height))
        surface.fill(color)
        surface.blit(spritesheet, (0, 0), (x_pos, y_pos, width, height))

        if transparent:
            surface.set_colorkey(color)
        
        surface = self.scale_image(surface, gs.SPRITE_SCALE)

        return surface

    ##### Loading an image from the assets folder #####
    def load_individual_image(self, path, scale=False, size=(0, 0)):
        """Loading individual image"""

        image = pygame.image.load(f"assets/{path}.png").convert_alpha()
        if scale:
            image = pygame.transform.scale(image, size)
        return image
