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

    def show(self):
        print('K = ', end='')
        for node in self.node_list:
            print(node.value, end=', ')
        print()
        print('Sigma = ', end='')
        for char in self.alphabet:
            print(char, end=', ')
        print()
        print('Delta:')
        for node in self.node_list:
            for edge in node.edges:
                print(node.value + ', ' + edge.in_char + ', ' + edge.target.value)
        print('s=' + self.start_node.value)
        print('F = ', end='')
        for node in self.final_states:
            print(node.value, end=', ')
        print()

    def add_rizos(self):
        self.start_node.add_rizos(self.alphabet)