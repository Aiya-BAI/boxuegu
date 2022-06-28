str = 'hello world and itcast and itheima and Python'

#1.find()
print(str.find('and')) #12从左往右
print(str.find('and', 15, 30)) #23,15到30之间查找
print(str.find('ands', )) # -1 查不到

#2.index()
print(str.index('and'))  #12
print(str.index('and', 15, 30))  #23
#print(str.index('ands', )) # 报错


#3.count()出现次数
print(str.count('and', 15, 30))  #1
print(str.count('and'))  #3
print(str.count('ands'))  #0

#4.rfind()从右侧开始查找
print(str.rfind('and'))  #35
print(str.rfind('ands'))

#5.rindex()从右侧
print(str.rindex('and'))  #35
#print(str.index('ands'))  #23