class Process():
    def __init__(self, card):
        self.card = card

    def card_deal(self):

        #カードを並べる
        for cardnum1, a in enumerate(self.card):
            print(str(cardnum1))

    def judge(self, card_judgeA, card_judgeB, game_count):
        self.card_judgeA = card_judgeA
        self.card_judgeB = card_judgeB
        self.game_count = game_count

        if card_judgeA in card_judgeB:
            print("あたり！１点獲得！")
            return game_count + 1
        else:
            print("はずれ...")
            return
    #仮
    def point_count(self, game_point):
        self.game_point = game_point

        game_point + 1
