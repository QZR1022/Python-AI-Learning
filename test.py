# Day07 字典 dict：简易通讯录
contact = {
    "张三": "13800138000",
    "李四": "13900139000",
    "家人": "13700137000"
}

print("=== 通讯录 ===")
print("张三的电话：", contact["张三"])

# 遍历
print("\n所有联系人：")
for name, phone in contact.items():
    print(name, ":", phone)

# 添加新联系人
contact["新同学"] = "13600136000"
print("\n添加后：", contact)