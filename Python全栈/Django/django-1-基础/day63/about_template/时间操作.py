import time
import datetime

# 1. 把一个自字符串格式的时间转化成结构化的时间
# 创建一个时间， 2018-10-01
# t1 = time.strptime('2018-10-01', '%Y-%m-%d')
# print(t1)  # 结构化的时间
# print(t1.tm_year)

# 2. 把结构化的时间格式转换成指定格式字符串: 2018.10.01
t2 = time.localtime()
t3 = time.strftime('%Y.%m.%d', t2)
print(t3)

# 3. 时间间隔
t4 = datetime.datetime.now()
print(t4)
print(type(t4))
# 在t2的基础上再加一天
t5 = t4 + datetime.timedelta(days=1)
print(t5)


