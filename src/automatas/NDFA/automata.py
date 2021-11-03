class automata:
    def __init__(self, start_node, alphabet):
        self.NDFA = start_node
        self.alphabet = alphabet

    def get_transition_table(self):
        return

    def e_closure(self, node_from):
        #set with every node reachable by epsilon
        closure = set()
        #to visit stack
        reachable = []
        #for every next state from this node
        for edge in node_from.edges:
            if(edge.in_char == '_'):
                reachable.append(edge.target) #add node to the DFS stack
                closure.add(edge.target) #add value of the new node to the set
        #consume the stack until empty
        while(len(reachable) > 0):
            reached = reachable.pop() #pop node
            #for every edge in node check if epsilon
            for edge in reached.edges:
                if(edge.in_char == '_'):
                    if(not (edge.target.value in closure)):
                        reachable.append(edge.target)
                        closure.add(edge.target)
        return closure