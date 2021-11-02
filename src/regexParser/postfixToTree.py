from .expressionTreeNode import treeNode


def isOperator(char):
    if char == '|' or char == '.' or char == '*':
        return True
    else:
        return False


def isKleene(char):
    if char == '*':
        return True
    else:
        return False


def constructTree(postfix):
    stack = []

    for char in postfix:
        t = treeNode(char)
        if not isOperator(char):
            stack.append(t)
        else:
            if isKleene(char):
                node = stack.pop()

                t.left = node
            else:
                nodeRight = stack.pop()
                nodeLeft = stack.pop()

                t.right = nodeRight
                t.left = nodeLeft
            stack.append(t)

    root = stack.pop()
    return root
