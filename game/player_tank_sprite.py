import pygame


from settings import player_tank_image


class PlayerTank(pygame.sprite.Sprite):
    # hitbox_window = pygame.display.set_mode((50, 50))

    def __init__(self, x: int, y: int, speed: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = speed

        self.direction = 'UP'
        self.original_image = pygame.image.load(player_tank_image)
        self.image = pygame.transform.scale(self.original_image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        
        # self.hitbox = (self.x - 1, self.y - 1, 52, 52)
    
    def update(self, keys) -> None:
        if keys[pygame.K_UP]:
            self.y -= self.speed
            self.direction = 'UP'
        elif keys[pygame.K_DOWN]:
            self.y += self.speed
            self.direction = 'DOWN'
        elif keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.direction = 'LEFT'
        elif keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.direction = 'RIGHT'

        self.rect.topleft = (self.x, self.y)

    def rotate(self) -> None:
        if self.direction == 'UP':
            self.image = pygame.transform.rotate(self.original_image, 0)
        elif self.direction == 'DOWN':
            self.image = pygame.transform.rotate(self.original_image, 180)
        elif self.direction == 'LEFT':
            self.image = pygame.transform.rotate(self.original_image, 90)
        elif self.direction == 'RIGHT':
            self.image = pygame.transform.rotate(self.original_image, 270)

        # TODO: This scaling to be refactored, so it becomes more memory efficient
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect(center=self.rect.center)

    def hit_object(self, enemy_team):
        hit_obects = pygame.sprite.spritecollide(self, enemy_team, False)
        # if hit_obects:
        #     # Handling left side
        #     if self.x + 50 >= hit_obects[0].x:
        #         self.x = hit_obects[0].x - self.rect.width
            
            # if self.x <= hit_obects[0].x + 50:
            #     self.x = hit_obects[0].x + 50

    def draw(self, screen) -> None:
        # Hitbox is declared here additionally, so it sticks with the object
        # self.hitbox = (self.x - 1, self.y - 1, 52, 52)
        # pygame.draw.rect(self.hitbox_window, (255, 0, 0), self.hitbox, 1)

        if self.x <= 0:
            self.x = 0
        if self.y <= 0:
            self.y = 0
        if self.x >= 750:
            self.x = 750
        if self.y >= 550:
            self.y = 550
        
        screen.blit(self.image, (self.x, self.y))
