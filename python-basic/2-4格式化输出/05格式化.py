'''
准备数据
格式化
'''

age = 18
name = 'Tom'
weight = 75.5
stu_id = 1

#初级
print('今年年龄是%d岁' %age)
print("我的名字是%s" %name)
print("我的体重是%f" %weight)
print("我的体重是%.2f" %weight)#保留两位小数

print('=====================')
#高级
print("学号是%03d" %stu_id)#不足3位以0补全，超过则原样显示

print('名字是%s,年龄是%d' % (name, age))#连用
print('名字是%s,明年年龄是%d' % (name, age+1))#连用

print('名字是%s',)

