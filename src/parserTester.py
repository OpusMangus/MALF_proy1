from regexParser.parser import parse
from automatas.DFA.thompson import startThompson

def inorder(t):
    if t is not None:
        inorder(t.left)
        print(t.value, end='')
        inorder(t.right)


regex = '(a.b)'
startThompson(regex)
t = parse(regex)
inorder(t)
