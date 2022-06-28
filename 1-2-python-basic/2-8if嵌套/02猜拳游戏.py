'''
1.出拳
    玩家，输入
    电脑，固定
2.判断
    玩家赢
    平局
    电脑赢

'''

player = int(input('请出拳：0--石头，1--剪刀，2--布：'))
computer = 1

if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print('玩家获胜')
elif player == computer:
    print('平局')
else:
    print('电脑胜利')




