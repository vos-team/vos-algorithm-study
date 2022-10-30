from nq.sb import bjrun

search_input = """4 5 1
1 2
1 3
1 4
2 4
3 4"""

search_input_2 = """5 5 3
5 4
5 2
1 2
3 4
3 1"""

search_input_3 = """1000 1 1000
999 1000"""

tests = [
    ("00_search.py", search_input),
    ("00_search.py", search_input_2),
    ("00_search.py", search_input_3),
]

for fp, input_text in tests:
    bjrun(fp, input_text)
