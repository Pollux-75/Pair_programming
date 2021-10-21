import random
import sys
import time

import pygame
import requests
import json

import socket
import os
import get
# 只有位置不变的按钮才有pos
# 只有按钮才有size
# size不考虑阴影，pos考虑阴影

global background  # 背景
global title  # 标题
global rule  # 规则
global plat_rule  # 规则放置区
global txt_volume  # “音量”
global txt_open_recorder  # “开启记牌器”
global use_card_recorder  # 是否开启记牌器的变量
global image_card_recorder_switch_on  # 打开记牌器开关的图片
global image_card_recorder_switch_off  # 关闭记牌器开关的图片

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

global tag_A_turn  # A的回合标牌
global tag_B_turn  # B的回合标牌
global tag_AI_turn  # AI回合标牌
global tag_turn  # 轮换标牌
global tag_A_win  # A胜利标牌
global tag_B_win  # B胜利标牌
global tag_AI_win  # AI胜利标牌
global tag_flush_boom  # 同花BOOM标牌
global tag_safe_play  # 安全出牌标牌
global tag_wait_play  # 等待出牌标牌
global tag_from_hand  # 手牌出牌标牌
global tag_from_deck  # 牌堆出牌标牌
global tag_equal  # 平局标牌

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

# 背景音乐
# pygame.mixer.music.load('./sounds/' + 'background.mp3')
# pygame.mixer.music.play(-1, 0.0)
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

# 导入 A的回合标牌
tag_A_turn = pygame.image.load('./images/tags/' + 'A的回合.jpg')
# 导入 B的回合标牌
tag_B_turn = pygame.image.load('./images/tags/' + 'B的回合.jpg')
# 导入 AI回合标牌
tag_AI_turn = pygame.image.load('./images/tags/' + 'AI回合.jpg')
# 导入 轮换标牌
tag_turn = pygame.image.load('./images/tags/' + '轮换.jpg')
# 导入 A胜利标牌
tag_A_win = pygame.image.load('./images/tags/' + 'A胜利.jpg')
# 导入 B胜利标牌
tag_B_win = pygame.image.load('./images/tags/' + 'B胜利.jpg')
# 导入 AI胜利标牌
tag_AI_win = pygame.image.load('./images/tags/' + 'AI胜利.jpg')
# 导入 同花BOOM标牌
tag_flush_boom = pygame.image.load('./images/tags/' + '同花BOOM.jpg')
# 导入 安全出牌标牌
tag_safe_play = pygame.image.load('./images/tags/' + '安全出牌.jpg')
# 导入 等待出牌标牌
tag_wait_play = pygame.image.load('./images/tags/' + '等待出牌.jpg')
# 导入 手牌出牌标牌
tag_from_hand = pygame.image.load('./images/tags/' + '手牌出牌.jpg')
# 导入 牌堆出牌标牌
tag_from_deck = pygame.image.load('./images/tags/' + '牌堆出牌.jpg')
# 导入 平局标牌
tag_equal = pygame.image.load('./images/tags/' + '平局.jpg')
# 导入 打开记牌器开关的图片
image_card_recorder_switch_on = pygame.image.load('./images/tags/' + '开关_开.jpg')
# 导入 关闭记牌器开关的图片
image_card_recorder_switch_off = pygame.image.load('./images/tags/' + '开关_关.jpg')

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
card_back = pygame.transform.scale(card_back, (105, 150))


# 卡牌类
class CARD:
    # 黑桃：S
    # 红心：H
    # 梅花：C
    # 方块：D
    # 大小王：K
    def __init__(self, card_value=1, card_type='S',
                 card_image=pygame.image.load('./images/' + '1.jpg'), ):
        self.card_value = card_value  # 卡牌数值
        self.card_type = card_type  # 卡牌花色
        self.card_image = card_image  # 卡牌图片


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

    def pop(self):
        return self.items.pop()


# 建立卡牌
cards = [CARD()]
for i in range(1, 14):
    cards.append(CARD(i, 'S', card_images[i]))
for i in range(14, 27):
    cards.append(CARD(i - 13, 'H', card_images[i]))
for i in range(27, 40):
    cards.append(CARD(i - 26, 'C', card_images[i]))
for i in range(40, 53):
    cards.append(CARD(i - 39, 'D', card_images[i]))
for i in range(53, 55):
    cards.append(CARD(i - 39, 'K', card_images[i]))
# ====================卡牌设置结束==================== #

# ====================相关变量/函数设置开始==================== #
use_card_recorder = True


# 花色类型S，H，C，D到0123的映射
def type_to_int(card_type):
    if card_type == 'S':
        return 0
    if card_type == 'H':
        return 1
    if card_type == 'C':
        return 2
    if card_type == 'D':
        return 3


# ====================相关变量/函数设置开始==================== #


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
                        """-------------------------增加选项：1、创建对局2、加入对局（这里要显示一个输入框，输入房间uid）----------------------"""
                        """如果选择了创建对局的话直接调用online_match()，选择加入对局的话调用online_match(1，input())"""
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
    global use_card_recorder

    def update_page_game_setting():
        # 转到游戏设置界面
        screen.blit(background, (0, 0))  # 插入背景
        screen.blit(title, (318, 108))  # 插入标题
        screen.blit(button_return, (849, 605))  # 插入返回按钮
        screen.blit(txt_volume, (222, 327))  # 插入“音量”
        screen.blit(txt_open_recorder, (156, 421))  # 插入“开启记牌器”
        if use_card_recorder:
            screen.blit(image_card_recorder_switch_on, (455, 425))
        else:
            screen.blit(image_card_recorder_switch_off, (455, 425))
        # 刷新屏幕
        pygame.display.flip()

    update_page_game_setting()
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
                    elif event.pos[0] in range(455, 455 + 85) and event.pos[1] in range(425, 425 + 46):
                        use_card_recorder = not use_card_recorder
                        update_page_game_setting()

        fps_clock.tick(fps)


