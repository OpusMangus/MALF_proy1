class NDFA_node:
    def __init__(self, value, final = False):
        self.value = value
        self.final = False
        self.edges = []
