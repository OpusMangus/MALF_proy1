from .DFA_edge import DFA_edge

class DFA_node:
    def __init__(self, value, NDFA_states, final = False):
        self.value = value
        self.final = final
        self.NDFA_states = NDFA_states
        self.edges = []
    
    def add_rizos(self, alphabet):
        for char in alphabet:
            edge = DFA_edge(char, self)
            self.edges.append(edge)
