
num_words = int(input())
trans_dict = {}

for i in range(num_words):
    pair = input().split()
    trans_dict[pair[0]] = pair[1]

sentence = input()

for word in sentence.split():
    if trans_dict.get(word.lower()):
        print(trans_dict[word.lower()], end=' ')
    else:
        print(word, end=' ')

