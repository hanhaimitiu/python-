import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self,settings, screen,tank,bullet_color,tank_which):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.center = tank.rect.center
        self.color = bullet_color
        self.y = self.rect.y
        self.x = self.rect.x
        self.img_now_num = int(tank_which)
        self.speed = settings.bullet_speed

    def update(self):
        if self.img_now_num==4:
            '''
            4代表向左发射'''
            self.x -= self.speed
            self.rect.x = self.x

        if self.img_now_num==3:
            '''
            3代表向下发射'''
            self.y += self.speed
            self.rect.y = self.y
        if self.img_now_num==2:
            '''
            2代表向右发射'''

            self.x += self.speed
            self.rect.x = self.x

        if self.img_now_num==1:
            '''
            4代表向上发射'''
            self.y -= self.speed
            self.rect.y = self.y

    def draw_bull(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
