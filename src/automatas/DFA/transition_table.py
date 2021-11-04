from .DFA_node import DFA_node
from .DFA_edge import DFA_edge
from automatas.automata import automata

class transition_table:
    def __init__(self, NDFA):
        self.start_node = NDFA.start_node
        self.alphabet = NDFA.alphabet
        self.node_list = NDFA.node_list
        self.final_states = NDFA.final_states

    def get_DFA(self):
        #Crear q0 del DFA
        start_NFA_states = self.e_closure(self.start_node)
        start_NFA_states.add(self.start_node)

        q0 = DFA_node('q0', start_NFA_states, self.is_final_node(start_NFA_states, self.final_states))
        DFA_list = [q0]
        DFA_stack = [q0]
        
        qCounter = 1
        while(len(DFA_stack) > 0):
            node = DFA_stack.pop()
            for char in self.alphabet:
                moved_set = self.move(node.NDFA_states, char)
                closure_set = self.e_closure_set(moved_set)
                new_NDFA_state = moved_set.union(closure_set)

                DFA_state = self.get_DFA_state(DFA_list, new_NDFA_state)
                if(DFA_state == None):
                    DFA_state = DFA_node('q' + str(qCounter), new_NDFA_state, self.is_final_node(new_NDFA_state, self.final_states))
                    DFA_list.append(DFA_state)
                    DFA_stack.append(DFA_state)
                    qCounter += 1
                
                edge = DFA_edge(char, DFA_state)
                node.edges.append(edge)
        
        automataDFA = automata(q0, DFA_list, self.alphabet)
        return automataDFA

    def make_dfa_automata(self):
        return

    def get_DFA_state(self, DFA_list, NDFA_state):
        for node in DFA_list:
            if(node.NDFA_states == NDFA_state):
                return node
        return None

    def is_final_node(self, NFA_state, NDFA_final_states):
        for state in NFA_state:
            if(state in NDFA_final_states):
                return True
        return False

    def move(self, origin_states, char):
        target_states = []
        for state in origin_states:
            for edge in state.edges:
                if(edge.in_char == char):
                    target_states.append(edge.target)
        return set(target_states)

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
    
    def e_closure_set(self, node_set):
        closure_set = set()
        for node in node_set:
            temp_closure = self.e_closure(node)
            closure_set.update(temp_closure)
        return closure_set