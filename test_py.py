'''
Created on 2022/04/21

@author: saitouryuunosuke
'''

import random

hands = ["グー", "チョキ", "パー"]

m = random.randint(0, 2)
com = hands[m]

print("0:グー　1:チョキ　2:パー")
p = int(input("じゃんけん・・・"))
player = hands[p]

