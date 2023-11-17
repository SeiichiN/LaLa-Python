dic = {
    'two': 324,
    'four': 830,
    'three': 493,
    'one': 172,
    'five': 1024
}
lst = sorted(dic.items(), key=lambda x: x[1])
print(lst)
keys = [k for k, v in lst]
print(keys)

