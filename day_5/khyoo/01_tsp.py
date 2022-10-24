import sys
import heapq

cnt = int(sys.stdin.readline())

graph = []
for _ in range(cnt):
    graph.append(list(map(int, sys.stdin.readline().split())))

start_loc = 0


def solution_1(graph, start_loc):
    def min_price(curr_loc, visited, curr_price_sum):
        if curr_loc == start_loc and curr_price_sum:
            return curr_price_sum
        else:
            visited.add(curr_loc)
            next_locs_prices = graph[curr_loc]
            next_loc_price_sums = []

            for next_loc in filter(
                lambda loc: loc not in visited and next_locs_prices[loc], range(cnt)
            ):
                next_loc_price = next_locs_prices[next_loc]
                heapq.heappush(
                    next_loc_price_sums,
                    min_price(next_loc, set(visited), curr_price_sum + next_loc_price),
                )

            if len(next_loc_price_sums):
                return heapq.heappop(next_loc_price_sums)

            if len(visited) == cnt and next_locs_prices[start_loc]:
                return curr_price_sum + next_locs_prices[start_loc]

            return cnt * 1_000_000

    return min_price(start_loc, set(), 0)


print(solution_1(graph, start_loc))

from itertools import permutations


def solution_2(graph, start_loc):
    min_total_price = cnt * 1_000_000
    for perm in permutations(range(1, cnt), cnt - 1):
        route = (start_loc, *perm, start_loc)
        total_price = 0
        i = 0
        while total_price < min_total_price and i < cnt:
            from_loc = route[i]
            next_loc = route[i + 1]
            i += 1
            if graph[from_loc][next_loc]:
                total_price += graph[from_loc][next_loc]
            else:
                total_price = cnt * 1_000_000
                break

        if total_price < min_total_price:
            min_total_price = total_price

    return min_total_price


print(solution_2(graph, start_loc))
