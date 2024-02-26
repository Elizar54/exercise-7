
num_words = int(input())
ant_dict = {}

for i in range(num_words):
    pair = input().split()
    ant_dict[pair[0]] = pair[1]
    ant_dict[pair[1]] = pair[0]

word = input().lower()

if ant_dict.get(word):
    print(ant_dict[word])
else:
    print(word)

