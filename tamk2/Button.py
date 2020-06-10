
import pygame
class Button():
    def __init__(self,screen,width,height,button_color,text_color,text,button_pos):
        self.font = pygame.font.SysFont('microsoftyaheimicrosoftyaheiuibold',48)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width = width
        self.height = height
        self.button_color = button_color
        self.text_color = text_color
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = button_pos
        self.load_text(text)

    def load_text(self,text):
        self.text_image = self.font.render(text,True,self.text_color,self.button_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.text_image,self.text_image_rect)

