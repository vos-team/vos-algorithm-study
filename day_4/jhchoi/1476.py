E, S, M = 1, 1, 1
year = 1
e, s, m = map(int, input().split())

while not (E == e and s == S and M == m): 
    E += 1
    S += 1
    M += 1
    year += 1
    if (E == 16): 
        E = 1
    if (S == 29):
        S = 1
    if (M == 20):
        M = 1

print(year)