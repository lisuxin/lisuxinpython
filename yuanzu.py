tuple = (1, 2, 3, 'k', 'Python')
print(type(tuple))
tuple_2 = (8,)  # 创建只含一个元素的元组时要注意，元素后要加“，”
print(tuple_2)
tuple_3 = (8)  # 未加“，”则视为一个括号表达式
print(tuple_3)
language = ("java", "c#", "PHP")
merge = tuple + language  # 链接运算
print(merge)
print(language*3)# 重复运算
# tuple.index(value,[start[,top]])
# tuple.count(value)
print(merge.index('java'))
print(merge.count('c#'))