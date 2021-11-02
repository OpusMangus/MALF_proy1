from regexParser.parser import parse


def preorder(t):
    if t is not None:
        print(t.value, end='')
        preorder(t.left)
        preorder(t.right)


def inorder(t):
    if t is not None:
        inorder(t.left)
        print(t.value, end='')
        inorder(t.right)


def postorder(t):
    if t is not None:
        postorder(t.left)
        postorder(t.right)
        print(t.value, end='')


regex = '(p*|(a.c*.b))*'

t = parse(regex)
print('preorder: ', end='')
preorder(t)
print()
print('inorder: ', end='')
inorder(t)
print()
print('postorder: ', end='')
postorder(t)
print()
