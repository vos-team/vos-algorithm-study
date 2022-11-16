from nq.sb import bjrun

# sort_input = """4 3
# 2 3 5 9
# 1 4 7"""

# sort_input_2 = """1 1
# 100
# 11"""

bad_lord = """6 7
0 1 5395
0 2 540
0 4 7096
1 2 1051
2 4 4750
3 4 9616
3 5 9476"""

bad_lord_2 = """7 9
0 1 4068
0 3 9921
1 4 474
2 3 421
2 5 9685
3 4 1182
3 5 1690
4 6 9761
5 6 644"""

prerequisite = """3 2
2 3
1 2"""

prerequisite_2 = """6 4
1 2
1 3
2 5
4 5"""

tests = [
    # ("11728.py", sort_input),
    # ("11728.py", sort_input_2),
    # ("20010.py", bad_lord),
    # ("20010.py", bad_lord_2),
    ("14567.py", prerequisite),
    ("14567.py", prerequisite_2),
]

for fp, input_text in tests:
    bjrun(fp, input_text)
