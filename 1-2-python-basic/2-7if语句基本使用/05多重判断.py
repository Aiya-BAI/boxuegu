age = int(input('请输入年龄：'))

if age < 18:
    print(f'{age}是童工')
elif age > 60:
    print(f'{age}退休了')

# else:
#     print(f'{age}正常上班')
#化简写法
elif 18 <= age <= 60:
    print(f'{age}正常上班')