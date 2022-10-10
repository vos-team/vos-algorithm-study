from nq.sb import bjrun

make_one_input_1 = "2"
make_one_input_2 = "10"

tests = [
    ("00_make_one.py", make_one_input_1),
    ("00_make_one.py", make_one_input_2),
]

for fp, input_text in tests:
    bjrun(fp, input_text)
