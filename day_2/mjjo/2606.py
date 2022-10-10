import sys

sys.stdin = open('day_2/mjjo/2606.txt', 'r')
input = sys.stdin.readline

# 1
n = int(input())
p = int(input())
pc_groups = []

for _ in range(p):
    m_idx = -1
    s_idx = -1
    m, s = map(int, input().split())
    for idx, pc_group in enumerate(pc_groups):
        if m in pc_group:
            m_idx = idx

        if s in pc_group:
            s_idx = idx
    
    if m_idx > -1 and s_idx > -1 and m_idx != s_idx:
        pc_groups[m_idx] = pc_groups[m_idx].union(pc_groups[s_idx])
        pc_groups.pop(s_idx)

    elif m_idx > -1:
        pc_groups[m_idx].add(s)

    elif s_idx > -1:
        pc_groups[s_idx].add(m)

    else:
        pc_groups.append(set([m, s]))

for pc_group in pc_groups:
    if 1 in pc_group:
        print(len(pc_group)-1)


# 2
def dfs(w):
    visit[w] = 1
    for i in pc_groups[w]:
        if visit[i] == 0:
            dfs(i)

pc_n = int(input())
visit = [0]*(pc_n+1)
pc_groups = [[] for _ in range(pc_n+1)]
p = int(input())

for _ in range(p):
    m, s = map(int, input().split())
    pc_groups[m].append(s)
    pc_groups[s].append(m)

dfs(1)
print(visit.count(1)-1)