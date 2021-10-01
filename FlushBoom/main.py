import sys
import pygame
from pygame.color import THECOLORS

# 只有位置不变的按钮才有pos
# 只有按钮才有size
# size不考虑阴影，pos考虑阴影

global background  # 背景
global title  # 标题
global rule  # 规则
global plat_rule  # 规则放置区
global txt_volume  # “音量”
global txt_open_recorder  # “开启记牌器”

global tag_gamer_A  # 玩家A标牌
global tag_gamer_B  # 玩家B标牌
global tag_AI  # AI标牌
global tag_cards_in_hand  # 手牌区
global tag_deck  # 牌堆区
global tag_deck_sign  # 牌堆区标志
global tag_deck_amount  # 牌堆区数量
global tag_placement_area  # 放置区
global tag_placement_area_amount  # 放置区数量
global tag_placement_area_sign  # 放置区标志
global tag_S_amount  # 黑桃数量标牌
global tag_H_amount  # 红心数量标牌
global tag_C_amount  # 梅花数量标牌
global tag_D_amount  # 方块数量标牌


global button_game_start  # 按钮：开始游戏
global pos_game_start
global size_game_start
global button_game_rule  # 按钮：游戏规则
global pos_game_rule
global size_game_rule
global button_game_setting  # 按钮：游戏设置
global pos_game_setting
global size_game_setting
global button_game_quit  # 按钮：退出游戏
global pos_game_quit
global size_game_quit
global button_return  # 按钮：返回
global size_return
global button_local_match  # 按钮：本地对战
global pos_local_match
global size_local_match
global button_AI_match  # 按钮：人机对战
global pos_AI_match
global size_AI_match
global button_online_match  # 按钮：联机对战
global pos_online_match
global size_online_match

global size_shadow  # 按钮阴影大小

global screen  # 窗口
global w
global h

global fps  # 帧率
global fps_clock  # 可以操作时间的对象

global cards  # 卡牌
global card_images  # 卡牌图片
global card_sounds  # 卡牌语音
global card_back  # 卡牌背面


# ====================pygame相关初始化开始==================== #
# pygame初始化
pygame.init()
# pygame.mixer初始化
pygame.mixer.init()
# ====================pygame相关初始化结束==================== #

# ====================窗口设置开始==================== #
# 窗口大小
w = 1080
h = 720
screen = pygame.display.set_mode([w, h])

# 屏幕帧率设置
fps = 60  # 每秒60帧
fps_clock = pygame.time.Clock()  # 用 pygame.time.Clock()创建一个可以操作时间的对象

# 程序名
pygame.display.set_caption("同花Boom")
# 程序图标
icon = pygame.image.load('./images/' + '标志.jpg')
pygame.display.set_icon(icon)
# ====================窗口设置结束==================== #

# ====================导入资源开始==================== #
# 导入背景
background = pygame.image.load('./images/' + '背景.jpg')
# 导入标题
title = pygame.image.load('./images/' + '标题.jpg')
# 导入规则
rule = pygame.image.load('./images/tags/' + '规则.jpg')
# 导入规则放置区
plat_rule = pygame.image.load('./images/tags/' + '规则放置区.jpg')
# 导入“音量”
txt_volume = pygame.image.load('./images/tags/' + '音量.jpg')
# 导入“开启记牌器”
txt_open_recorder = pygame.image.load('./images/tags/' + '开启记牌器.jpg')

