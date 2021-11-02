class NFDA_Node:
    def __init__(self, value):
        self.value = value
        self.final = False
        self.edges = []
