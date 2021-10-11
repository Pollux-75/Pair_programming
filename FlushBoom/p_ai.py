
# now_info: 当前场上局势，
# 0-3:      my_card                 自己手牌
# 4-7:      opponent_card           对手手牌
# 8-11:     deck_card               牌堆牌
# 12-15:    placement_card          放置区牌
# 16        top_type_of_placement_area   放置区牌顶

# answer:
#   0-出手牌黑桃
#   1-出手牌红心
#   2-出手牌梅花
#   3-出手牌方块
#   4-牌堆出排
def p_ai(now_info):
    # 设定应该保留的手牌数
    amount_to_keep = 4

    my_card = [now_info[0], now_info[1], now_info[2], now_info[3]]
    opponent_card = [now_info[4], now_info[5], now_info[6], now_info[7]]
    deck_card = [now_info[8], now_info[9], now_info[10], now_info[11]]
    placement_card = [now_info[12], now_info[13], now_info[14], now_info[15]]
    top_type_of_placement_area = now_info[16]

    my_card_amount = 0
    opponent_card_amount = 0
    deck_card_amount = 0
    placement_card_amount = 0

    for type_i in range(0, 4):
        my_card_amount += my_card[type_i]
        opponent_card_amount += opponent_card[type_i]
        deck_card_amount += deck_card[type_i]
        placement_card_amount += placement_card[type_i]

    def get_second_most_cards_type_in_deck(temp_card):
        temp_card[temp_card.index(max(temp_card))] = -1
        return temp_card.index(max(temp_card))

    # 牌堆中最多的牌（牌堆最有可能被抽到的花色）
    most_cards_type_in_deck = deck_card.index(max(deck_card))
    # 牌堆中第二多的牌
    second_most_cards_type_in_deck = get_second_most_cards_type_in_deck(deck_card)

    # 把手牌中跟放置区顶相同花色的花色置为0
    if top_type_of_placement_area != 4:
        my_card[top_type_of_placement_area] = 0

    # 己方牌为0时
    if my_card_amount == 0:
        # 直接抽牌堆
        return 4

    # 对方没牌而且放置区牌数大于5
    if opponent_card_amount == 0 and placement_card_amount >=5:
        # 放置区顶不是牌堆最可能出现的牌
        if top_type_of_placement_area != most_cards_type_in_deck:
            return most_cards_type_in_deck


    # 己方牌数 > 对手牌数 时，出手牌
    if my_card_amount > opponent_card_amount:
        # 最多的牌和放置区冲突 且 除了最多的牌没牌，则抽牌堆
        if my_card[my_card.index(max(my_card))] == 0:
            return 4
        # 否则出最多的牌
        else:
            return my_card.index(max(my_card))
    # 己方牌数 <= 对手牌数 时，安全则抽牌堆，否则出手牌
    else:
        # 如果牌堆中最可能出现的牌不是放置区顶的牌，则出牌
        if most_cards_type_in_deck != top_type_of_placement_area:
            return 4
        # 否则，在没牌的情况下抽牌，有牌则出牌
        else:
            if my_card_amount == 0:
                return 4
            else:
                return my_card.index(max(my_card))
