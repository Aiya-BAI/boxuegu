from student import *

class StudentManage(object):
    def __init__(self):
        # 存储学员数据
        self.student_list = []

    # 一、程序入口函数
    def run(self):
        # 加载文件里的数据
        self.load_student()
        while True:
            # 显示功能菜单
            self.show_menu()
            # 输入序号
            menu_num = int(input('输入序号：'))
            # 根据序号执行功能

            if menu_num == 1:
                # 添加
                self.add_student()
            elif menu_num == 2:
                # 删除
                self.del_student()
            elif menu_num == 3:
                # 修改
                self.modify_stadent()
            elif menu_num == 4:
                # 查询
                self.search_student()
            elif menu_num == 5:
                # 显示
                self.show_student()
            elif menu_num == 6:
                # 保存
                self.save_student()
            elif menu_num == 7:
                # 退出
                break

    # 二、系统功能函数
    # 显示功能 ---打印序号和功能对应关系 --静态方法
    @staticmethod
    def show_menu():
        print('请选择功能：')
        print('1:添加')
        print('2:删除')
        print('3:修改')
        print('4:查询')
        print('5:显示')
        print('6:保存')
        print('7:退出')

    # 添加
    def add_student(self):
        # print('添加学员')
        name = input('姓名：')
        gender = input('性别：')
        tel = input('手机号：')

        student = Student(name, gender, tel)
        self.student_list.append(student)
        print(self.student_list)
        print(student)

    # 删除
    def del_student(self):
        print('删除')

    # 修改
    def modify_stadent(self):
        print('修改')

    # 查询
    def search_student(self):
        print('查询学员信息')

    # 显示
    def show_student(self):
        print('显示')

    # 保存
    def save_student(self):
        print('保存')

    # 加载信息
    def load_student(self):
        print('加载信息')