# 退出游戏：
def page_game_quit():
    sys.exit()


def local_match():
    deck_recorder = [13, 13, 13, 13]  # 牌堆记牌器
    placement_area_recorder = [0, 0, 0, 0]  # 放置区记牌器

    turn = 0  # 0表示A回合，1表示B回合
    # 牌堆，仅保存卡牌下标（因为随机）
    deck = []
    for ii in range(1, 53):
        deck.append(ii)
    placement_area = Stack()  # 放置区
    cards_in_hand = []
    for index in range(0, 8):
        cards_in_hand.append(Stack())  # 初始化手牌，0~3是A的手牌，4~7是B的手牌

    # 记牌器
    def show_card_recorder():
        screen.blit(tag_S_amount, (198, 270))  # 插入牌堆记牌器黑桃数量标牌
        screen.blit(tag_H_amount, (198, 317))  # 插入牌堆记牌器红心数量标牌
        screen.blit(tag_C_amount, (198, 363))  # 插入牌堆记牌器梅花数量标牌
        screen.blit(tag_D_amount, (198, 410))  # 插入牌堆记牌器方块数量标牌

        screen.blit(tag_S_amount, (791, 270))  # 插入放置区记牌器黑桃数量标牌
        screen.blit(tag_H_amount, (791, 317))  # 插入放置区记牌器红心数量标牌
        screen.blit(tag_C_amount, (791, 363))  # 插入放置区记牌器梅花数量标牌
        screen.blit(tag_D_amount, (791, 410))  # 插入放置区记牌器方块数量标牌

        # 显示牌数
        font = pygame.font.SysFont('microsoft Yahei', 30)
        # 显示牌堆牌数

        for deck_recorder_i in range(0, 4):
            card_num = font.render(str(deck_recorder[deck_recorder_i]), False, (255, 255, 255))
            screen.blit(card_num, (198 + 60, 270 + 47 * deck_recorder_i + 12))
        for placement_area_recorder_i in range(0, 4):
            card_num = font.render(str(placement_area_recorder[placement_area_recorder_i]), False, (255, 255, 255))
            screen.blit(card_num, (791 + 60, 270 + 47 * placement_area_recorder_i + 12))

    # 展示当前场上卡牌状况（1：等待出牌，2：安全出排，3：同花BOOM，4：牌堆出牌，5：手牌出牌）
    def show_situation(situation_type):
        # 展示当前场上的情况
        screen.blit(background, (0, 0))  # 插入背景
        screen.blit(button_return, (872, -7))  # 插入返回按钮
        screen.blit(tag_gamer_A, (110, 502))  # 玩家A标牌
        screen.blit(tag_gamer_B, (110, 10))  # 玩家B标牌
        if turn == 0:
            screen.blit(tag_A_turn, (467, 248))  # A的回合
        else:
            screen.blit(tag_B_turn, (467, 248))  # B的回合
        screen.blit(tag_cards_in_hand, (215, 502))  # A的手牌区
        screen.blit(tag_cards_in_hand, (215, 11))  # B的手牌区
        screen.blit(tag_deck, (303, 266))  # 牌堆区
        screen.blit(tag_deck_sign, (338, 468))  # 牌堆区标志
        screen.blit(tag_deck_amount, (337, 231))  # 牌堆区数量
        screen.blit(tag_placement_area, (628, 266))  # 放置区
        screen.blit(tag_placement_area_amount, (662, 229))  # 放置区数量
        screen.blit(tag_placement_area_sign, (663, 468))  # 放置区标志
        screen.blit(tag_S_amount, (252, 512))  # A-黑桃数量标牌
        screen.blit(tag_H_amount, (414, 512))  # A-红心数量标牌
        screen.blit(tag_C_amount, (577, 512))  # A-梅花数量标牌
        screen.blit(tag_D_amount, (739, 512))  # A-方块数量标牌

        screen.blit(tag_S_amount, (252, 21))  # B-黑桃数量标牌
        screen.blit(tag_H_amount, (414, 21))  # B-红心数量标牌
        screen.blit(tag_C_amount, (577, 21))  # B-梅花数量标牌
        screen.blit(tag_D_amount, (739, 21))  # B-方块数量标牌

        # 展示牌堆
        if len(deck) > 0:
            screen.blit(card_back, (327, 287))  # 牌堆顶是卡牌背面（即不展示）
        # 展示放置区
        if not placement_area.is_empty():
            screen.blit(placement_area.peek().card_image, (651, 289))
        # 展示手牌
        for iii in range(0, 8):
            if not cards_in_hand[iii].is_empty():
                if iii % 4 == 0:
                    if iii < 4:
                        screen.blit(cards_in_hand[iii].peek().card_image, (244, 555))
                    else:
                        screen.blit(cards_in_hand[iii].peek().card_image, (244, 64))
                elif iii % 4 == 1:
                    if iii < 4:
                        screen.blit(cards_in_hand[iii].peek().card_image, (406, 555))
                    else:
                        screen.blit(cards_in_hand[iii].peek().card_image, (406, 64))
                elif iii % 4 == 2:
                    if iii < 4:
                        screen.blit(cards_in_hand[iii].peek().card_image, (569, 555))
                    else:
                        screen.blit(cards_in_hand[iii].peek().card_image, (569, 64))
                elif iii % 4 == 3:
                    if iii < 4:
                        screen.blit(cards_in_hand[iii].peek().card_image, (731, 555))
                    else:
                        screen.blit(cards_in_hand[iii].peek().card_image, (731, 64))
        # 展示当前状况（1：等待出牌，2：安全出排，3：同花BOOM，4：牌堆出牌，5：手牌出牌）
        if situation_type == 1:
            screen.blit(tag_wait_play, (467, 327))  # 等待出牌
        elif situation_type == 2:
            screen.blit(tag_safe_play, (467, 327))  # 安全出排
        elif situation_type == 3:
            screen.blit(tag_flush_boom, (467, 327))  # 同花BOOM
        elif situation_type == 4:
            # screen.blit(tag_from_deck, (469, 290))  # 牌堆出牌
            screen.blit(tag_wait_play, (467, 327))  # 等待出牌
        elif situation_type == 5:
            # screen.blit(tag_from_hand, (469, 290))  # 手牌出牌
            screen.blit(tag_wait_play, (467, 327))  # 等待出牌
        # 显示牌数
        font = pygame.font.SysFont('microsoft Yahei', 30)
        # 显示牌堆牌数
        num = len(deck)
        card_num = font.render(str(num), False, (255, 255, 255))
        screen.blit(card_num, (367, 237))
        # 显示放置区牌数
        num = placement_area.size()
        card_num = font.render(str(num), False, (255, 255, 255))
        screen.blit(card_num, (692, 237))
        # 显示当前玩家牌数
        for card_num_i in range(0, 4):
            num = cards_in_hand[card_num_i].size()
            card_num = font.render(str(num), False, (255, 255, 255))
            if card_num_i == 0:
                screen.blit(card_num, (312, 524))
            elif card_num_i == 1:
                screen.blit(card_num, (474, 524))
            elif card_num_i == 2:
                screen.blit(card_num, (637, 524))
            elif card_num_i == 3:
                screen.blit(card_num, (799, 524))
        # 显示对方玩家牌数
        for card_num_i in range(4, 8):
            num = cards_in_hand[card_num_i].size()
            card_num = font.render(str(num), False, (255, 255, 255))
            if card_num_i == 4:
                screen.blit(card_num, (312, 33))
            elif card_num_i == 5:
                screen.blit(card_num, (474, 33))
            elif card_num_i == 6:
                screen.blit(card_num, (637, 33))
            elif card_num_i == 7:
                screen.blit(card_num, (799, 33))

        # 显示记牌器
        if use_card_recorder:
            show_card_recorder()

        # 刷新屏幕
        pygame.display.flip()

    show_situation(1)
    while len(deck) != 0:
        for event in pygame.event.get():
            if len(deck) == 0:
                break

            print(event)
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
                    elif event.pos[0] in range(327, 327 + 105) and event.pos[1] in range(287, 287 + 150):

                        if turn == 0:
                            print('动作：A从【牌堆】抽牌')
                        else:
                            print('动作：B从【牌堆】抽牌')
                        # 随机生成一个 [0, len(deck)) 的整型，得到随机的下标
                        random_num = random.randint(0, len(deck) - 1)
                        show_situation(4)
                        screen.blit(cards[deck[random_num]].card_image, (327, 287))
                        pygame.display.flip()  # 刷新屏幕
                        time.sleep(0.4)
                        # 牌堆抽牌，牌堆记牌器变化
                        deck_recorder[type_to_int(cards[deck[random_num]].card_type)] -= 1
                        if (not placement_area.is_empty()) \
                                and cards[deck[random_num]].card_type == placement_area.peek().card_type:
                            print('事件：同花Boom')
                            # 同花BOOM，放置区记牌器清空
                            placement_area_recorder = [0, 0, 0, 0]
                            placement_area.push(cards[deck[random_num]])
                            del deck[random_num]
                            while not placement_area.is_empty():
                                if placement_area.peek().card_type == 'S':
                                    cards_in_hand[turn * 4 + 0].push(placement_area.peek())
                                elif placement_area.peek().card_type == 'H':
                                    cards_in_hand[turn * 4 + 1].push(placement_area.peek())
                                elif placement_area.peek().card_type == 'C':
                                    cards_in_hand[turn * 4 + 2].push(placement_area.peek())
                                elif placement_area.peek().card_type == 'D':
                                    cards_in_hand[turn * 4 + 3].push(placement_area.peek())
                                placement_area.pop()
                            show_situation(3)
                            time.sleep(0.5)
                        else:
                            print('事件：不是同花')
                            # 不是同花，更新放置区记牌器
                            placement_area_recorder[type_to_int(cards[deck[random_num]].card_type)] += 1
                            placement_area.push(cards[deck[random_num]])
                            del deck[random_num]
                            show_situation(2)
                            time.sleep(0.5)
                        print('事件：轮换')
                        if turn == 1:
                            turn = 0
                        else:
                            turn = 1
                        show_situation(1)

                    elif (event.pos[0] in range(244, 244 + 105)
                          and event.pos[1] in range(555 - turn * 491, 555 + 150 - turn * 491)) \
                            or (event.pos[0] in range(406, 406 + 105)
                                and event.pos[1] in range(555 - turn * 491, 555 + 150 - turn * 491)) \
                            or (event.pos[0] in range(569, 569 + 105)
                                and event.pos[1] in range(555 - turn * 491, 555 + 150 - turn * 491)) \
                            or (event.pos[0] in range(731, 731 + 105)
                                and event.pos[1] in range(555 - turn * 491, 555 + 150 - turn * 491)):
                        # 从手牌出牌
                        temp_type = 'X'  # X表示无效的temp_type
                        if turn == 0:
                            character = 'A'
                        else:
                            character = 'B'
                        if event.pos[0] in range(244, 244 + 105) \
                                and event.pos[1] in range(555 - turn * 491, 555 + 150 - turn * 491):
                            if cards_in_hand[turn * 4 + 0].is_empty():
                                continue
                            print('动作：%s从【手牌】抽牌，【黑桃】' % character, cards_in_hand[turn * 4 + 0].top().card_value)
                            temp_type = 'S'
                        elif event.pos[0] in range(406, 406 + 105) \
                                and event.pos[1] in range(555 - turn * 491, 555 + 150 - turn * 491):
                            if cards_in_hand[turn * 4 + 1].is_empty():
                                continue
                            print('动作：%s从【手牌】抽牌，【红心】' % character, cards_in_hand[turn * 4 + 1].top().card_value)
                            temp_type = 'H'
                        elif event.pos[0] in range(569, 569 + 105) \
                                and event.pos[1] in range(555 - turn * 491, 555 + 150 - turn * 491):
                            if cards_in_hand[turn * 4 + 2].is_empty():
                                continue
                            print('动作：%s从【手牌】抽牌，【梅花】' % character, cards_in_hand[turn * 4 + 2].top().card_value)
                            temp_type = 'C'
                        elif event.pos[0] in range(731, 731 + 105) \
                                and event.pos[1] in range(555 - turn * 491, 555 + 150 - turn * 491):
                            if cards_in_hand[turn * 4 + 3].is_empty():
                                continue
                            print('动作：%s从【手牌】抽牌，【方块】' % character, cards_in_hand[turn * 4 + 3].top().card_value)
                            temp_type = 'D'
                        show_situation(5)  # 手牌出牌

                        if placement_area.is_empty():
                            if temp_type == 'S':
                                placement_area.push(cards_in_hand[turn * 4 + 0].peek())
                                cards_in_hand[turn * 4 + 0].pop()
                            elif temp_type == 'H':
                                placement_area.push(cards_in_hand[turn * 4 + 1].peek())
                                cards_in_hand[turn * 4 + 1].pop()
                            elif temp_type == 'C':
                                placement_area.push(cards_in_hand[turn * 4 + 2].peek())
                                cards_in_hand[turn * 4 + 2].pop()
                            elif temp_type == 'D':
                                placement_area.push(cards_in_hand[turn * 4 + 3].peek())
                                cards_in_hand[turn * 4 + 3].pop()
                            show_situation(2)
                        else:
                            if temp_type == placement_area.peek().card_type:
                                print('事件：同花Boom')
                                # 同花BOOM，清空放置区记牌器
                                placement_area_recorder = [0, 0, 0, 0]
                                while not placement_area.is_empty():
                                    if temp_type == 'S':
                                        placement_area.push(cards_in_hand[turn * 4 + 0].peek())
                                        cards_in_hand[turn * 4 + 0].pop()
                                    elif temp_type == 'H':
                                        placement_area.push(cards_in_hand[turn * 4 + 1].peek())
                                        cards_in_hand[turn * 4 + 1].pop()
                                    elif temp_type == 'C':
                                        placement_area.push(cards_in_hand[turn * 4 + 2].peek())
                                        cards_in_hand[turn * 4 + 2].pop()
                                    elif temp_type == 'D':
                                        placement_area.push(cards_in_hand[turn * 4 + 3].peek())
                                        cards_in_hand[turn * 4 + 3].pop()
                                    placement_area.pop()
                                show_situation(3)
                                time.sleep(0.5)
                            else:
                                print('事件：不是同花')
                                if temp_type == 'S':
                                    placement_area.push(cards_in_hand[turn * 4 + 0].peek())
                                    cards_in_hand[turn * 4 + 0].pop()
                                elif temp_type == 'H':
                                    placement_area.push(cards_in_hand[turn * 4 + 1].peek())
                                    cards_in_hand[turn * 4 + 1].pop()
                                elif temp_type == 'C':
                                    placement_area.push(cards_in_hand[turn * 4 + 2].peek())
                                    cards_in_hand[turn * 4 + 2].pop()
                                elif temp_type == 'D':
                                    placement_area.push(cards_in_hand[turn * 4 + 3].peek())
                                    cards_in_hand[turn * 4 + 3].pop()
                                # 不是同花，更新放置区记牌器
                                placement_area_recorder[type_to_int(temp_type)] += 1
                                show_situation(2)
                                time.sleep(0.5)
                        print('事件：轮换')
                        if turn == 1:
                            turn = 0
                        else:
                            turn = 1
                        show_situation(1)

    a_score = 0
    b_score = 0
    for type_i in range(0, 4):
        a_score = cards_in_hand[0 + type_i].size()
        b_score = cards_in_hand[3 + type_i].size()
    if a_score == b_score:  # 平局
        screen.blit(tag_equal, (469, 407))
    else:
        if a_score < b_score:  # A胜出
            screen.blit(tag_A_win, (469, 407))
        else:  # B胜出
            screen.blit(tag_B_win, (469, 407))
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


