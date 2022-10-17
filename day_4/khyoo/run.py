from nq.sb import bjrun

ascending_input = """5
5
2
3
4
1"""

tests = [
    ("00_ascending.py", ascending_input),
]

for fp, input_text in tests:
    bjrun(fp, input_text)
