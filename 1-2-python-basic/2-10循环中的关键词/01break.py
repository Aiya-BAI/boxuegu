#当某些条件成立，退出整个循环

i = 1
while i <= 5:
    # 条件吃到4个或者>3 ,则打印吃饱了
    if i == 4:
        print('吃饱了')
        break
    print(f'吃了{i}个苹果')
    i += 1