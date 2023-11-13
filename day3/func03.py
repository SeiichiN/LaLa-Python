def countdown(start, end=0):
    print('引数1で受け取った値:', start)
    print('引数2で受け取った値:', end)
    print('カウントダウンをします')
    counter = start
    while counter >= end:
        print(counter)
        counter -= 1

countdown(4)

