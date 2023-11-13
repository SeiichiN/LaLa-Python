class Seiseki:
    def __init__(self, pid, name):
        self.id = pid
        self.name = name
        self.ko = 0
        self.su = 0
        self.ei = 0
        self.sum = 0

    def set_score(self, points):
        self.ko = points['ko']
        self.su = points['su']
        self.ei = points['ei']
        self.sum = self.ko + self.su + self.ei

    def print_info(self):
        print(f'id:{self.id}', end=' ')
        print(f'名前:{self.name}', end=' ')
        print(f'国:{self.ko}', end=' ')
        print(f'数:{self.su}', end=' ')
        print(f'英:{self.ei}', end=' ')
        print(f'計:{self.sum}')


a = Seiseki(1, 'Taro')
b = Seiseki(2, 'Jiro')
score = {'ko': 56, 'su': 67, 'ei': 89}
a.set_score(score)
score = {'ko': 34, 'su': 56, 'ei': 35}
b.set_score(score)
a.print_info()
b.print_info()
