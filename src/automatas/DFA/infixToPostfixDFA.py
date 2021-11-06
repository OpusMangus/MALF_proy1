
def operator(i):
    if pila == [] or pila[len(pila)-1] == "(" or i == "(":
        pila.append(i) 
    elif i == "+" or i == "*":
        if pila[len(pila)-1] == "+" or pila[len(pila)-1] == "*":
            lpos.append(i)
        else:
            pila.append(i)
    elif i == "-":
        #print "len(pila)"
        #print len(pila)

        while pila[len(pila)-1] == "+" or pila[len(pila)-1] == "*":
            lpos.append(pila.pop())
            #print len(pila)
        if pila[len(pila)-1] == "-":
            lpos.append(i)
        else:
            pila.append(i)
    elif i == "|":
        while pila[len(pila)-1] == "+" or pila[len(pila)-1] == "*" or pila[len(pila)-1] == "-":
            lpos.append(pila.pop())
        if pila[len(pila)-1] == "|":
            lpos.append(i)
        else:
            pila.append(i)
    else:
        while pila[len(pila)-1] != "(":
            lpos.append(pila.pop())
        pila.pop()


def addOperator():
    while len(pila) > 1:
        lpos.append(pila.pop())


lpos = []
alfabeto = []
pila = ['n']

def infixToPostFix(expresion):
    for i in expresion:
    #comprueba que sea una letra mayuscula o minuscula
        if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
            lpos.append(i)
            #save letter
            alfabeto.append(i)
        #si es klean(*), union(|), posit(+) o conc(-)
        else:
           operator(i)
    #load operator at the end
    addOperator()
    return lpos,alfabeto,pila