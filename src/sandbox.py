from automatas.NDFA.automata import automata
from automatas.NDFA.NDFA_edge import NDFA_edge
from automatas.NDFA.NDFA_node import NDFA_node


# NDFA 1: a.b
q0 = NDFA_node('q0')
q1 = NDFA_node('q1')
q2 = NDFA_node('q2', True)

edg1 = NDFA_edge('a')
edg1.target = q1

edg2 = NDFA_edge('b')
edg2.target = q2

q0.edges.append(edg1)
q1.edges.append(edg2)

# NDFA 2: a|b*
k0 = NDFA_node('q0')
k1 = NDFA_node('q1')
k2 = NDFA_node('q2')
k3 = NDFA_node('q3')
k4 = NDFA_node('q4')
k5 = NDFA_node('q5')
k6 = NDFA_node('q6')
k7 = NDFA_node('q7', True)

# q0
ed1 = NDFA_edge('_')
ed1.target = k1

ed2 = NDFA_edge('_')
ed2.target = k3

k0.edges.append(ed1)
k0.edges.append(ed2)

# q1
ed3 = NDFA_edge('a')
ed3.target = k2

k1.edges.append(ed3)

# q2
ed4 = NDFA_edge('_')
ed4.target = k7

k2.edges.append(ed4)

# q3
ed5 = NDFA_edge('_')
ed5.target(k4)

ed6 = NDFA_edge('_')
ed6.target(k6)

k3.edges.append(ed5)
k3.edges.append(ed6)

# q4
ed7 = NDFA_edge('b')
ed7.target(k5)

k4.edges.append(ed7)

# q5
ed8 = NDFA_edge('_')
ed8.target = k4

ed9 = NDFA_edge('_')
ed9.target = k6

k5.edges.append(ed8)
k5.edges.append(ed9)

# q6
ed10 = NDFA_edge('_')
ed10.target = k7

k6.edges.append(ed10)

t1 = automata("asdf")
t1.get_transition_table()
print(t1.NDFA)
