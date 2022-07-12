try:
    print(1/0)
except(NameError, ZeroDivisionError):
    print('有错误')

try:
    print(1/0)
except(NameError, ZeroDivisionError) as result:
    print(result)
# print(1/0)

try:
    print(1)
except Exception as result:
    print(result)
else:
    print('没有错误')

try:
    f = open('test.txt', 'r')
except Exception as result:
    f = open('test.txt', 'w')
else:
    print('没有异常')
finally:
    f.close()