def ai_match():
    pass


def online_match(host_client=0, uuid=""):
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    r = {}
    datas = {
        'student_id': '031902322',
        'password': '895875010.3'
    }

    def login():
        """获取token"""
        fail = 0
        url = "http://172.17.173.97:8080/api/user/login"
        while True:
            try:
                if fail >= 20:
                    break
                r = requests.post(url=url, data=datas)
                if r.status_code == 200:
                    r = r.json()["data"]["token"]
                else:
                    continue
            except:
                fail += 1
                print("网络连接出现问题，正在尝试", fail)
            else:
                break

        # 将获取到的token返回
        return r

    headers["Authorization"] = str(login())

    def creat_game():
        """调用获取登录信息接口，将登录成功后，返回的token放在该请求的header中"""
        # 将login（）方法中返回的token放入header中
        # print(login())
        datas['private'] = True
        # print(datas)
        # print(headers)
        r = requests.post(
            url="http://172.17.173.97:9000/api/game",
            data=json.dumps(datas),
            headers=headers
        )
        print(r.json()["data"]["uuid"])
        return r.json()["data"]["uuid"]

    def join_game(uuid2):
        r = requests.post(
            url="http://172.17.173.97:9000/api/game/" + str(uuid2),
            data=json.dumps(datas),
            headers=headers
        )
        print(r)
        print(r.json())

    uuid_host = ""

    def get_last():
        if host_client == 0:
            url = "http://172.17.173.97:9000/api/game/" + uuid_host + "/last"
        else:
            url = "http://172.17.173.97:9000/api/game/" + uuid + "/last"
        r = requests.get(
            url=url,
            data=json.dumps(datas),
            headers=headers
        )
        print(r)
        print(r.json())
        return r.json()

    def player_do(x=0, y=""):
        datas["type"] = x
        datas["card"] = y
        if host_client == 0:
            url = "http://172.17.173.97:9000/api/game/" + uuid_host
        else:
            url = "http://172.17.173.97:9000/api/game/" + uuid
        r = requests.put(
            url=url,
            data=json.dumps(datas),
            headers=headers
        )
        print(r)
        print(r.json())
        return r.json()

    def value_change(num):
        str1 = ''
        if num == 11:
            str1 = 'J'
        elif num == 12:
            str1 = 'Q'
        elif num == 13:
            str1 = 'K'
        else:
            str1 = str(num)
        return str1

    deck_recorder = [13, 13, 13, 13]  # 牌堆记牌器
    placement_area_recorder = [0, 0, 0, 0]  # 放置区记牌器

    turn = 0  # 0表示我的回合，1表示对方回合
    # 牌堆，仅保存卡牌下标（因为随机）
    deck = []
    deck_num = 52
    for ii in range(1, 53):
        deck.append(ii)
    placement_area = Stack()  # 放置区
    cards_in_hand = []
    for index in range(0, 8):
        cards_in_hand.append(Stack())  # 初始化手牌，0~3是p1的手牌，4~7是p2的手牌

    # 记牌器
    def show_card_recorder():
        screen.blit(tag_S_amount, (198, 270))  # 插入牌堆记牌器黑桃数量标牌
        screen.blit(tag_H_amount, (198, 317))  # 插入牌堆记牌器红心数量标牌
        screen.blit(tag_C_amount, (198, 363))  # 插入牌堆记牌器梅花数量标牌
        screen.blit(tag_D_amount, (198, 410))  # 插入牌堆记牌器方块数量标牌

        screen.blit(tag_S_amount, (791, 270))  # 插入放置区记牌器黑桃数量标牌
        screen.blit(tag_H_amount, (791, 317))  # 插入放置区记牌器红心数量标牌
        screen.blit(tag_C_amount, (791, 363))  # 插入放置区记牌器梅花数量标牌
        screen.blit(tag_D_amount, (791, 410))  # 插入放置区记牌器方块数量标牌

        # 显示牌数
        font = pygame.font.SysFont('microsoft Yahei', 30)
        # 显示牌堆牌数

        for deck_recorder_i in range(0, 4):
            card_num = font.render(str(deck_recorder[deck_recorder_i]), False, (255, 255, 255))
            screen.blit(card_num, (198 + 60, 270 + 47 * deck_recorder_i + 12))
        for placement_area_recorder_i in range(0, 4):
            card_num = font.render(str(placement_area_recorder[placement_area_recorder_i]), False, (255, 255, 255))
            screen.blit(card_num, (791 + 60, 270 + 47 * placement_area_recorder_i + 12))

    # 展示当前场上卡牌状况（1：等待出牌，2：安全出排，3：同花BOOM，4：牌堆出牌，5：手牌出牌）
    def show_situation(situation_type):
        # 展示当前场上的情况
        screen.blit(background, (0, 0))  # 插入背景
        screen.blit(button_return, (872, -7))  # 插入返回按钮
        if host_client == 0:
            screen.blit(tag_gamer_A, (110, 502))  # 玩家A标牌
            screen.blit(tag_gamer_B, (110, 10))  # 玩家B标牌
        else:
            screen.blit(tag_gamer_A, (110, 10))  # 玩家A标牌
            screen.blit(tag_gamer_B, (110, 502))  # 玩家B标牌
        if turn == 0:
            screen.blit(tag_A_turn, (467, 248))  # A的回合
        else:
            screen.blit(tag_B_turn, (467, 248))  # B的回合

        screen.blit(tag_cards_in_hand, (215, 502))  # A的手牌区
        screen.blit(tag_cards_in_hand, (215, 11))  # B的手牌区

        screen.blit(tag_deck, (303, 266))  # 牌堆区
        screen.blit(tag_deck_sign, (338, 468))  # 牌堆区标志
        screen.blit(tag_deck_amount, (337, 231))  # 牌堆区数量
        screen.blit(tag_placement_area, (628, 266))  # 放置区
        screen.blit(tag_placement_area_amount, (662, 229))  # 放置区数量
        screen.blit(tag_placement_area_sign, (663, 468))  # 放置区标志
        screen.blit(tag_S_amount, (252, 512))  # A-黑桃数量标牌
        screen.blit(tag_H_amount, (414, 512))  # A-红心数量标牌
        screen.blit(tag_C_amount, (577, 512))  # A-梅花数量标牌
        screen.blit(tag_D_amount, (739, 512))  # A-方块数量标牌

        screen.blit(tag_S_amount, (252, 21))  # B-黑桃数量标牌
        screen.blit(tag_H_amount, (414, 21))  # B-红心数量标牌
        screen.blit(tag_C_amount, (577, 21))  # B-梅花数量标牌
        screen.blit(tag_D_amount, (739, 21))  # B-方块数量标牌

        # 展示牌堆
        if deck_num > 0:
            screen.blit(card_back, (327, 287))  # 牌堆顶是卡牌背面（即不展示）
        # 展示放置区
        if not placement_area.is_empty():
            screen.blit(placement_area.peek().card_image, (651, 289))
        # 展示手牌
        for iii in range(0, 8):
            if not cards_in_hand[iii].is_empty():
                if iii % 4 == 0:
                    if iii < 4:
                        if host_client == 0:
                            screen.blit(cards_in_hand[iii].peek().card_image, (244, 555))
                        else:
                            screen.blit(cards_in_hand[iii].peek().card_image, (244, 64))
                    else:
                        if host_client == 0:
                            screen.blit(cards_in_hand[iii].peek().card_image, (244, 64))
                        else:
                            screen.blit(cards_in_hand[iii].peek().card_image, (244, 555))
                elif iii % 4 == 1:
                    if iii < 4:
                        if host_client == 0:
                            screen.blit(cards_in_hand[iii].peek().card_image, (406, 555))
                        else:
                            screen.blit(cards_in_hand[iii].peek().card_image, (406, 64))
                    else:
                        if host_client == 0:
                            screen.blit(cards_in_hand[iii].peek().card_image, (406, 64))
                        else:
                            screen.blit(cards_in_hand[iii].peek().card_image, (406, 555))
                elif iii % 4 == 2:
                    if iii < 4:
                        if host_client == 0:
                            screen.blit(cards_in_hand[iii].peek().card_image, (569, 555))
                        else:
                            screen.blit(cards_in_hand[iii].peek().card_image, (569, 64))
                    else:
                        if host_client == 0:
                            screen.blit(cards_in_hand[iii].peek().card_image, (569, 64))
                        else:
                            screen.blit(cards_in_hand[iii].peek().card_image, (569, 555))
                elif iii % 4 == 3:
                    if iii < 4:
                        if host_client == 0:
                            screen.blit(cards_in_hand[iii].peek().card_image, (731, 555))
                        else:
                            screen.blit(cards_in_hand[iii].peek().card_image, (731, 64))
                    else:
                        if host_client == 0:
                            screen.blit(cards_in_hand[iii].peek().card_image, (731, 64))
                        else:
                            screen.blit(cards_in_hand[iii].peek().card_image, (731, 555))
        # 展示当前状况（1：等待出牌，2：安全出排，3：同花BOOM，4：牌堆出牌，5：手牌出牌）
        if situation_type == 1:
            screen.blit(tag_wait_play, (467, 327))  # 等待出牌
        elif situation_type == 2:
            screen.blit(tag_safe_play, (467, 327))  # 安全出排
        elif situation_type == 3:
            screen.blit(tag_flush_boom, (467, 327))  # 同花BOOM
        elif situation_type == 4:
            # screen.blit(tag_from_deck, (469, 290))  # 牌堆出牌
            screen.blit(tag_wait_play, (467, 327))  # 等待出牌
        elif situation_type == 5:
            # screen.blit(tag_from_hand, (469, 290))  # 手牌出牌
            screen.blit(tag_wait_play, (467, 327))  # 等待出牌
        # 显示牌数
        font = pygame.font.SysFont('microsoft Yahei', 30)
        # 显示牌堆牌数
        num = deck_num
        card_num = font.render(str(num), False, (255, 255, 255))
        screen.blit(card_num, (367, 237))
        # 显示放置区牌数
        num = placement_area.size()
        card_num = font.render(str(num), False, (255, 255, 255))
        screen.blit(card_num, (692, 237))
        # 显示当前玩家牌数
        for card_num_i in range(0, 4):
            num = cards_in_hand[card_num_i].size()
            card_num = font.render(str(num), False, (255, 255, 255))
            if card_num_i == 0:
                if host_client == 0:
                    screen.blit(card_num, (312, 524))
                else:
                    screen.blit(card_num, (312, 33))
            elif card_num_i == 1:
                if host_client == 0:
                    screen.blit(card_num, (474, 524))
                else:
                    screen.blit(card_num, (474, 33))
            elif card_num_i == 2:
                if host_client == 0:
                    screen.blit(card_num, (637, 524))
                else:
                    screen.blit(card_num, (637, 33))
            elif card_num_i == 3:
                if host_client == 0:
                    screen.blit(card_num, (799, 524))
                else:
                    screen.blit(card_num, (799, 33))
        # 显示对方玩家牌数
        for card_num_i in range(4, 8):
            num = cards_in_hand[card_num_i].size()
            card_num = font.render(str(num), False, (255, 255, 255))
            if card_num_i == 4:
                if host_client == 1:
                    screen.blit(card_num, (312, 524))
                else:
                    screen.blit(card_num, (312, 33))
            elif card_num_i == 5:
                if host_client == 1:
                    screen.blit(card_num, (474, 524))
                else:
                    screen.blit(card_num, (474, 33))
            elif card_num_i == 6:
                if host_client == 1:
                    screen.blit(card_num, (637, 524))
                else:
                    screen.blit(card_num, (637, 33))
            elif card_num_i == 7:
                if host_client == 1:
                    screen.blit(card_num, (799, 524))
                else:
                    screen.blit(card_num, (799, 33))

        # 显示记牌器
        if use_card_recorder:
            show_card_recorder()

        # 刷新屏幕
        pygame.display.flip()

    show_situation(1)  # 等待出牌
    if host_client == 0:
        uuid_host = str(creat_game())
        socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        addr = (get.get_ip(), 10000)
        # 绑定地址
        try:
            socket_server.bind(addr)
        except Exception as e:
            print(e)
        # 设置监听
        socket_server.listen(1)
        print("服务器已开启，等待连接...")
        # socket_server.accept()返回一个元组, 元素1为客户端的socket对象, 元素2为客户端的地址(ip地址，端口号)
        try:
            client_socket, address = socket_server.accept()
            print("有一个人连接上")
        except  Exception as e:
            print(e)
    if host_client == 1:
        join_game(uuid)
        # 创建一个socket对象
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # addr = 服务器端的IP和端口
        addr = (get.get_ip(), 10000)  # 只有自己一台电脑做测试时，可以直接用左边的
        s.connect(addr)
    while deck_num != 0:
        if turn == 1 and host_client == 0 or turn == 0 and host_client == 1:
            if host_client == 0:
                recvmsg = client_socket.recv(1024)
                strData = recvmsg.decode("gbk")
                print(strData)
                if strData == "finish":
                    client_step = get_last()
            if host_client == 1:
                msg = s.recv(1024)
                print(msg.decode("gbk"))
                if msg.decode("gbk") == "finish":
                    client_step = get_last()

            if client_step["data"]["last_code"][2] == '0':
                # pyautogui.moveTo(377, 337, duration=0.25)
                k = pygame.event.Event(pygame.MOUSEBUTTONUP, {'pos': (337, 337), 'button': 1, 'window': None})
            elif client_step["data"]["last_code"][2] == '1' and client_step["data"]["last_code"][4] == 'S':
                # pyautogui.moveTo(294, 139, duration=0.25)
                k = pygame.event.Event(pygame.MOUSEBUTTONUP, {'pos': (294, 139), 'button': 1, 'window': None})
            elif client_step["data"]["last_code"][2] == '1' and client_step["data"]["last_code"][4] == 'H':
                # pyautogui.moveTo(456, 139, duration=0.25)
                k = pygame.event.Event(pygame.MOUSEBUTTONUP, {'pos': (456, 139), 'button': 1, 'window': None})
            elif client_step["data"]["last_code"][2] == '1' and client_step["data"]["last_code"][4] == 'C':
                # pyautogui.moveTo(619, 139, duration=0.25)
                k = pygame.event.Event(pygame.MOUSEBUTTONUP, {'pos': (619, 139), 'button': 1, 'window': None})
            elif client_step["data"]["last_code"][2] == '1' and client_step["data"]["last_code"][4] == 'D':
                # pyautogui.moveTo(781, 139, duration=0.25)
                k = pygame.event.Event(pygame.MOUSEBUTTONUP, {'pos': (781, 139), 'button': 1, 'window': None})
            pygame.event.post(k)
        """触发获取到的事件"""
        for event in pygame.event.get():
            if len(deck) == 0:
                break
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
                    elif event.pos[0] in range(327, 327 + 105) and event.pos[1] in range(287, 287 + 150):
                        if turn == 0:
                            print('动作：A从【牌堆】抽牌')
                            if host_client == 0:
                                player_do(0)
                        elif turn == 1:
                            print('动作：B从【牌堆】抽牌')
                            if host_client == 1:
                                player_do(0)
                        # 根据上一步操作生成一个下标，无论上一步是对方还是我方操作都可以用get_last()函数
                        puke = get_last()["data"]["last_code"]
                        print(puke)
                        mark = 0
                        if puke[4] == 'S':
                            mark = 0
                        elif puke[4] == 'H':
                            mark = 1
                        elif puke[4] == 'C':
                            mark = 2
                        elif puke[4] == 'D':
                            mark = 3
                        num_string = ""
                        num_string = puke[5:len(puke)]
                        if num_string == 'J':
                            num_string = "11"
                        if num_string == 'Q':
                            num_string = "12"
                        if num_string == 'K':
                            num_string = "13"
                        random_num = mark * 13 + int(num_string) - 1
                        print("随机数是{}".format(random_num))
                        show_situation(4)
                        screen.blit(cards[deck[random_num]].card_image, (327, 287))
                        pygame.display.flip()  # 刷新屏幕
                        time.sleep(0.4)
                        # 牌堆抽牌，牌堆记牌器变化
                        deck_recorder[type_to_int(cards[deck[random_num]].card_type)] -= 1
                        if (not placement_area.is_empty()) \
                                and cards[deck[random_num]].card_type == placement_area.peek().card_type:
                            print('事件：同花Boom')
                            # 同花BOOM，放置区记牌器清空
                            placement_area_recorder = [0, 0, 0, 0]
                            placement_area.push(cards[deck[random_num]])
                            # del deck[random_num]
                            deck_num = deck_num - 1
                            while not placement_area.is_empty():
                                if placement_area.peek().card_type == 'S':
                                    cards_in_hand[turn * 4 + 0].push(placement_area.peek())
                                elif placement_area.peek().card_type == 'H':
                                    cards_in_hand[turn * 4 + 1].push(placement_area.peek())
                                elif placement_area.peek().card_type == 'C':
                                    cards_in_hand[turn * 4 + 2].push(placement_area.peek())
                                elif placement_area.peek().card_type == 'D':
                                    cards_in_hand[turn * 4 + 3].push(placement_area.peek())
                                placement_area.pop()
                            show_situation(3)
                            time.sleep(0.5)
                        else:
                            print('事件：不是同花')
                            # 不是同花，更新放置区记牌器
                            placement_area_recorder[type_to_int(cards[deck[random_num]].card_type)] += 1
                            placement_area.push(cards[deck[random_num]])
                            # del deck[random_num]
                            deck_num = deck_num - 1
                            show_situation(2)
                            time.sleep(0.5)
                        if turn == 0 and host_client == 0:
                            client_socket.send('finish'.encode("gbk"))
                        if turn == 1 and host_client == 1:
                            s.send('finish'.encode("gbk"))
                        print('事件：轮换')
                        if turn == 1:
                            turn = 0
                        else:
                            turn = 1
                        show_situation(1)


                    elif (event.pos[0] in range(244, 244 + 105) or event.pos[0] in range(406, 406 + 105) or \
                          event.pos[0] in range(569, 569 + 105) or event.pos[0] in range(731, 731 + 105)) \
                            and (event.pos[1] in range(555, 555 + 150) or event.pos[1] in range(64, 64 + 150)):
                        # 从手牌出牌
                        temp_type = 'X'  # X表示无效的temp_type
                        if turn == 0:
                            character = 'A'
                        else:
                            character = 'B'
                        if event.pos[0] in range(244, 244 + 105) \
                                and (event.pos[1] in range(555, 555 + 150) or event.pos[1] in range(64, 64 + 150)):
                            if cards_in_hand[turn * 4 + 0].is_empty():
                                continue
                            print('动作：%s从【手牌】抽牌，【黑桃】' % character, cards_in_hand[turn * 4 + 0].peek().card_value)
                            temp_type = 'S'
                            if turn == host_client:
                                player_do(1, temp_type + value_change(cards_in_hand[turn * 4 + 0].peek().card_value))
                        elif event.pos[0] in range(406, 406 + 105) \
                                and (event.pos[1] in range(555, 555 + 150) or event.pos[1] in range(64, 64 + 150)):
                            if cards_in_hand[turn * 4 + 1].is_empty():
                                continue
                            print('动作：%s从【手牌】抽牌，【红心】' % character, cards_in_hand[turn * 4 + 1].peek().card_value)
                            temp_type = 'H'
                            if turn == host_client:
                                player_do(1, temp_type + value_change(cards_in_hand[turn * 4 + 1].peek().card_value))
                        elif event.pos[0] in range(569, 569 + 105) \
                                and (event.pos[1] in range(555, 555 + 150) or event.pos[1] in range(64, 64 + 150)):
                            if cards_in_hand[turn * 4 + 2].is_empty():
                                continue
                            print('动作：%s从【手牌】抽牌，【梅花】' % character, cards_in_hand[turn * 4 + 2].peek().card_value)
                            temp_type = 'C'
                            if turn == host_client:
                                player_do(1, temp_type + value_change(cards_in_hand[turn * 4 + 2].peek().card_value))
                        elif event.pos[0] in range(731, 731 + 105) \
                                and (event.pos[1] in range(555, 555 + 150) or event.pos[1] in range(64, 64 + 150)):
                            if cards_in_hand[turn * 4 + 3].is_empty():
                                continue
                            print('动作：%s从【手牌】抽牌，【方块】' % character, cards_in_hand[turn * 4 + 3].peek().card_value)
                            temp_type = 'D'
                            if turn == host_client:
                                a = type_to_int(temp_type)
                                player_do(1, temp_type + value_change(cards_in_hand[turn * 4 + a].peek().card_value))
                        show_situation(5)  # 手牌出牌

                        if placement_area.is_empty():
                            if temp_type == 'S':
                                placement_area.push(cards_in_hand[turn * 4 + 0].peek())
                                print(cards_in_hand[turn * 4 + 0].peek())
                                cards_in_hand[turn * 4 + 0].pop()
                            elif temp_type == 'H':
                                placement_area.push(cards_in_hand[turn * 4 + 1].peek())
                                print(cards_in_hand[turn * 4 + 1].peek())
                                cards_in_hand[turn * 4 + 1].pop()
                            elif temp_type == 'C':
                                placement_area.push(cards_in_hand[turn * 4 + 2].peek())
                                print(cards_in_hand[turn * 4 + 2].peek())
                                cards_in_hand[turn * 4 + 2].pop()
                            elif temp_type == 'D':
                                placement_area.push(cards_in_hand[turn * 4 + 3].peek())
                                print(cards_in_hand[turn * 4 + 3].peek())
                                cards_in_hand[turn * 4 + 3].pop()
                            show_situation(2)
                        else:
                            if temp_type == placement_area.peek().card_type:
                                print('事件：同花Boom')
                                # 同花BOOM，清空放置区记牌器
                                placement_area_recorder = [0, 0, 0, 0]
                                while not placement_area.is_empty():
                                    if placement_area.peek().card_type == 'S':
                                        cards_in_hand[turn * 4 + 0].push(placement_area.peek())
                                    elif placement_area.peek().card_type == 'H':
                                        cards_in_hand[turn * 4 + 1].push(placement_area.peek())
                                    elif placement_area.peek().card_type == 'C':
                                        cards_in_hand[turn * 4 + 2].push(placement_area.peek())
                                    elif placement_area.peek().card_type == 'D':
                                        cards_in_hand[turn * 4 + 3].push(placement_area.peek())
                                    placement_area.pop()
                                show_situation(3)
                                time.sleep(0.5)
                            else:
                                print('事件：不是同花')
                                if temp_type == 'S':
                                    placement_area.push(cards_in_hand[turn * 4 + 0].peek())
                                    cards_in_hand[turn * 4 + 0].pop()
                                elif temp_type == 'H':
                                    placement_area.push(cards_in_hand[turn * 4 + 1].peek())
                                    cards_in_hand[turn * 4 + 1].pop()
                                elif temp_type == 'C':
                                    placement_area.push(cards_in_hand[turn * 4 + 2].peek())
                                    cards_in_hand[turn * 4 + 2].pop()
                                elif temp_type == 'D':
                                    placement_area.push(cards_in_hand[turn * 4 + 3].peek())
                                    cards_in_hand[turn * 4 + 3].pop()
                                # 不是同花，更新放置区记牌器
                                placement_area_recorder[type_to_int(temp_type)] += 1
                                show_situation(2)
                                time.sleep(0.5)
                        print('事件：轮换')
                        if turn == 0 and host_client == 0:
                            client_socket.send('finish'.encode("gbk"))
                        if turn == 1 and host_client == 1:
                            s.send('finish'.encode("gbk"))
                        if turn == 1:
                            turn = 0
                        else:
                            turn = 1
                        show_situation(1)

    if host_client == 0:
        socket_server.close()
        os._exit(0)
    else:
        os._exit(0)
    a_score = 0
    b_score = 0
    for type_i in range(0, 4):
        a_score = cards_in_hand[0 + type_i].size()
        b_score = cards_in_hand[3 + type_i].size()
    if a_score == b_score:  # 平局
        screen.blit(tag_equal, (469, 407))
    else:
        if a_score < b_score:  # A胜出
            screen.blit(tag_A_win, (469, 407))
        else:  # B胜出
            screen.blit(tag_B_win, (469, 407))
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


if __name__ == '__main__':
    # 开始菜单
    page_start_menu()
