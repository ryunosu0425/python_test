'''
Created on 2022/04/21

@author: saitouryuunosuke
'''

import random
from anaconda_project.internal.conda_api import result

hands = ["グー", "チョキ", "パー"]

m = random.randint(0, 2)
com = hands[m]

print("0:グー　1:チョキ　2:パー")
p = int(input("じゃんけん・・・"))
player = hands[p]

if player == com:
    result = "あいこ"

elif player == "グー":
    if com == "チョキ":
        result = "勝ち"
    elif com == "パー":
        result = "負け"

elif player == "チョキ":
    if com == "パー":
        result = "勝ち"
    elif com == "グー":
        result = "負け"

elif player == "パー":
    if com == "グー":
        result = "勝ち"
    elif com == "チョキ":
        result = "負け"

print(f"コンピュータは、「{com}」を出しました")
print(f"あなたは、「{player}」を出したので、あなたの「{result}」です")