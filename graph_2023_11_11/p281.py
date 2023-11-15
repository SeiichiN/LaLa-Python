import matplotlib
import matplotlib.pyplot as plt
# import japanize_matplotlib


def get_r(x):
    return x[1]


pref_count_dict = {}

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
lst_desc = sorted(lst, key=get_r, reverse=True)
print(lst_desc)
labels = [k for k, v in lst_desc]
values = [v for k, v in lst_desc]
print(labels)
print(values)
plt.rcParams['font.family'] = 'Yu Gothic'
plt.bar(labels, values)
plt.xticks(rotation=60)
plt.ylabel('人', rotation=0)
plt.title('図書館の訪問者数')
plt.savefig('図書館の訪問者数.png')
plt.show()

# matplotlib.use("AGG") は,CUI環境などグラフを描画する
# インターフェースがない環境で画像としてグラフを保存する場合
# 必要になる。
