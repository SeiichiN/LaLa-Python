import matplotlib.pyplot as plt
import japanize_matplotlib

pref_count_dict = {}
with open('data/visitor_record.txt', encoding='UTF=8') as f:
    for line in f:
        date, pref, num_adult, num_child = line.rstrip('\n').split(',')
        num_all = int(num_adult) + int(num_child)
        if pref in pref_count_dict:
            pref_count_dict[pref] += num_all
        else:
            pref_count_dict[pref] = num_all

pref_count_sorted = sorted(pref_count_dict.items(), key=lambda x: x[1], reverse=True)
for i in pref_count_sorted:
    print(i)

labels = []
values = []
for l, v in pref_count_sorted:
    labels.append(l)
    values.append(v)
print(labels)
print(values)
# plt.rcParams['font.family'] = 'Yu Gothic'
plt.xticks(rotation=60)
plt.title('図書館の訪問者数')
plt.ylabel('人', rotation=0)
plt.bar(labels, values)
plt.savefig('図書館の訪問者数.png')
plt.show()
