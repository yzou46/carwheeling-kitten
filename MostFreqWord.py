
file_name = 'test.txt'
file = open(file_name)

counts = {}

for line in file:
    words = line.split(' ')
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigCount = 0
bigWord = None

for word, count in counts.items():
    if bigWord is None or count > bigCount:
        bigCount = count
        bigWord = word

print(bigWord, bigCount)
