import sys

sys.stdin = open('day_6/mjjo/11724.txt')
input = sys.stdin.readline
N, M = map(int, input().split())


# 1
node_dic = dict((_, set([])) for _ in range(1, N+1))
for _ in range(M):
    m, s = map(int, input().split())
    node_dic[m].add(s)
    node_dic[s].add(m)

node_arr = [_ for _ in range(1, N+1)]
count = 0

def dfs(v):
    visited = [v]
    queue = node_dic[v]

    while queue:
        node = queue.pop()
        if node not in visited:
            visited.append(node)
            queue = node_dic[node].union(queue)

    return visited

while node_arr:
    v = node_arr.pop(0)
    visited_arr = dfs(v)
    node_arr = list(set(node_arr) - set(visited_arr))
    count += 1

print(count)


# 2
# list in O(n)
# set in O(1)
node_set = set([_ for _ in range(1, N+1)])
visited_set = set([])
groups = []
for _ in range(M):
    m_idx = -1
    s_idx = -1
    m, s = map(int, input().split())
    for idx, group in enumerate(groups):
        if m in group:
            m_idx = idx

        if s in group:
            s_idx = idx
    
    if m_idx > -1 and s_idx > -1 and m_idx != s_idx:
        groups[m_idx] = groups[m_idx].union(groups[s_idx])
        groups.pop(s_idx)

    elif m_idx > -1:
        groups[m_idx].add(s)

    elif s_idx > -1:
        groups[s_idx].add(m)

    else:
        groups.append(set([m, s]))

for group in groups:
    visited_set = visited_set.union(group)
# print(node_set)
# print(visited_set)
# print(groups)
# print(len(groups))

print(len(groups) + len(node_set - visited_set))