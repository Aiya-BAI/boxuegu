j = 0
while j < 10:
    i = 1
    while i <= j:
        # print('*', end='\n')
        print(f'{i}*{j}={i*j}', end='\t')
        i += 1
    print()
    j += 1