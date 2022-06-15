infile = open('D:/python/input.txt', 'r')
freq = {}

for line in infile:
    for ch in line.rstrip():
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
print(freq)

infile.close()