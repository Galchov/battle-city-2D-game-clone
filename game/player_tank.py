import pygame

from characters import Tank


class PlayerTank(Tank):

    def __init__(self, game, assets, groups, position, direction, color, tank_level) -> None:
        super().__init__(game, assets, groups, position, direction, color, tank_level)

    def input(self, keypressed) -> None:
        """Handles the tank movement"""

        if self.color == "Gold":
            if keypressed[pygame.K_w]:
                self.move_tank("Up")
            elif keypressed[pygame.K_s]:
                self.move_tank("Down")
            elif keypressed[pygame.K_a]:
                self.move_tank("Left")
            elif keypressed[pygame.K_d]:
                self.move_tank("Right")
        
        if self.color == "Green":
            if keypressed[pygame.K_UP]:
                self.move_tank("Up")
            elif keypressed[pygame.K_DOWN]:
                self.move_tank("Down")
            elif keypressed[pygame.K_LEFT]:
                self.move_tank("Left")
            elif keypressed[pygame.K_RIGHT]:
                self.move_tank("Right")
