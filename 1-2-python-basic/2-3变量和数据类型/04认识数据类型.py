"""
1.数据类型
"""
num1 = 1
num2 = 1.1
a = 'hello worLD '
b = True

print(type(num1))
print(type(num2))
print(type(a))
print(type(b))
#列表
c = [10, 20, 30]
print(c)
print(type(c))
#元组
d = (10, 20, 30)
print(type(d))
#集合
e = {10, 20, 30}
print(type(e))
#

#字符串转换
print(a.title())
print(a.upper())
print(a.lower())

#字符串拼接
first_name = "bai yun ce "
print("hello, " + first_name.title() + "!")

#制表符 换行符
print("\tbaiyunce ")
print("\nbaiyunce ")
print("\t\nbaiyunce ")
print("\n\tbaiyunce ")#\n在前\t才能生效

#删除空白 lstrip(),rstrip(),strip()
test1 = "baiyc  "
test2 = "  sunjy"
print(test1 + test2)
print(test1.rstrip() + test2.rstrip())
print(test1.lstrip() + test2.lstrip())
print(test1.strip().upper() + test2.title().strip())










