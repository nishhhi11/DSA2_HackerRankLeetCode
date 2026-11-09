numbers = [1, 2, 2, 3, 1, 4, 2, 3]
freq = {}

for i in numbers:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)