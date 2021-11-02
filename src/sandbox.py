from automatas.NDFA.automata import automata
from automatas.NDFA.NDFA_edge import NDFA_edge
from automatas.NDFA.NDFA_node import NDFA_node



t1 = automata("asdf")
t1.get_transition_table()
print(t1.NDFA)