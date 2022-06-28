# 没有循环不执行else中执行语句
i = 0

while i < 5:
    print('我错了')
    i += 1
else:
    print('可以了')