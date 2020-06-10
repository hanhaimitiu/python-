class Settings_of_Show():
    def __init__(self):
        self.screen_width = 1000

        self.screen_height =600
        self.bg_color = (230,230,230)

class Settings():
    def __init__(self,tank_speed,bullet_speed,bullet_allow_num):
        self.tank_speed = tank_speed
        self.bullet_speed = bullet_speed
        self.bullet_width = 5
        self.bullet_height = 5

        self.bullet_allow_num = bullet_allow_num