# 导入 玩家A标牌
tag_gamer_A = pygame.image.load('./images/tags/' + '玩家A标牌.jpg')
# 导入 玩家B标牌
tag_gamer_B = pygame.image.load('./images/tags/' + '玩家B标牌.jpg')
# 导入 AI标牌
tag_AI = pygame.image.load('./images/tags/' + 'AI标牌.jpg')
# 导入 手牌区
tag_cards_in_hand = pygame.image.load('./images/tags/' + '手牌区.jpg')
# 导入 牌堆区
tag_deck = pygame.image.load('./images/tags/' + '牌堆.jpg')
# 导入 牌堆区标志
tag_deck_sign = pygame.image.load('./images/tags/' + '牌堆标牌.jpg')
# 导入 牌堆区数量
tag_deck_amount = pygame.image.load('./images/tags/' + '牌堆数量标牌.jpg')
# 导入 放置区
tag_placement_area = pygame.image.load('./images/tags/' + '放置区.jpg')
# 导入 放置区数量
tag_placement_area_amount = pygame.image.load('./images/tags/' + '放置区数量标牌.jpg')
# 导入 放置区标志
tag_placement_area_sign = pygame.image.load('./images/tags/' + '放置区标牌.jpg')
# 导入 黑桃数量标牌
tag_S_amount = pygame.image.load('./images/tags/' + '黑桃数量标牌.jpg')
# 导入 红心数量标牌
tag_H_amount = pygame.image.load('./images/tags/' + '红心数量标牌.jpg')
# 导入 梅花数量标牌
tag_C_amount = pygame.image.load('./images/tags/' + '梅花数量标牌.jpg')
# 导入 方块数量标牌
tag_D_amount = pygame.image.load('./images/tags/' + '方块数量标牌.jpg')

# 导入 按钮：开始游戏
button_game_start = pygame.image.load('./images/tags/' + '开始游戏.jpg')
size_game_start = (220, 76)
pos_game_start = (405, 250)
# 导入 按钮：游戏规则
button_game_rule = pygame.image.load('./images/tags/' + '游戏规则.jpg')
size_game_rule = (220, 76)
pos_game_rule = (405, 351)
# 导入 按钮：游戏设置
button_game_setting = pygame.image.load('./images/tags/' + '游戏设置.jpg')
size_game_setting = (220, 76)
pos_game_setting = (405, 452)
# 导入 按钮：退出游戏
button_game_quit = pygame.image.load('./images/tags/' + '退出游戏.jpg')
size_game_quit = (220, 76)
pos_game_quit = (405, 553)
# 导入 按钮：返回
button_return = pygame.image.load('./images/tags/' + '返回.jpg')
size_return = (157, 61)
# 导入 按钮：本地对战
button_local_match = pygame.image.load('./images/tags/' + '本地对战.jpg')
pos_local_match = (405, 282)
size_local_match = (220, 76)
# 导入 按钮：人机对战
button_AI_match = pygame.image.load('./images/tags/' + '人机对战.jpg')
pos_AI_match = (405, 391)
size_AI_match = (220, 76)
# 导入 按钮：联机对战
button_online_match = pygame.image.load('./images/tags/' + '联机对战.jpg')
pos_online_match = (405, 500)
size_online_match = (220, 76)

# 设置按钮阴影大小
size_shadow = (25, 25)

# ====================导入资源结束==================== #

# ====================卡牌设置开始==================== #
# 导入卡牌图片（包括大小王）
card_images = [pygame.image.load('./images/' + '1.jpg')]  # 卡牌图片初始化
for i in range(1, 55):
    card_images.append(pygame.image.load('./images/' + str(i) + '.jpg'))
# 导入卡牌背面
card_back = pygame.image.load('./images/' + 'card_back.jpg')

# 导入卡牌语音（包括大小王）
card_sounds = [pygame.mixer.Sound('./sounds/' + '1.wav')]  # 卡牌语音初始化
for i in range(1, 16):
    card_sounds.append(pygame.mixer.Sound('./sounds/' + str(i) + '.wav'))


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


# 栈
class Stack(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self, item):
        return self.items.pop()


# 建立卡牌
cards = [CARD()]
for i in range(1, 14):
    cards.append(CARD(i, 'S', card_images[i], card_sounds[i]))
for i in range(14, 27):
    cards.append(CARD(i - 13, 'H', card_images[i], card_sounds[i - 13]))
for i in range(27, 40):
    cards.append(CARD(i - 26, 'C', card_images[i], card_sounds[i - 26]))
for i in range(40, 53):
    cards.append(CARD(i - 39, 'D', card_images[i], card_sounds[i - 39]))
