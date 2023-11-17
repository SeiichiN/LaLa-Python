l = ['リンゴ', 'バナナ', 'オレンジ']
try:
    a = input('好きな整数を入力')
    print(l[int(a)])
except ValueError:
    print('数字が入力されませんでした')
except IndexError:
    print('範囲外の数字が入力されました')
