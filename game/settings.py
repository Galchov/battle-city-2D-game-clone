import os


# Directory settings and paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

IMAGE_DIR = os.path.join(PROJECT_ROOT, "assets", "images")

PLAYER_TANK_IMAGE = os.path.join(IMAGE_DIR, "player_1.png")
ENEMY_TANK_IMAGE = os.path.join(IMAGE_DIR, "enemy_3.png")

# Screen settings
SCREEN_WIDTH = 850
SCREEN_HEIGHT = 750

BATTLEFIELD_SIZE = 750
BATTLEFIELD_X = 0
BATTLEFIELD_Y = (SCREEN_HEIGHT - BATTLEFIELD_SIZE) // 2

STAT_PANEL_WIDTH = SCREEN_WIDTH - BATTLEFIELD_SIZE
STAT_PANEL_X = BATTLEFIELD_SIZE
STAT_PANEL_Y = 0
STAT_PANEL_HEIGHT = SCREEN_HEIGHT

# FPS settings
FPS = 60

# Game objects setttings
PLAYER_SPAWN_POINT = (250, 700)
ENEMY_SPAWN_POINTS = ((0, 0), (350, 0), (700, 0))

# Colour definitions
DARK_GREY = (128, 128, 128)
