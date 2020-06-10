import sys
import pygame
import Tank, Game_Settings, Bull, Button, Score, TextBox
from pygame.sprite import Group
import time
import socket
from time import ctime
import threading
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
local_ip = ("192.168.31.205", 19999)
target_ip = ("192.168.31.116", 18000)
udp_socket.bind(local_ip)
get_data = None
send_data = None
tank1_posx,tank1_posy=0,0
tank2_posx,tank2_posy=0,0
#n代表tank1
n=0
m=0

def update_screen(tank1, bullets1, tank2, bullets2):
    bullets1.update()
    bullets2.update()
    tank1.draw_tank()
    tank2.draw_tank()

def recv_msg(udp_socket):
    global get_data,n,tank1_posx,tank1_posy
    while True:
        print("jiesou")
        recv_data, addr = udp_socket.recvfrom(1024)
        print(recv_data,addr)
        if recv_data:

            recv_data=recv_data.decode("utf-8")
            print(recv_data)

            recv_data = recv_data.split("|")
            get_data = recv_data[0]
            tank1_posx= int(recv_data[1])
            tank1_posy=int(recv_data[2])
        else:
            print(">>>")
            n=0
        time.sleep(0.015)





def send_msg(udp_socket, target_ip):
    global send_data,m,tank2_posx,tank2_posy
    while True:

        if send_data:
            temp = str(send_data)+str(tank2_posx)+"|"+str(tank2_posy)
            #print(send_data)
            udp_socket.sendto(bytes(temp.encode("utf-8")), target_ip)
            send_data=None
        time.sleep(0.015)


def who_win_game():
    pass


def tank1_control_event(settings, tank1, bullets, screen,sound_shoot):
    global n, get_data,tank1_posx,tank1_posy
    move = pygame.mixer.Sound("music//move.wav")
    move.set_volume(0.1)

    if get_data == "left":  #
        move.play()
        tank1.img = pygame.image.load("坦克4.png")
        n = 4
        tank1.rect.centerx = tank1_posx
        time.sleep(0.015)
        move.stop()
        if tank1.rect.centerx < 30:
            tank1.rect.centerx = tank1.screen_rect.left
        get_data = None
    elif get_data == "right":
        move.play()
        tank1.img = pygame.image.load("坦克2.png")
        tank1.rect.centerx = tank1_posx
        n = 2
        time.sleep(0.015)
        move.stop()
        if tank1.rect.centerx > 960:
            tank1.rect.centerx = tank1.screen_rect.right
        get_data = None
    elif get_data == "up":  # 如果按键按下，这个值为1
        move.play()
        tank1.img = pygame.image.load("坦克1.png")
        n = 1
        tank1.rect.centery = tank1_posy
        time.sleep(0.015)
        move.stop()
        if tank1.rect.centery < 0:
            tank1.rect.centery = tank1.screen_rect.bottom
        get_data = None
    elif get_data == "down":  # 如果按键按下，这个值为1
        move.play()
        tank1.img = pygame.image.load("坦克3.png")
        n = 3
        tank1.rect.centery = tank1_posy
        time.sleep(0.015)
        move.stop()
        if tank1.rect.centery > 590:
            tank1.rect.centery = tank1.screen_rect.top
        get_data = None
    elif get_data == "LEFT":
            n = 4
            print("444")
            new_bullet = Bull.Bullet(settings, screen, tank1, (60, 60, 60), n)
            bullets.add(new_bullet)

            n=0
            get_data=None
            sound_shoot.play()
            time.sleep(0.015)
            sound_shoot.stop()
    elif get_data == "RIGHT":
            n = 2
            print("2222")
            new_bullet = Bull.Bullet(settings, screen, tank1, (60, 60, 60), n)
            bullets.add(new_bullet)

            n=0
            get_data = None
            sound_shoot.play()
            time.sleep(0.015)
            sound_shoot.stop()
    elif get_data == "UP":
            n = 1
            print("1111")
            new_bullet = Bull.Bullet(settings, screen, tank1, (60, 60, 60), n)
            bullets.add(new_bullet)

            n=0
            get_data = None
            sound_shoot.play()
            time.sleep(0.015)
            sound_shoot.stop()
    elif get_data=="DOWN":
            n = 3
            print("3333")
            new_bullet = Bull.Bullet(settings, screen, tank1, (60, 60, 60),n)
            bullets.add(new_bullet)
            n = 0
            get_data = None
            sound_shoot.play()
            time.sleep(0.015)
            sound_shoot.stop()



