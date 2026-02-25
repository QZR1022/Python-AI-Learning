# Day06 列表 list：成绩管理
# 定义成绩列表
scores = [85, 92, 78, 90, 88]
print("所有成绩：", scores)

# 增
scores.append(95)
print("添加后：", scores)

# 查
print("最高分：", max(scores))
print("最低分：", min(scores))
print("平均分：", sum(scores) / len(scores))

# 遍历
print("\n遍历成绩：")
for s in scores:
    print(s)