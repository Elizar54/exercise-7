
def count_descendants(gr, start):
    c = 0
    if gr[start] == []:
        return 0
    else:
        c += len(gr[start])
        for child in gr[start]:
            c += count_descendants(gr, child)
        return c


n = int(input()) 
gr = {}

for i in range(n):
    pair = input().split()

    if gr.get(pair[0]):
        gr[pair[0]].append(pair[1])
    else:
        gr[pair[0]] = [pair[1]]

    if not gr.get(pair[1]):
        gr[pair[1]] = []

'''
with open('graph_5.txt', encoding='utf-8') as f:
    for x in f:
        pair = x.split()

        if gr.get(pair[0]):
            gr[pair[0]].append(pair[1])
        else:
            gr[pair[0]] = [pair[1]]

        if not gr.get(pair[1]):
            gr[pair[1]] = []
'''

start = input()


print(count_descendants(gr, start))