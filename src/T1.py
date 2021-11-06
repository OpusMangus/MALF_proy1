from automatas.NDFA.thompson import startThompson
from automatas.DFA.transition_table import transition_table
from automatas.DFA.find_occurrences import find_ocurrences
from automatas.NDFA.NDFA_node import NDFA_node
from automatas.automata import automata
from regexParser.parser import get_sigma

def print_matches(matches):
    print('Ocurrencias:')
    for match in matches:
        print(' '.join(map(str, match)))

if (__name__ == '__main__'):
    regex = input()
    string = input()   

    if(regex == '~'):
        q0 = NDFA_node('q0')
        q1 = NDFA_node('q1', True)

        qList = [q0, q1]
        ndfa = automata(q0, qList, get_sigma(string))
    else:
        ndfa = startThompson(regex)
    
    ttSinRizos = transition_table(ndfa)
    dfaSinRizos = ttSinRizos.get_DFA()

    ndfa.add_rizos()
    ttConRizos = transition_table(ndfa)
    dfaConRizos = ttConRizos.get_DFA()

    ndfa.show('AFND')
    dfaConRizos.show('AFD')

    matches = find_ocurrences(dfaSinRizos, string)
    print_matches(matches)


