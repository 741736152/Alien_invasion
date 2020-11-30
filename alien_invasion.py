import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from Alien import Alien
def run_game():
    # 初始化游戏并且创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(screen, ai_settings)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人
    alien = Alien(ai_settings, screen)

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)     # 鼠标键盘 事件管理
        ship.update()   # 更新飞船移动位置
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)    # 更新屏幕
run_game()