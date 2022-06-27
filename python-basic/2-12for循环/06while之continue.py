i = 0
while i < 5:
    if i == 3:
        i += 1
        continue
    print('我错了')
    i += 1
else:
    print('可以了')    #continue后else执行