import sys

getLine = lambda: sys.stdin.readline().strip()
dex_cnt, q_cnt = map(int, getLine().split())

pokemons = []
name_dex = {}


def store(i):
    pokemon = getLine()
    name_dex[pokemon] = i + 1
    pokemons.append(pokemon)


def find(_):
    q = getLine()
    print(pokemons[int(q) - 1] if q.isdigit() else name_dex[q])


jobs = [store] * dex_cnt + [find] * q_cnt

list(map(lambda i: (jobs[i](i)), range(dex_cnt + q_cnt)))
