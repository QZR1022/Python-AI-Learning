# Day04 for 循环：求和、打印图案
print("1 到 100 求和：")
sum_result = 0
for i in range(1, 101):
    sum_result += i
print("结果：", sum_result)

# 打印星星
print("\n打印星星：")
for i in range(1, 6):
    print("*" * i)