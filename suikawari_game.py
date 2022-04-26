'''
Created on 2022/04/25

@author: saitouryuunosuke
'''
import random
import math

suika_x = random.randint(0, 5)
suika_y = random.randint(0, 5)
# スイカの初期位置を設定
suika = [suika_x, suika_y]

start_x = random.randint(0, 5)
start_y = random.randint(0, 5)
# スタート位置を設定、報告
player = [start_x, start_y]
print(f"スタート位置は{player}です。")

# スイカとプレイヤーが重なるまで繰り返す
while player != suika:
    # スイカとスタート位置の距離を報告
    distance_x = abs(suika_x - player[0])
    distance_y = abs(suika_y - player[1])

    # 距離を導出
    distance = math.sqrt((distance_x ** 2) + (distance_y ** 2))
    print(f"スイカまでの距離は{distance}です。")

    # 動く方向を決める
    print(f"現在地は{player}です。")
    print("0:東　1:西　2:南　3:北")
    direction_player = int(input("動く方向を入力して下さい："))

    # 東の場合y方向に+1する
    if direction_player == 0:
        player[1] += 1

    # 西の場合y方向に-1する
    if direction_player == 1:
        player[1] -= 1

    # 南の場合x方向に+1する
    if direction_player == 2:
        player[0] += 1

    # 北の場合x方向に-1する
    if direction_player == 3:
        player[0] -= 1


print("スイカが割れました")
