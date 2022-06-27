# 条件成立执行的表达式  if 条件  else   条件不成立执行表达式

a = 1
b = 2
c = a if a > b else b
print(c)


aa = 6
bb = 10
#cc = (aa if aa > bb else bb) - (aa if aa < bb else bb)
cc = aa - bb if aa > bb else bb - aa
print(cc)
