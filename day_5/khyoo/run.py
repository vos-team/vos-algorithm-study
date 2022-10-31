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

calc_days_input = """1 16 16"""
calc_days_input_2 = """1 1 1"""
calc_days_input_3 = """1 2 3"""

tests = [
    ("00_ball.py", ball_input),
    ("01_tsp.py", tsp_input),
    ("02_dummy.py", dummy_input),
    ("03_calc_days.py", calc_days_input),
    ("03_calc_days.py", calc_days_input_2),
    ("03_calc_days.py", calc_days_input_3),
]

for fp, input_text in tests:
    bjrun(fp, input_text)
