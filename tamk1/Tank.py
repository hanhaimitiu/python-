import pygame

class Tank1():
    def __init__(self,screen):

        self.screen = screen
        self.img = pygame.image.load("坦克1.png")
        self.rect = self.img.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.center = self.screen_rect.center

        self.rect.top = self.screen_rect.top
        self.rect.bottom = self.screen_rect.bottom
        self.rect.left = self.screen_rect.left
        self.rect.right = self.screen_rect.right






    def draw_tank(self):
        self.screen.blit(self.img,self.rect)


class Tank2():
    def __init__(self,screen):

        self.screen = screen
        self.img = pygame.image.load("坦克_1.png")
        self.rect = self.img.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.center = self.screen_rect.center

        self.rect.top = self.screen_rect.top
        self.rect.bottom = self.screen_rect.bottom
        self.rect.left = self.screen_rect.left
        self.rect.right = self.screen_rect.right






    def draw_tank(self):
        self.screen.blit(self.img,self.rect)