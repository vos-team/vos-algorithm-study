import sys
sys.stdin = open('day_2/mjjo/1620.txt', 'r')

input = sys.stdin.readline
input_num, req_num = list(map(int, input().strip().split()))

pokemon_arr = [0] * input_num
for idx in range(input_num):
    pokemon = input().strip()
    pokemon_arr[idx] = pokemon

pokemon_dic = dict(zip(pokemon_arr, range(1, input_num+1)))
for idx in range(req_num):
    req = input().strip()
    if req.isdigit():
        print(pokemon_arr[int(req)-1])
    else:
        print(pokemon_dic[req])
