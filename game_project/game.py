import pygame
import settings as gs
import random

from characters import Tank
from player_tank import PlayerTank
from game_hud import GameHud
from tile import BrickTile


class Game:

    def __init__(self, main, assets, player_1=True, player_2=False) -> None:
        """The main Game Object"""
        self.main = main
        self.assets = assets

        # Objects groups
        self.groups = {
            "Player_Tanks": pygame.sprite.Group(),
            "All_Tanks": pygame.sprite.Group(), 
            "Bullets": pygame.sprite.Group(),
            "Destructable_Tiles": pygame.sprite.Group(),
            "Impassable_Tiles": pygame.sprite.Group(),
            }

        # Game HUD
        self.hud = GameHud(self, self.assets)

        # Level information
        self.level_num = 1
        self.data = self.main.levels

        # Player attributes
        self.player_1_active = player_1
        self.player_2_active = player_2

        # Player objects
        if self.player_1_active:
            self.player_1 = PlayerTank(self, self.assets, self.groups, gs.PLAYER_1_POS, "Up", "Gold", 0)
        if self.player_2_active:
            self.player_2 = PlayerTank(self, self.assets, self.groups, gs.PLAYER_2_POS, "Up", "Green", 1)

        # Number of Enemy Tanks
        self.enemies = 20
        self.enemy_tank_spawn_timer = gs.TANK_SPAWNING_TIME
        self.enemy_spawn_postitions = [gs.AI_TANK_1_POS, gs.AI_TANK_2_POS, gs.AI_TANK_3_POS]

        # Load the stage
        self.create_new_stage()

        # Game over
        self.end_game = False

    def input(self) -> None:
        """Handle the game inputs while running"""

        keypressed = pygame.key.get_pressed()
        if self.player_1_active:
            self.player_1.input(keypressed)
        if self.player_2_active:
            self.player_2.input(keypressed)

        # pygame event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.main.run = False

            # Keyboard shortcut to quit the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.end_game = True

                if event.key == pygame.K_SPACE:
                    if self.player_1_active:
                        self.player_1.shoot()
                if event.key == pygame.K_RCTRL:
                    if self.player_2_active:
                        self.player_2.shoot()
                if event.key == pygame.K_RETURN:
                    Tank(self, self.assets, self.groups, (100, 100), "Down")
                    self.enemies -= 1
    
    def update(self) -> None:

        self.hud.update()
        for key in self.groups.keys():
            if key == "Player_Tanks":
                continue
            for item in self.groups[key]:
                item.update()
        
        self.spawn_enemy_tanks()

    def draw(self, window) -> None:
        """Drawing to the screen"""

        # Draw the HUD
        self.hud.draw(window)
        
        # Draw characters
        for key in self.groups.keys():
            for item in self.groups[key]:
                item.draw(window)

    def create_new_stage(self):
        # Reset the various sprite groups to Zero
        for key, value in self.groups.items():
            if key == "Player_Tanks":
                continue
            value.empty()

        # Retrieves the specific level data
        self.current_level_data = self.data.level_data[self.level_num - 1]

        # Number of enemy tanks to spawn in the stage, tracked down to Zero
        # self.enemies = random.choice([16, 17, 18, 19, 20])
        self.enemies = 5

        # Track the number of killed enemies, tracked down to Zero
        self.enemies_killed = self.enemies

        # Load in the level data
        self.load_level_data(self.current_level_data)

        # Generate the spawn queue for the AI tanks
        self.generate_spawn_queue()
        self.spawn_pos_index = 0
        self.spawn_queue_index = 0
        print(self.spawn_queue)

        if self.player_1_active:
            self.player_1.new_stage_spawn(gs.PLAYER_1_POS)
        if self.player_2_active:
            self.player_2.new_stage_spawn(gs.PLAYER_2_POS)

    def load_level_data(self, level):
        """Load the level data"""

        self.grid = []

        for i, row in enumerate(level):
            line = []
            for j, tile in enumerate(row):
                pos = (gs.SCREEN_BORDER_LEFT + (j * gs.IMAGE_SIZE // 2), 
                       gs.SCREEN_BORDER_TOP + (i * gs.IMAGE_SIZE // 2))
                if int(tile) < 0:
                    line.append("   ")
                elif int(tile) == 432:
                    line.append(f"{tile}")
                    map_tile = BrickTile(pos, self.groups["Destructable_Tiles"], self.assets.brick_tiles)
                    self.groups["Impassable_Tiles"].add(map_tile)
                elif int(tile) == 482:
                    line.append(f"{tile}")
                elif int(tile) == 483:
                    line.append(f"{tile}")
                elif int(tile) == 484:
                    line.append(f"{tile}")
                elif int(tile) == 533:
                    line.append(f"{tile}")
                else:
                    line.append(f"{tile}")
                
            self.grid.append(line)
        
        # for row in self.grid:
        #     print(row)

    def generate_spawn_queue(self):
        """Generates a list of tanks that will be spawning during the level"""

        self.spawn_queue_ratios = gs.TANK_SPAWN_QUEUE[f"queue_{str((self.level_num - 1 % 36) // 3)}"]
        self.spawn_queue = []

        for lvl, ratio in enumerate(self.spawn_queue_ratios):
            for i in range(int(round(self.enemies * (ratio / 100)))):
                self.spawn_queue.append(f"level_{lvl}")
        
        random.shuffle(self.spawn_queue)

    def spawn_enemy_tanks(self):
        """Spawn enemy tanks, as each one spawns as per the queue"""

        if self.enemies == 0:
            return
        
        if pygame.time.get_ticks() - self.enemy_tank_spawn_timer >= gs.TANK_SPAWNING_TIME:
            position = self.enemy_spawn_postitions[self.spawn_pos_index % 3]
            tank_level = gs.TANK_CRITERIA[self.spawn_queue[self.spawn_queue_index % len(self.spawn_queue)]]["image"]
            Tank(self, self.assets, self.groups, position, "Down", True, "Silver", tank_level)

            # Reset enemy tank spawn timer
            self.enemy_tank_spawn_timer = pygame.time.get_ticks()
            self.spawn_pos_index += 1
            self.spawn_queue_index += 1
            self.enemies -= 1
