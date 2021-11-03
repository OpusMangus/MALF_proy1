from .infixToPostfix import infixToPostfix
from .postfixToTree import constructTree


def parse(infixRegex):
    postfix = infixToPostfix(infixRegex)
    expressionTreeRoot = constructTree(postfix)
    return expressionTreeRoot
