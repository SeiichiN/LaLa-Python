age = int(input('年齢を教えてください: '))

##if age < 4:
##    print('入場料は無料です')
##elif age < 13:
##    print('子供料金で入場できます')
##else:
##    print('大人料金が必要です')
    
if age < 13 or age >= 65:
    print('入場料は無料です')
else:
    print('料金が必要です')

if 12 < age < 65:
    print("料金が必要です")
    
