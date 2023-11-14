class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def age_check(p, i):
    if p.age > i:
        return True
    else:
        return False

a = Person("高橋太郎", 19)
b = Person("小林花子", 18)
age = 20
if age_check(a, age):
    print(f'{a.name}の年齢は{age}歳超')
else:
    print(f'{a.name}の年齢は{age}歳以下')
