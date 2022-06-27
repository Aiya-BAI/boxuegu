str = 'itheima'
for i in str:
    if i == 'e':
        continue    #如果使用continue,在continue前一定要修改计数器，否则进入死循环
    print(i)