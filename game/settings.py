import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

IMAGE_DIR = os.path.join(PROJECT_ROOT, "assets", "images")

player_tank_image = os.path.join(IMAGE_DIR, "Battle_City_Tank_Player1.png")
enemy_tank_image = os.path.join(IMAGE_DIR, "Battle_City_Tank_Enemy3.png")
