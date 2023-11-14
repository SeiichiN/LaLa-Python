with open('visitor_record.txt', encoding='UTF-8') as f:
    lines = [l.rstrip('\n') for l in f]
    for l in lines:
        print(l)