for i in range(53, 55):
    cards.append(CARD(i - 39, 'K', card_images[i], card_sounds[i - 39]))
# ====================卡牌设置结束==================== #


# 开始菜单
def page_start_menu():
    # 转到开始菜单界面
    screen.blit(background, (0, 0))  # 插入背景
    screen.blit(title, (318, 108))  # 插入标题
    screen.blit(button_game_start, pos_game_start)  # 插入按钮：开始游戏
    screen.blit(button_game_rule, pos_game_rule)  # 插入按钮：游戏规则
    screen.blit(button_game_setting, pos_game_setting)  # 插入按钮：游戏设置
    screen.blit(button_game_quit, pos_game_quit)  # 插入按钮：退出游戏
    # 刷新屏幕
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                continue  # 是鼠标移动事件则跳到下一个事件

            if event.type == pygame.QUIT:  # 点击关闭窗口
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:  # 点击事件
                if event.button == 1:  # 左键点击
                    if event.pos[0] in range(pos_game_start[0] + size_shadow[0],
                                             pos_game_start[0] + size_shadow[0] + size_game_start[0]) \
                            and event.pos[1] in range(pos_game_start[1] + size_shadow[1],
                                                      pos_game_start[1] + size_shadow[1] + size_game_start[1]):
                        print('动作：点击按钮【开始游戏】')
                        page_game_start()
                    elif event.pos[0] in range(pos_game_rule[0] + size_shadow[0],
                                               pos_game_rule[0] + size_shadow[0] + size_game_rule[0]) \
                            and event.pos[1] in range(pos_game_rule[1] + size_shadow[1],
                                                      pos_game_rule[1] + size_shadow[1] + size_game_rule[1]):
                        print('动作：点击按钮【游戏规则】')
                        page_game_rule()
                    elif event.pos[0] in range(pos_game_setting[0] + size_shadow[0],
                                               pos_game_setting[0] + size_shadow[0] + size_game_setting[0]) \
                            and event.pos[1] in range(pos_game_setting[1] + size_shadow[1],
                                                      pos_game_setting[1] + size_shadow[1] + size_game_setting[1]):
                        print('动作：点击按钮【游戏设置】')
                        page_game_setting()
                    elif event.pos[0] in range(pos_game_quit[0] + size_shadow[0],
                                               pos_game_quit[0] + size_shadow[0] + size_game_quit[0]) \
                            and event.pos[1] in range(pos_game_quit[1] + size_shadow[1],
                                                      pos_game_quit[1] + size_shadow[1] + size_game_quit[1]):
                        print('动作：点击按钮【退出游戏】')
                        page_game_quit()

                    # 转到开始菜单界面
                    screen.blit(background, (0, 0))  # 插入背景
                    screen.blit(title, (318, 108))  # 插入标题
                    screen.blit(button_game_start, pos_game_start)  # 插入按钮：开始游戏
                    screen.blit(button_game_rule, pos_game_rule)  # 插入按钮：游戏规则
                    screen.blit(button_game_setting, pos_game_setting)  # 插入按钮：游戏设置
                    screen.blit(button_game_quit, pos_game_quit)  # 插入按钮：退出游戏
                    # 刷新屏幕
                    pygame.display.flip()

        fps_clock.tick(fps)


