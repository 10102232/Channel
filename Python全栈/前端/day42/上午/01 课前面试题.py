
"""
去重， 保持原来的顺序
"""
l1 = [11, 2, 33, 7, 11, 8, 19, 1, 2]

# 去重
l2 = list(set(l1))
print(l2)  # [33, 2, 1, 7, 8, 11, 19]

# 保持顺序
# 怎么用代码描述这个 元素出现的顺序  --> 索引
# 将去重之后列表中的元素 按照原来的顺序 排序

print(l1.index(33))
l2.sort(key=l1.index)
print(l2)


l3 = [
    {"name": "sylar", "age": 88},
    {"name": "Gold", "age": 38},
    {"name": "Eva_J", "age": 18},
    {"name": "Alex", "age": 9000},
]

# 将l3中的元素按照age由小到大排序
ret = sorted(l3, key=lambda dic:dic["age"])
print(ret)

l3.sort(key=lambda x: x["age"])
print(l3)

