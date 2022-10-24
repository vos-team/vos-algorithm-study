from nq.sb import bjrun

ascending_input = """5
5
2
3
4
1"""

time_sum_min_input = """5
3 1 4 3 2"""

coords_input = """5
0 4
1 2
1 -1
2 2
3 3"""

string_sort_input = """13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours"""

tests = [
    ("00_ascending.py", ascending_input),
    ("01_time_sum_min.py", time_sum_min_input),
    ("02_coords.py", coords_input),
    ("03_string_sort.py", string_sort_input),
]

for fp, input_text in tests:
    bjrun(fp, input_text)
