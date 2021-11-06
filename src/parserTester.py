from regexParser.infixToPostfix import infixToPostfix
from automatas.NDFA.thompson import startThompson
from automatas.DFA.transition_table import transition_table

def inorder(t):
    if t is not None:
        inorder(t.left)
        print(t.value, end='')
        inorder(t.right)


regex = '(a.b)*'
pf = infixToPostfix(regex)
#print(list(pf))
aut1 = startThompson(regex)

aut1.add_rizos()
aut1.show('NDFA:')
tt = transition_table(aut1)
aut2 = tt.get_DFA()
aut2.show('DFA:')
