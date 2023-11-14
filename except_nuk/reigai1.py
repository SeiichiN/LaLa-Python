print('a ÷ b')
try:
    a = input('a > ')
    b = input('b > ')
    c = float(a) / float(b)
    print('Ans:', c)
except ValueError:
    print('wrong input!')
except ZeroDivisionError:
    print('ZERO division!')

print('end')
