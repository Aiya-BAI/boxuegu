
'''
自写
i = 2
result = 0
while i <= 100:
    result = result + i
    i += 2
print(result)

'''
# 推荐这种，程序运算，不掺杂人脑运算
i = 1
result = 0
while i <= 100:
    if i % 2 ==0:
        result += i
    i += 1
print(result)

