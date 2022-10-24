from nq.sb import bjrun

ball_input = """4
3 1
2 3
3 1
3 2"""

tsp_input = """4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0"""

dummy_input = """6
3
3 4
2 5
5 3
3
3 D
15 L
17 D"""

tests = [
    ("00_ball.py", ball_input),
    ("01_tsp.py", tsp_input),
    ("02_dummy.py", dummy_input),
]

for fp, input_text in tests:
    bjrun(fp, input_text)
