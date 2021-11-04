class automata:
    def __init__(self, start_node, node_list, alphabet):
        self.start_node = start_node
        self.alphabet = alphabet
        self.node_list = node_list
        self.final_states = self.get_final_states()

    def get_final_states(self):
        temp = []
        for node in self.node_list:
            if(node.final):
                temp.append(node)
        return temp

    def format_list(self, coll):
        formatted = '{'
        for item in coll:
            formatted = formatted + item + ','
        formatted = formatted[:-1]
        formatted = formatted + '}'
        return formatted

    def show(self, tittle):
        print(tittle + ':')
        print('K=', end='')
        nodes = [node.value for node in self.node_list]
        print(self.format_list(nodes))
        print('Sigma=', end='')
        print(self.format_list(self.alphabet))
        print('Delta:')
        for node in self.node_list:
            for edge in node.edges:
                print('(' + node.value + ',' + edge.in_char + ',' + edge.target.value + ')')
        print('s=' + self.start_node.value)
        print('F=', end='')
        states = [state.value for state in self.final_states]
        print(self.format_list(states))
        print()
    
    
    def add_rizos(self):
        self.start_node.add_rizos(self.alphabet)