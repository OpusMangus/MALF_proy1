from automatas.NDFA.automata import automata
from automatas.NDFA.NDFA_edge import NDFA_edge
from automatas.NDFA.NDFA_node import NDFA_node


# NDFA 1: a.b
q0 = NDFA_node('q0')
q1 = NDFA_node('q1')
q2 = NDFA_node('q2')
q2.final = True

edg1 = NDFA_edge('a')
edg1.target = q1

edg2 = NDFA_edge('b')
edg2.target = q2

q0.edges.append(edg1)
q1.edges.append(edg2)

# NDFA 2: a|b*


t1 = automata("asdf")
t1.get_transition_table()
print(t1.NDFA)
