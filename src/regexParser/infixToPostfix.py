# Basado en https://gist.github.com/DmitrySoshnikov/1239804
# Por Dmitry Soshnikov

# Entrada: Lista de elementos no vacía
# Salida: Valor del último elemento de la lista
def peek(list):
    return list[len(list)-1]


#Entrada: Caracter
# Salida: Entero que representa precedencia del caracater en una expresión regular (menor número, mayor presedencia)
def precedenceOf(char):
    if char == '(':
        return 1
    elif char == '|':
        return 2
    elif char == '.':
        return 3
    elif char == '*':
        return 4
    else:
        return 5


# Entrada: String de expresión regular infix
# Salida: String de expresión regular postfix
def infixToPostfix(regexString):
    output = []
    stack = []

    strLen = len(regexString)

    for x in range(strLen):
        currentChar = regexString[x]

        if currentChar == '(':
            stack.append(currentChar)
        elif currentChar == ')':
            while len(stack) > 0 and peek(stack) != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while len(stack):
                peekedChar = peek(stack)

                peekedCharPrecedence = precedenceOf(peekedChar)
                currentCharPrecedence = precedenceOf(currentChar)

                if peekedCharPrecedence >= currentCharPrecedence:
                    output.append(stack.pop())
                else:
                    break
            stack.append(currentChar)

    while len(stack):
        output.append(stack.pop())

    return ''.join(output)
