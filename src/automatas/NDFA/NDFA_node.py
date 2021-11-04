from .NDFA_edge import NDFA_edge

class NDFA_node:
    def __init__(self, value, final = False):
        self.value = value
        self.final = final
        self.edges = []

    def add_rizos(self, alphabet):
        for char in alphabet:
            edge = NDFA_edge(char, self)
            self.edges.append(edge)
