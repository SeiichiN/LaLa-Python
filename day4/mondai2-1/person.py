class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def print_info(p):
    print(f'名前: {p.name}')
    print(f'年齢: {p.age}')

a = Person("高橋太郎", 19)
b = Person("小林花子", 18)
print_info(a)
print_info(b)
