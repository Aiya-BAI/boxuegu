str = '0123456789'

print(str)
print(str[1])
print(str[5])
#
print(str[0:3])      #012
print(str[:3])       #012
print(str[3:])       #3456789
print(str[0:6:2])    #024
#负数测试
print(str[6:0:-2])   #642
print(str[::-1])     #倒叙9876543210
print(str[-4:-1])    #678
#终极

print(str[-4:-1:1])  #678
print(str[-4:-1:-1]) #方向冲突：无法选取


