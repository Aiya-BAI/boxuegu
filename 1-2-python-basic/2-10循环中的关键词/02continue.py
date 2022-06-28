i = 1
while i <= 5:
    if i == 3:
        print(f'第{i}个吃到了虫子,但是没吃饱')
        # 如果使用continue,在continue前一定要修改计数器，否则进入死循环
        i += 1
        continue
    print(f'吃了{i}个苹果')
    i += 1