def tank2_control_event(settings, tank2, bullets, screen, shoot_sound):
    global m,send_data,tank2_posx,tank2_posy
    move = pygame.mixer.Sound("music//move.wav")
    move.set_volume(0.1)
    mykeyslist = pygame.key.get_pressed()  # 获取按键元组信息
    if mykeyslist[pygame.K_a]:  # 如果按键按下，这个值为1
        move.play()

        tank2.img = pygame.image.load("坦克_4.png")
        m=4
        send_data= "left|"


        tank2.rect.centerx = tank2.rect.centerx - settings.tank_speed
        tank2_posx = tank2.rect.centerx
        if tank2.rect.centerx < 30:
            tank2.rect.centerx = tank2.screen_rect.left
    elif mykeyslist[pygame.K_d]:  # 如果按键按下，这个值为1
        move.play()
        tank2.img = pygame.image.load("坦克_2.png")
        tank2.rect.centerx = tank2.rect.centerx + settings.tank_speed
        tank2_posx = tank2.rect.centerx
        m = 2
        send_data = "right|"
        if tank2.rect.centerx > 960:
            tank2.rect.centerx = tank2.screen_rect.right
    elif mykeyslist[pygame.K_w]:  # 如果按键按下，这个值为1
        move.play()
        tank2.img = pygame.image.load("坦克_1.png")
        m = 1
        send_data = "up|"
        tank2.rect.centery = tank2.rect.centery - settings.tank_speed
        tank2_posy = tank2.rect.centery
        if tank2.rect.centery < 0:
            tank2.rect.centery = tank2.screen_rect.bottom
    elif mykeyslist[pygame.K_s]:  # 如果按键按下，这个值为1
        move.play()
        tank2.img = pygame.image.load("坦克3.png")
        m = 3
        send_data = "down|"
        tank2.rect.centery = tank2.rect.centery + settings.tank_speed
        tank2_posy = tank2.rect.centery
        if tank2.rect.centery > 590:
            tank2.rect.centery = tank2.screen_rect.top
    elif mykeyslist[pygame.K_SPACE]:

        if len(bullets) < settings.bullet_allow_num:
            if m==4:
                send_data = "LEFT|"
                new_bullet = Bull.Bullet(settings, screen, tank2, (120, 120, 120), m)
                bullets.add(new_bullet)
                shoot_sound.play()
            if m==2:
                send_data = "RIGHT|"
                new_bullet = Bull.Bullet(settings, screen, tank2, (120, 120, 120), m)
                bullets.add(new_bullet)
                shoot_sound.play()
            if m==1:
                send_data = "UP|"
                new_bullet = Bull.Bullet(settings, screen, tank2, (120, 120, 120), m)
                bullets.add(new_bullet)
                shoot_sound.play()
            if m==3:
                send_data = "DOWN|"
                new_bullet = Bull.Bullet(settings, screen, tank2, (120, 120, 120), m)
                bullets.add(new_bullet)
                shoot_sound.play()
            else:
                pass

    else:
        pass



def game_button(button1, button2, button3):
    '''
    进入主界面，点击
                开始游戏-1
                游戏设置-2
                游戏帮助-3
                进入到游戏当中1
                进入到游戏设置里2
                进入到游戏帮助里3
                界面不动0

    '''
    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button1.rect.collidepoint(mouse_x, mouse_y):
                return -1
            if button2.rect.collidepoint(mouse_x, mouse_y):
                return -2
            if button3.rect.collidepoint(mouse_x, mouse_y):
                return -3
    return 0


