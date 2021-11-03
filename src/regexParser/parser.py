from .infixToPostfix import infixToPostfix
from .postfixToTree import constructTree


def parse(infixRegex):
    postfix = infixToPostfix(infixRegex)
    expressionTreeRoot = constructTree(postfix)
    return expressionTreeRoot

def get_sigma(regex):
    postfix = infixToPostfix(regex)
    tmp = postfix.replace('.', '')
    tmp = tmp.replace('|', '')
    tmp = tmp.replace('*', '')
    if(tmp == ''):
        return
    sigma = set(tmp)
    return sigma