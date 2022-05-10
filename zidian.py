dict = {}  # 创建一个空字典
# dict={'键':值,}
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dict)
lag = {'python': 1, 'c': 2, 'java': 3}
print(lag['java'])
print(dict['a'])
# 修改值
lag["java"] = 4  # 直接将值赋给键
# 增加值
lag["c#"] = 3  # 直接将值赋给一个新的键
print(lag)
del lag["c#"]  # 删除元素
print(lag)
del lag  # 删除元组
