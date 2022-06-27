#float()
num1 = 1
str1 = '10'
print(type(float(num1)))
print(float(num1))
print(float(str1))

#str()
print(type(str(num1)))

#tuple() 将一个序列转换成元组,序列列表中括号，元组小括号
list1 = [100, 200, 300]
print(list1)
print(tuple(list1))

#list()  将一个序列转换成列表
t1 = (100, 200, 300)
print(list(t1))

#eval() 计算在字符串中有效的python表达式，并返回一个对象
str2  = '1'
str3  = '1.1'
str4  = '(100, 200, 300)'
str5  = '[100, 200, 300]'
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))

