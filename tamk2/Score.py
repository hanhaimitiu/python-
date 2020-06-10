import pygame
class Score():
    def __init__(self, screen, tank1, tank2, bullets1, bullets2, settings_screen):
        self.screen = screen
        self.tank1 = tank1
        self.tank2 = tank2
        self.bullets1 = bullets1
        self.bullets2 = bullets2
        self.score1 = 0
        self.score2 = 0
        self.temp1 = False
        self.temp2 = False
        self.settings = settings_screen
        self.sound_explode = pygame.mixer.Sound("music//explode.wav")

    def score_draw(self):
        font = pygame.font.SysFont("隶书", 48)
        text = font.render(str(self.score1) + "：" + str(self.score2),
                           True, (255, 255, 255), (0, 255, 0))
        text_rect = text.get_rect()
        text_rect.center = (500, 50)
        self.screen.blit(text, text_rect)
        if self.temp1 or self.temp2:
            print(self.score1)
            print(self.score2)
            print("bifen")
            self.temp1 = False
            self.temp2 = False

    def score_change(self):
        for i in self.bullets1.copy():
            if self.tank2.rect.collidepoint(i.rect.center):
                print("tank2_ok")
                txt_rect = pygame.Rect(0, 0, 80, 80)
                pygame.draw.rect(self.screen, (200, 230, 50), txt_rect)
                self.score1 += 1
                self.temp1 = True
                self.bullets1.remove(i)
                self.sound_explode.play()
                break
            self.temp1 = False
        for i in self.bullets2.copy():
            if self.tank1.rect.collidepoint(i.rect.center):
                txt_rect = pygame.Rect(0, 0, 80, 80)
                pygame.draw.rect(self.screen, (255, 255, 255), txt_rect)
                self.score2 += 1
                self.temp2 = True
                self.bullets2.remove(i)
                self.sound_explode.play()
                break
            self.temp2 = False

    def who_win(self):
        if self.score1 == 16 and self.score1 > self.score2:
            self.screen.fill(self.settings.bg_color)
            font = pygame.font.SysFont("隶书", 48)
            text = font.render("TANK1胜利!",
                               True, (255, 255, 255), (0, 255, 0))
            text_rect = text.get_rect()
            text_rect.center = (500, 300)
            self.screen.blit(text, text_rect)
            return True
        if self.score2 == 16 and self.score2 > self.score1:
            self.screen.fill(self.settings.bg_color)
            font = pygame.font.SysFont("隶书", 48)
            text = font.render("TANK2胜利!",
                               True, (255, 255, 255), (0, 255, 0))
            text_rect = text.get_rect()
            text_rect.center = (500, 300)
            self.screen.blit(text, text_rect)
            return True
        if self.score2 == 15 == self.score1:
            self.screen.fill(self.settings.bg_color)
            font = pygame.font.SysFont("隶书", 48)
            text = font.render("平局!",
                               True, (255, 255, 255), (0, 255, 0))
            text_rect = text.get_rect()
            text_rect.center = (500, 300)
            self.screen.blit(text, text_rect)
            return True
        return False