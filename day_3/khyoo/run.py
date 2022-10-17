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

AB_input_1 = """B
ABBA"""

AB_input_2 = """AB
ABB"""

quit_input = """7
3 10
5 20
1 10
1 20
2 15
4 40
2 200"""

quit_input_2 = """10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10"""

quit_input_3 = """10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6"""

quit_input_4 = """10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50"""

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
    ("03_quit.py", quit_input),
    ("03_quit.py", quit_input_2),
    ("03_quit.py", quit_input_3),
    ("03_quit.py", quit_input_4),
]

for fp, input_text in tests:
    bjrun(fp, input_text)