# 开始游戏（选择模式：本地对战；人机对战；联机对战）
def page_game_start():
    # 转到开始游戏（选择模式：本地对战；人机对战；联机对战）界面
    screen.blit(background, (0, 0))  # 插入背景
    screen.blit(title, (318, 108))  # 插入标题
    screen.blit(button_return, (849, 605))  # 插入返回按钮
    screen.blit(button_local_match, pos_local_match)  # 插入“本地对战”按钮
    screen.blit(button_AI_match, pos_AI_match)  # 插入“AI对战”按钮
    screen.blit(button_online_match, pos_online_match)  # 插入“联机对战”按钮
    # 刷新屏幕
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                continue  # 是鼠标移动事件则跳到下一个事件

            if event.type == pygame.QUIT:  # 点击关闭窗口
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:  # 点击事件
                if event.button == 1:  # 左键点击
                    if event.pos[0] in range(874, 874 + size_return[0]) \
                            and event.pos[1] in range(630, 630 + size_return[1]):
                        print('动作：点击按钮【返回】')
                        return
                    elif event.pos[0] in range(pos_local_match[0] + size_shadow[0],
                                               pos_local_match[0] + size_shadow[0] + size_local_match[0]) \
                            and event.pos[1] in range(pos_local_match[1] + size_shadow[1],
                                                      pos_local_match[1] + size_shadow[1] + size_local_match[1]):
                        print('动作：点击按钮【本地对战】')
                        local_match()
                    elif event.pos[0] in range(pos_AI_match[0] + size_shadow[0],
                                               pos_AI_match[0] + size_shadow[0] + size_local_match[0]) \
                            and event.pos[1] in range(pos_AI_match[1] + size_shadow[1],
                                                      pos_AI_match[1] + size_shadow[1] + size_AI_match[1]):
                        print('动作：点击按钮【人机对战】')
                        ai_match()
                    elif event.pos[0] in range(pos_online_match[0] + size_shadow[0],
                                               pos_online_match[0] + size_shadow[0] + size_online_match[0]) \
                            and event.pos[1] in range(pos_online_match[1] + size_shadow[1],
                                                      pos_online_match[1] + size_shadow[1] + size_online_match[1]):
                        print('动作：点击按钮【联机对战】')
                        online_match()

                    # 转到开始游戏（选择模式：本地对战；人机对战；联机对战）界面
                    screen.blit(background, (0, 0))  # 插入背景
                    screen.blit(title, (318, 108))  # 插入标题
                    screen.blit(button_return, (849, 605))  # 插入返回按钮
                    screen.blit(button_local_match, pos_local_match)  # 插入“本地对战”按钮
                    screen.blit(button_AI_match, pos_AI_match)  # 插入“AI对战”按钮
                    screen.blit(button_online_match, pos_online_match)  # 插入“联机对战”按钮
                    # 刷新屏幕
                    pygame.display.flip()

        fps_clock.tick(fps)


# 游戏规则：
def page_game_rule():
    # 转到游戏规则界面
    screen.blit(background, (0, 0))  # 插入背景
    screen.blit(title, (318, 12))  # 插入标题
    screen.blit(plat_rule, (67, 113))  # 插入规则放置区
    screen.blit(rule, (141, 134))  # 插入规则
    screen.blit(button_return, (872, -7))  # 插入返回按钮
    # 刷新屏幕
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                continue  # 是鼠标移动事件则跳到下一个事件

            if event.type == pygame.QUIT:  # 点击关闭窗口
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:  # 点击事件
                if event.button == 1:  # 左键点击
                    if event.pos[0] in range(897, 897 + size_return[0]) \
                            and event.pos[1] in range(18, 18 + size_return[1]):
                        print('动作：点击按钮【返回】')
                        return
        fps_clock.tick(fps)


# 游戏设置：
def page_game_setting():
    # 转到游戏设置界面
    screen.blit(background, (0, 0))  # 插入背景
    screen.blit(title, (318, 108))  # 插入标题
    screen.blit(button_return, (849, 605))  # 插入返回按钮
    screen.blit(txt_volume, (222, 327))  # 插入“音量”
    screen.blit(txt_open_recorder, (156, 421))  # 插入“开启记牌器”
    # 刷新屏幕
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                continue  # 是鼠标移动事件则跳到下一个事件

            if event.type == pygame.QUIT:  # 点击关闭窗口
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:  # 点击事件
                if event.button == 1:  # 左键点击
                    if event.pos[0] in range(874, 874 + size_return[0]) \
                            and event.pos[1] in range(630, 630 + size_return[1]):
                        print('动作：点击按钮【返回】')
                        return
        fps_clock.tick(fps)


# 退出游戏：
def page_game_quit():
    sys.exit()


