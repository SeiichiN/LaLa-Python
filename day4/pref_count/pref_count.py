pref_count_dict = {}
with open('data/visitor_record.txt', encoding='UTF=8') as f:
    for line in f:
        date, pref, num_adult, num_child = line.rstrip('\n').split(',')
        num_all = int(num_adult) + int(num_child)
        if pref in pref_count_dict:
            pref_count_dict[pref] += num_all
        else:
            pref_count_dict[pref] = num_all

print(pref_count_dict)