def settings_mode_ui(settings, button1, button2, button3, button4, button5, button6):
    '''
    进入游戏设置，点击
                炮弹速度1
                炮弹速度2
                炮弹速度3
                坦克速度4
                坦克速度5
                坦克速度6
                界面不动0

    '''
    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button1.rect.collidepoint(mouse_x, mouse_y):
                settings.bullet_speed = 1
                return 1
            if button2.rect.collidepoint(mouse_x, mouse_y):
                settings.bullet_speed = 2
                return 2
            if button3.rect.collidepoint(mouse_x, mouse_y):
                settings.bullet_speed = 3
                return 3
            if button4.rect.collidepoint(mouse_x, mouse_y):
                settings.tank_speed = 1
                return 4
            if button5.rect.collidepoint(mouse_x, mouse_y):
                settings.tank_speed = 2
                return 5
            if button6.rect.collidepoint(mouse_x, mouse_y):
                settings.tank_speed = 3
                return 6

    return -1


def end_help(button):
    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button.rect.collidepoint(mouse_x, mouse_y):
                return 1
    return -1


def run_game():
    global tank1_posx,tank2_posx,tank1_posy,tank2_posy
    pygame.init()
    setinit = Game_Settings.Settings_of_Show()
    screen = pygame.display.set_mode((setinit.screen_width, setinit.screen_height))

    pygame.display.set_caption("联机坦克大战")
    tank1 = Tank.Tank1(screen)
    tank2 = Tank.Tank2(screen)
    bullets1 = Group()
    bullets2 = Group()

    start_button = Button.Button(screen, 80, 40, (0, 255, 0), (255, 255, 255), "开始游戏", (500, 200))
    settings_button = Button.Button(screen, 80, 40, (164, 247, 151), (255, 255, 255), "游戏设置", (500, 300))
    help_button = Button.Button(screen, 80, 40, (105, 194, 49), (255, 255, 255), "游戏帮助", (500, 400))
    game_settings = Game_Settings.Settings(tank_speed=5, bullet_speed=1, bullet_allow_num=1)

    bullet_speed1 = Button.Button(screen, 80, 40, (164, 247, 151), (255, 255, 255), "炮弹速度1", (200, 150))
    bullet_speed2 = Button.Button(screen, 80, 40, (164, 247, 151), (255, 255, 255), "炮弹速度2", (500, 150))
    bullet_speed3 = Button.Button(screen, 80, 40, (164, 247, 151), (255, 255, 255), "炮弹速度3", (800, 150))
    tank_speed1 = Button.Button(screen, 80, 40, (164, 247, 151), (255, 255, 255), "坦克速度1", (200, 300))
    tank_speed2 = Button.Button(screen, 80, 40, (164, 247, 151), (255, 255, 255), "坦克速度2", (500, 300))
    tank_speed3 = Button.Button(screen, 80, 40, (164, 247, 151), (255, 255, 255), "坦克速度3", (800, 300))
    login_name_input = TextBox.TextBox(screen,None,None,20,"microsoftyaheimicrosoftyaheiuibold",(0,0,0),(255,255,255),(500,300),"输入用户名")
    password_input = TextBox.TextBox(screen, None, None, 20, "microsoftyaheimicrosoftyaheiuibold", (0, 0, 0), (255, 255, 255), (500, 300), "输入密码")

    sound_shoot = pygame.mixer.Sound("music//shoot.wav")
    '''
    flag=None
    login_name = "wsde"
    while flag!=login_name:
        screen.fill(setinit.bg_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                flag = login_name_input.key_down_text(event)
                print(flag)
        login_name_input.draw_textbox()
        pygame.display.flip()

    flag = None
    password: str = "ff"
    print(password)
    while flag != password:
        screen.fill(setinit.bg_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                flag= password_input.key_down_text(event)

        password_input.draw_textbox()

        pygame.display.flip()

    print("!!!!!!!")
    '''
    # 游戏主界面
    while True:

        screen.fill(setinit.bg_color)
        flag = game_button(start_button, settings_button, help_button)
        if flag == 0:
            settings_button.draw()

            start_button.draw()

            help_button.draw()


        if flag == -1:
            pygame.display.flip()
            screen.fill(setinit.bg_color)
            print("-1")

            pygame.display.flip()
            print(game_settings.tank_speed, game_settings.bullet_speed)
            score_of_two = Score.Score(screen, tank1, tank2, bullets1, bullets2, setinit)
            # 进入游戏
            main_flag = False

            while not main_flag:

                screen.fill(setinit.bg_color)
                score_of_two.score_change()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                tank2_control_event(game_settings, tank2, bullets2, screen, sound_shoot)
                tank1_control_event(game_settings, tank1, bullets1, screen, sound_shoot)


                score_of_two.score_draw()

                for i in bullets1.copy():
                    if i.rect.centerx <= 0 or i.rect.centerx >= 1000:
                        bullets1.remove(i)
                    elif i.rect.centery >= 600 or i.rect.centery <= 0:
                        bullets1.remove(i)
                for i in bullets1.sprites():
                    i.draw_bull()

                for i in bullets2.copy():
                    if i.rect.centerx <= 0 or i.rect.centerx >= 1000:
                        bullets2.remove(i)
                    elif i.rect.centery >= 600 or i.rect.centery <= 0:
                        bullets2.remove(i)
                for i in bullets2.sprites():
                    i.draw_bull()
                update_screen(tank1, bullets1, tank2, bullets2)
                main_flag = score_of_two.who_win()
                pygame.display.flip()
            score_of_two.who_win()
            time.sleep(10)
        if flag == -2:
            pygame.display.flip()
            screen.fill(setinit.bg_color)
            # print("-2")
            temp_settings = -1
            while True:
                # print("1")

                if temp_settings == -1:
                    screen.fill(setinit.bg_color)
                    # print("设定难度")
                    bullet_speed1.draw()
                    bullet_speed2.draw()
                    bullet_speed3.draw()
                    tank_speed1.draw()
                    tank_speed2.draw()
                    tank_speed3.draw()

                    temp_settings: int = settings_mode_ui(game_settings, bullet_speed1, bullet_speed2, bullet_speed3,
                                                          tank_speed1,
                                                          tank_speed2, tank_speed3)
                    pygame.display.flip()

                # print(temp_settings)
                if temp_settings == 1:
                    screen.fill(setinit.bg_color)
                    print(temp_settings)
                    break
                if temp_settings == 2:
                    screen.fill(setinit.bg_color)
                    print(temp_settings)
                    break
                if temp_settings == 3:
                    screen.fill(setinit.bg_color)
                    print(temp_settings)
                    break
                if temp_settings == 4:
                    screen.fill(setinit.bg_color)
                    print(temp_settings)
                    break
                if temp_settings == 5:
                    screen.fill(setinit.bg_color)
                    print(temp_settings)
                    break
                if temp_settings == 6:
                    screen.fill(setinit.bg_color)
                    print(temp_settings)
                    break

        if flag == -3:
            pygame.display.flip()
            screen.fill(setinit.bg_color)
            # print("-2")
            help_flag = -1
            jump_end_button = Button.Button(screen, 40, 50, (164, 247, 151), (255, 255, 255), "结束", (800, 300))
            while True:
                if help_flag == -1:
                    screen.fill(setinit.bg_color)
                    font = pygame.font.SysFont("microsoftyaheimicrosoftyaheiuibold", 20)
                    text = font.render("服务器端上线后，客户端才可以登录",
                                       True, (255, 255, 255), (0, 255, 0))
                    text_rect = text.get_rect()
                    text_rect.center = screen.get_rect().center
                    screen.blit(text, text_rect)
                    jump_end_button.draw()
                    help_flag = end_help(jump_end_button)
                    pygame.display.flip()
                if help_flag == 1:
                    break

        pygame.display.flip()

t1 = threading.Thread(target=recv_msg, args=(udp_socket,))
t2 = threading.Thread(target=send_msg, args=(udp_socket, target_ip,))
t3 = threading.Thread(target=run_game)

t3.start()

t1.start()
t2.start()



