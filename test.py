# Day03 if-elif-else 成绩判断
score = int(input("请输入你的成绩(0-100)："))

if score >= 90:
    print("等级：优秀")
elif score >= 80:
    print("等级：良好")
elif score >= 60:
    print("等级：及格")
else:
    print("等级：不及格，要加油啦！")