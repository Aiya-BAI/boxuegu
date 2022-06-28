str = 'hello world and itcast and itheima and Python'

#1.replace and换成he
# replace有返回值，不会改变原有返回值
# 说明  字符串是不可变数据类型
#替换次数如果超出出现次数，便是替换所有

mystr = str.replace('and', 'he')
print(str)   #原有字符串不变
print(mystr)


#2.split() ---分割，返回一个列表
list1 = str.split('and')
print(list1)
list2 = str.split('and', 2)
print(list2)

#3.join() ---合并  合并列表里的字符串数据为一个大字符串
mylist = ['aa', 'bb', 'cc']
new_str = ''.join(mylist)
print(new_str)
new_str1 = '...'.join(mylist)
print(new_str1)

