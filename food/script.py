from food import Food
from drink import Drink

food1 = Food("ハンバーガー", 300, 400)
food2 = Food("チキンナゲット", 200, 250)

foods = [food1, food2]

print("食べ物メニュー")

drink1 = Drink("メロンソーダ", 150, 300)
drink2 = Drink("コーラ", 250, 500)

drinks = [drink1, drink2]

index = 0


for food in foods:
    print(str(index) + "." + food.info())
    index += 1

print("飲み物メニュー")

index = 0

for drink in drinks:
    print(str(index) + "." + drink.info())
    index += 1

oder = int(input("食べ物の番号を選択してください"))
selected_food = foods[oder]

oder = int(input("飲み物の番号を選択してください"))
selected_drink = drinks[oder]

count = int(input("何セット買いますか？（３つ以上で割引）"))

result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

print("合計金額は" + str(result) + "円です")

