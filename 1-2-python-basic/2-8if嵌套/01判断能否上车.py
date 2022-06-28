#有钱上车，没钱不上车；是否有座才坐下

money = int(input('输入钱:'))
seat  = int(input('输入1或者0:'))
print(seat)
print(type(seat))

if money >= 1:
    print("可以上车")

    if seat == 1:
        print('坐下')
    else:
        print('站着吧')

else:
    print('不能上车')