def local_match():
    turn = 1  # 0表示A回合，1表示B回合
    deck = range(1, 53)  # 牌堆，仅保存下标（因为随机）
    placement_area = Stack()  # 放置区
    cards_in_hand = []
    for index in range(0, 8):
        cards_in_hand.append(Stack())  # 初始化手牌，0~3是A的手牌，4~7是B的手牌

    # 转到本地对战
    screen.blit(background, (0, 0))  # 插入背景
    screen.blit(button_return, (872, -7))  # 插入返回按钮
    screen.blit(tag_gamer_A, (190, 419))  # 玩家A标牌
    screen.blit(tag_gamer_B, (190, 5))  # 玩家B标牌
    screen.blit(tag_cards_in_hand, (190, 472))  # 手牌区
    screen.blit(tag_deck, (303, 190))  # 牌堆区
    screen.blit(tag_deck_sign, (338, 392))  # 牌堆区标志
    screen.blit(tag_deck_amount, (337, 155))  # 牌堆区数量
    screen.blit(tag_placement_area, (628, 190))  # 放置区
    screen.blit(tag_placement_area_amount, (662, 153))  # 放置区数量
    screen.blit(tag_placement_area_sign, (663, 392))  # 放置区标志
    screen.blit(tag_S_amount, (252, 478))  # A-黑桃数量标牌
    screen.blit(tag_H_amount, (414, 478))  # A-红心数量标牌
    screen.blit(tag_C_amount, (577, 478))  # A-梅花数量标牌
    screen.blit(tag_D_amount, (739, 478))  # A-方块数量标牌

    screen.blit(tag_S_amount, (252, 60))  # B-黑桃数量标牌
    screen.blit(tag_H_amount, (414, 60))  # B-红心数量标牌
    screen.blit(tag_C_amount, (577, 60))  # B-梅花数量标牌
    screen.blit(tag_D_amount, (739, 60))  # B-方块数量标牌

    # 展示当前场上卡牌状况
    if turn == 1: turn = 0
    else: turn = 1
    # 展示牌堆
    if len(deck) > 0:
        screen.blit(card_back, (326, 213))  # 牌堆顶是卡牌背面（即不展示）
    # 展示放置区
    for index in range(turn * 4 + 0, turn * 4 + 3):
        if not cards_in_hand[index].is_empty():
            if index % 4 == 0:
                screen.blit(cards_in_hand[index].peek().card_image, (244, 521))
            elif index % 4 == 1:
                screen.blit(cards_in_hand[index].peek().card_image, (406, 521))
            elif index % 4 == 2:
                screen.blit(cards_in_hand[index].peek().card_image, (569, 521))
            elif index % 4 == 3:
                screen.blit(cards_in_hand[index].peek().card_image, (731, 521))

    # 刷新屏幕
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                continue  # 是鼠标移动事件则跳到下一个事件

            if event.type == pygame.QUIT:  # 点击关闭窗口
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:  # 点击事件
                if event.button == 1:  # 左键点击
                    if event.pos[0] in range(897, 897 + size_return[0]) \
                            and event.pos[1] in range(18, 18 + size_return[1]):
                        print('动作：点击按钮【返回】')
                        return
                    elif event.pos[0] in range(326, 326 + 105) and event.pos[1] in range(213, 213 + 150):
                        print('动作：从【牌堆】抽牌', )
                    elif event.pos[0] in range(244, 244 + 105) and event.pos[1] in range(521, 521 + 150):
                        print('动作：从【手牌】抽牌，【黑桃】')
                    elif event.pos[0] in range(406, 406 + 105) and event.pos[1] in range(521, 521 + 150):
                        print('动作：从【手牌】抽牌，【红心】')
                    elif event.pos[0] in range(569, 569 + 105) and event.pos[1] in range(521, 521 + 150):
                        print('动作：从【手牌】抽牌，【梅花】')
                    elif event.pos[0] in range(731, 731 + 105) and event.pos[1] in range(521, 521 + 150):
                        print('动作：从【手牌】抽牌，【方块】')

        fps_clock.tick(fps)


def ai_match():
    pass


def online_match():
    pass


if __name__ == '__main__':
    # 开始菜单
    page_start_menu()
