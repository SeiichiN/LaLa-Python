nums = [1, 2, 4, 3, 2, 1, 5, 1]
num2freq = {}
for n in nums:
    if n in num2freq:
        num2freq[n] += 1
    else:
        num2freq[n] = 1

print(num2freq)
