class DFA_node:
    def __init__(self, value, NDFA_states, final = False):
        self.value = value
        self.final = final
        self.NDFA_states = NDFA_states
        self.edges = []
