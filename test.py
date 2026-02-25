# Day05 while 循环：猜数字游戏
import random

# 随机生成1-10的数字
target_num = random.randint(1, 10)
print("=== 猜数字游戏（1-10）===")

while True:
    guess = int(input("请猜一个数字："))

    if guess > target_num:
        print("太大了，再试试～")
    elif guess < target_num:
        print("太小了，再试试～")
    else:
        print("恭喜你！猜对啦！")
        break