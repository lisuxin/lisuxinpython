alist = [3, 4, 2, 9, 12, 6, 18, -6]
print(alist[:])  # 取全部元素
print(alist[0:])
print(alist[:-1])  # 取除最后一个元素的所有的元素
print(alist[2:5])  # 从第二个开始取到第五个，不包含第五个
print(alist[::2])  # 从0开始每隔一个取一个元素
print(alist[1:5:2])  # 从第一个开始取到第五个每隔一个取一个，不包含第五个
print(alist[::-1])  # 从右向左取全部
print(alist[5:0:-2])  # 从第五个开始，从右向左隔一个取一个到0为止不包含0
