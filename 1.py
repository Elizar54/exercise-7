sent = input().split()
freq = {}

for elem in sent:
    if freq.get(elem.lower()):
        freq[elem.lower()] += 1
    else:
        freq[elem.lower()] = 1
    

reverse_dict = {}

for key, value in freq.items():
    reverse_dict[value] = key
    

for key in sorted(reverse_dict.keys())[::-1]:
    print(reverse_dict[key], end=' ')
