from nq.sb import bjrun

map_input = """26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna"""

virus_input = """7
6
1 2
2 3
1 5
5 2
5 6
4 7"""

tree_input = """50
30
24
5
28
45
98
52
60"""


tests = [
    ("00_poke_master.py", map_input),
    ("01_virus.py", virus_input),
    ("02_tree.py", tree_input),
]

for fp, input_text in tests:
    bjrun(fp, input_text)
