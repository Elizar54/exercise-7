
num_words = int(input())
word_dict = {}

for i in range(num_words):
    words = input().split()
    key = words[0]
    value = [x.lower() for x in words[1:]]
    word_dict[key] = value

word = input().lower()

for key in word_dict:
    if word in set(word_dict[key]):
        print(key)
        break
else:
    print('Слово не обнаружено')
