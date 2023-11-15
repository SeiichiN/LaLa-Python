pref_count_dict = {}

def get_right(x):
    return x[1]

with open('visitor_record.txt', encoding='UTF-8') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]
    for line in lines:
        date, pref, num_adult, num_child = line.split(',')
        num_all = int(num_adult) + int(num_child)
        if pref in pref_count_dict:
            pref_count_dict[pref] += num_all
        else:
            pref_count_dict[pref] = num_all

lst = pref_count_dict.items()
lst_desc = sorted(lst, key=get_right, reverse=True)
print(lst_desc)



