
def lst_matrix(gr, n, city_index):
    matrix = []
    for i in range(n):
        matrix.append([float('inf')]*n)
    for city_1, city_2, c in gr:
        matrix[city_index[city_1]][city_index[city_2]] = int(c)
        matrix[city_index[city_2]][city_index[city_1]] = int(c)
    return matrix


def floyd(matrix):
    n = len(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] + matrix[j][k] < matrix[i][k]:
                    matrix[i][k] = matrix[i][j] + matrix[j][k]
    return matrix


n = int(input())
m = int(input())
gr = []
city_set = set()
graph = {}
city_index = {}

'''
for i in range(m):
    conseq = input().split()
    gr.append(conseq)

    for elem in conseq[:2]:
        city_set.add(elem)
'''
path = input().split()


with open('graph_6.txt', encoding='utf-8') as f:
    for x in f:
        conseq = x.split()
        gr.append(conseq)
        for elem in conseq[:2]:
            city_set.add(elem)


index = 0
for city in city_set:
    city_index[city] = index
    index += 1

matrix = lst_matrix(gr, n, city_index)

matrix = floyd(matrix)

print(matrix[city_index[path[0]]][city_index[path[1]]])