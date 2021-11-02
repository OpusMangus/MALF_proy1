from regexParser.parser import parse


def inorder(t):
    if t is not None:
        inorder(t.left)
        print(t.value, end='')
        inorder(t.right)


regex = '(a.b)*'

t = parse(regex)
inorder(t)
