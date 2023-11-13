def print_price(price, func):
    print('価格は' + func(price))

print_price(800, lambda x: f'税抜き{x}円')

print_price(800, lambda x: f'税込み{int(x*1.1)}円')
