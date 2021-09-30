import pygame
from pygame.color import THECOLORS

global window  # 窗口
global background  # 背景
global title  # 标题
global fps  # 帧率
global f_clock  # 可以操作时间的对象
global cards  # 卡牌
global card_images  # 卡牌图片
global card_sounds  # 卡牌语音

# ====================pygame相关初始化开始==================== #
# pygame初始化
pygame.init()
# pygame.mixer初始化
pygame.mixer.init()
# ====================pygame相关初始化结束==================== #


# 卡牌类
class CARD:
    # 黑桃：S
    # 红心：H
    # 梅花：C
    # 方块：D
    # 大小王：K
    def __init__(self, card_value=1, card_type='S',
                 card_image=pygame.image.load('./images/' + '1.jpg'),
                 card_sound=pygame.mixer.Sound('./sounds/' + '1.wav')):
        self.card_value = card_value  # 卡牌数值
        self.card_type = card_type    # 卡牌花色
        self.card_image = card_image  # 卡牌图片
        self.card_sound = card_sound  # 卡牌声音


# 开始菜单：
#   开始游戏：
#     本地对战：
#     人机对战：
#     联机对战：
#   游戏规则：
#   游戏设置：
#   退出游戏：


# 开始菜单
def page_start_menu():

    # 转到开始菜单界面
    window.blit(background, [0, 0])

    # 刷新屏幕
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


# 开始游戏
def page_game_start():
    pass


# 游戏规则：
def page_game_rule():
    pass


# 游戏设置：
def page_game_setting():
    pass


# 退出游戏：
def page_game_quit():
    pass


# 初始化
def init():
    global window  # 窗口
    global background  # 背景
    global title  # 标题
    global fps  # 帧率
    global f_clock  # 可以操作时间的对象
    global cards  # 卡牌
    global card_images  # 卡牌图片
    global card_sounds  # 卡牌语音


# ====================窗口设置开始==================== #
    # 窗口大小
    w = 1080
    h = 720
    window = pygame.display.set_mode([w, h])

    # 屏幕帧率设置
    fps = 60  # 每秒60帧
    f_clock = pygame.time.Clock()  # 用 pygame.time.Clock()创建一个可以操作时间的对象

    # 程序名
    pygame.display.set_caption("同花Boom")

    # 程序图标
    icon = pygame.image.load('./images/' + '标志.jpg')
    pygame.display.set_icon(icon)

    # 导入背景
    background = pygame.image.load('./images/' + '背景.jpg')

    # 导入标题
    title = pygame.image.load('./images/' + '标题.jpg')
# ====================窗口设置结束==================== #

# ====================卡牌设置开始==================== #
    # 导入卡牌图片（包括大小王）
    card_images = [pygame.image.load('./images/' + '1.jpg')]  # 卡牌图片初始化
    for i in range(1, 54):
        card_images.append(pygame.image.load('./images/' + str(i) + '.jpg'))

    # 导入卡牌语音（包括大小王）
    card_sounds = [pygame.mixer.Sound('./sounds/' + '1.wav')]  # 卡牌语音初始化
    for i in range(1, 15):
        card_sounds.append(pygame.mixer.Sound('./sounds/' + str(i) + '.wav'))

    # 建立卡牌
    cards = [CARD()]
    for i in range(1, 13):
        cards.append(CARD(i, 'S', card_images[i], card_sounds[i]))
    for i in range(14, 26):
        cards.append(CARD(i - 13, 'H', card_images[i], card_sounds[i - 13]))
    for i in range(27, 39):
        cards.append(CARD(i - 26, 'C', card_images[i], card_sounds[i - 26]))
    for i in range(40, 52):
        cards.append(CARD(i - 39, 'D', card_images[i], card_sounds[i - 39]))
    for i in range(53, 54):
        cards.append(CARD(i - 39, 'K', card_images[i], card_sounds[i - 39]))
# ====================卡牌设置结束==================== #


if __name__ == '__main__':

    # 初始化
    init()

    # 开始菜单
    page_start_menu()
