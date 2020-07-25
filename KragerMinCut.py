from random import choice
from copy import deepcopy


def contract(copy):
    u = choice(list(copy.keys()))
    v = choice(copy[u])
    new_key = u + "-" + v
    copy[new_key] = copy[u] + copy[v]
    del copy[u]
    del copy[v]
    for key in copy.keys():
        copyRow = copy[key][:]
        if new_key == key:
            for item in copyRow:
                if item == u or item == v:
                    copy[key].remove(item)
        else:
            for item in copyRow:
                if item == u or item == v:
                    copy[key].remove(item)
                    copy[key].append(new_key)


def min_cut(graph):
    n = len(graph)
    minimum = n * (n - 1) // 2
    for i in range(n):
        copy = deepcopy(graph)
        while len(copy) > 2:
            contract(copy)
            minimum = min(minimum, len(list(copy.values())[0]))
    return minimum


graph = {}
with open('KargerMinCut.txt') as f:
    data = f.readlines()
    for line in data:
        elements = list(map(str, line.split('\t')[:-1]))
        graph[str(elements[0])] = elements[1:]
f.close()
print(min_cut(graph))