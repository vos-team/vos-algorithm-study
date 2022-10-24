from nq.sb import bjrun

ball_input = '''4
3 1
2 3
3 1
3 2'''

tests = [
    ("00_ball.py", ball_input),
]

for fp, input_text in tests:
    bjrun(fp, input_text)
