class automata:
    def __init__(self, start_node):
        self.NDFA = start_node

    def get_transition_table(self):
        return

    def move(origin_states, char):
        target_states = []
        for state in origin_states:
            for edge in state.edges:
                if(edge.in_char == char):
                    target_states.append(edge.target)
        return set(target_states)
