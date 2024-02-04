from save import savetofile

fee = input('请输入午餐费用：')
members = input('请输入聚餐人姓名，以中文逗号，分隔：')

# 将人员放入一个列表
memberlist = members.split('，')
# 得到人数
headcount = len(memberlist)

avgfee = int(fee) / headcount
print(avgfee)

savetofile(memberlist, avgfee)

