class Seiseki:
    def __init__(self, id, name, ko, su, ei):
        self.id = id
        self.name = name
        self.ko = ko
        self.su = su
        self.ei = ei
        self.sum = ko + su + ei

    def print_info(self):
        print(f'id:{self.id}', end=' ')
        print(f'名前:{self.name}', end=' ')
        print(f'国:{self.ko}', end=' ')
        print(f'数:{self.su}', end=' ')
        print(f'英:{self.ei}', end=' ')
        print(f'計:{self.sum}')


a = Seiseki(1, 'Taro', 34, 45, 56)
b = Seiseki(2, 'Jiro', 56, 67, 78)
a.print_info()
b.print_info()

