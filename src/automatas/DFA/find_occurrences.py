def find_ocurrences(DFA, string):
    matches = []

    i = 0
    while i < len(string):
        match_end_index = sub_string_max_match(DFA, string[i:])
        if(match_end_index > -1):
            matches.append([i, i + match_end_index])
            i = i + match_end_index + 1
        else:
            i += 1

    return matches

def sub_string_max_match(DFA, substring):
    start_node = DFA.start_node
    node_stack = []
    char_stack = list(substring)

    node_stack.append(start_node)
    max_final_pos = -1
    
    char_count = -1
    for char in char_stack:
        if(len(node_stack) > 0): #Se llega a un nodo nuevo (puede ser el inicial)
            current_node = node_stack.pop()
            
            if current_node.final: #Si es un nodo final, se reemplaza la actual posición máxima de match
                max_final_pos = char_count
            for edge in current_node.edges: #Se busca si se puede llegar a otro nodo con el caracter consumido
                if edge.in_char == char: #Se consume un caracter
                    node_stack.append(edge.target)
                    char_count += 1
                    break
        else: #Se llega a un estado sin salida
            return max_final_pos

    if(len(node_stack) > 0):
        current_node = node_stack.pop()  #Nodo luego de consumir todos los caracteres  
        if current_node.final: #Si es un nodo final, se reemplaza la actual posición máxima de match
            max_final_pos = char_count

    return max_final_pos