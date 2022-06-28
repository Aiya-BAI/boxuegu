class Sweetpotato:
    def __init__(self):
        self.cook_time = 0
        self.cook_statu = '生的'
        self.condiments = []

    def cook(self, time):
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_statu = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_statu = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_statu = '熟了'
        elif self.cook_time > 8:
            self.cook_statu = '糊了'

    def add_condiments(self, condiment):
        self.condiments.append(condiment)

    def __str__(self):
        return f'地瓜是 {self.cook_statu},添加了{self.condiments}'

potato = Sweetpotato()
potato.cook(4)
potato.add_condiments('芥末')
print(potato)






