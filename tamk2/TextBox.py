import pygame


class TextBox():
    def __init__(self,screen,width,height,size,font,font_color,bg_color, location,text):
        self.screen = screen
        self.width = width
        self.font = font
        self.height = height
        self.size = size
        self.font_color = font_color
        self.bg_color = bg_color
        self.location = location
        self.text = text

    def key_down_text(self,event):
        unicode = event.unicode
        key = event.key

        #退格键
        if key==8:
            self.text = self.text[:-1]
            return None
        #切换大小写键
        if key == 301:
            return None

        #回车键
        if key==13:
            return self.text

        if not unicode=="":
            char = unicode
        else:
            char = chr(key)

        self.text += char
        return None


    def draw_textbox(self):
        font = pygame.font.SysFont(self.font, self.size)
        text = font.render(str(self.text),
                           True, self.font_color, self.bg_color)
        text_rect = text.get_rect()
        text_rect.center = self.location
        self.screen.blit(text, text_rect)

