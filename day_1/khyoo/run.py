from nq.sb import bjrun

stack_input_1 = """14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top"""

stack_input_2 = """7
pop
top
push 123
top
pop
top
pop"""

pq_input = """3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1"""

dq_input_1 = "(1+(2*(3+4)))"
# (1+(2*3+4))
# (1+2*(3+4))
# (1+2*3+4)
# 1+(2*(3+4))
# 1+(2*3+4)
# 1+2*(3+4)
# 1+2*3+4

dq_input_2 = "(0/(0))"
# (0/0)
# 0/(0)
# 0/0

dq_input_3 = "(2+(2*2)+2)"
# (2+2*2+2)
# 2+(2*2)+2
# 2+2*2+2

tests = [
    ("00_stack.py", stack_input_1),
    ("00_stack.py", stack_input_2),
    ("01_printer_queue.py", pq_input),
    ("02_rm_paren.py", dq_input_1),
    ("02_rm_paren.py", dq_input_2),
    ("02_rm_paren.py", dq_input_3),
]

for fp, input_text in tests:
    bjrun(fp, input_text)
