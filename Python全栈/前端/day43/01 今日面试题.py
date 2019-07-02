"""
编写代码生成如下列表：
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12]]
"""

# ret = []
# for i in range(4):
#     l1 = [0, ]
#     for j in range(4):
#         l1.append(l1[-1]+i)
#     ret.append(l1)
# print(ret)

ret = []
for i in range(4):
    l1 = []
    for j in range(5):
        l1.append(i*j)
    ret.append(l1)
print(ret)


ret = [[i * j for j in range(5)] for i in range(4)]
print(ret)


#
# ret = []
# for i in range(4):
#     ret.append(list(map(lambda x: x*i, [0, 1, 2, 3, 4])))
# print(ret)
