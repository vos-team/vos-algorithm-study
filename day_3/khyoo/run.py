from nq.sb import bjrun

make_one_input_1 = "2"
make_one_input_2 = "10"

yakusoku_input_1 = """3
1 21 79
20 30 25"""

yakusoku_input_2 = """8
100 15 1 2 3 4 6 5
49 40 1 2 3 4 5 4"""

yakusoku_input_3 = """12
1 1 1 1 1 1 1 1 1 1 1 1
100 100 100 100 100 100 100 100 100 100 100 100"""

yakusoku_input_4 = """8
100 26 13 17 24 33 100 99
34 56 21 1 24 34 100 99"""

yakusoku_input_5 = """1
100
20"""

yakusoku_input_6 = """4
100 50 20 13
20 30 40 50"""

AB_input_1 = '''B
ABBA'''

AB_input_2 = '''AB
ABB'''

tests = [
    ("00_make_one.py", make_one_input_1),
    ("00_make_one.py", make_one_input_2),
    ("01_yakusoku.py", yakusoku_input_1),
    ("01_yakusoku.py", yakusoku_input_2),
    ("01_yakusoku.py", yakusoku_input_3),
    ("01_yakusoku.py", yakusoku_input_4),
    ("01_yakusoku.py", yakusoku_input_5),
    ("01_yakusoku.py", yakusoku_input_6),
    ("02_AB.py", AB_input_1),
    ("02_AB.py", AB_input_2),
]

for fp, input_text in tests:
    bjrun(fp, input_text)
