# https://www.acmicpc.net/problem/1966

import sys

l = lambda: sys.stdin.readline().strip()

n = int(l())
for i in range(n):
    doc_cnt, target_doc_idx = map(int, l().split())
    doc_priorities = list(map(int, l().split()))

    docs = [(p, i) for i, p in enumerate(doc_priorities)]
    doc_priorities_sorted = sorted(doc_priorities, reverse=True)

    printed = 0
    while len(docs):
        if docs[0][0] == doc_priorities_sorted[0]:
            printed += 1
            if docs[0][1] == target_doc_idx:
                print(printed)
                break
            docs = docs[1:]
            doc_priorities_sorted = doc_priorities_sorted[1:]
        else:
            docs = docs[1:] + docs[:1]
