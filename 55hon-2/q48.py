a = 0
b = 5
try:
    print(a / b)
    print(b / a)
except ZeroDivisionError:
    print('zero division')
