import random
from process import Process


cardA = ["a", "b", "c", "d"]

cardB = ["a", "b", "c", "d"]
#要素をシャッフル
random.shuffle(cardA)
random.shuffle(cardB)

game_max_count = int(len(cardA))
game_count = 0
game_point = 0


#後でWhileに変更
for count in range(game_max_count):

    deal = Process(cardA)
   
    deal.card_deal()

    print("------------")

    deal = Process(cardB)

    deal.card_deal()

    cardA_input = int(input("１枚目のカード番号を選んでください"))
    card_judgeA = cardA[cardA_input]
    print(cardA[cardA_input])

    cardB_input = int(input("２枚目のカード番号を選んでください"))
    card_judgeB = cardB[cardB_input]
    print(cardB[cardB_input])

    game_count_c = game_count
    deal.judge(card_judgeA, card_judgeB, game_count)
    print("現在" + str(game_point) + "ポイントです")
    
    if game_count_c > game_count:
        cardA.remove(cardA[cardA_input])
        cardB.remove(cardB[cardB_input])
        deal.point_count(game_point)
    else:
        pass

