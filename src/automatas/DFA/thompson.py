from .operators import union
from .operators import klean
from .operators import conc
from .operators import posit
from .infixToPostfixDFA import infixToPostFix
from automatas.NDFA.NDFA_edge import NDFA_edge
from automatas.NDFA.NDFA_node import NDFA_node


def thompson(cadena):
    cont=0
    cont2=1
    lista_Trans = []
    pila_I = ['n']
    pila_F = ['n']
    for c in cadena: 
        if((ord(c)>=97 and ord(c)<=122) or (ord(c)>=65 and ord(c)<=90) or (ord(c)>=48 and ord(c)<=57)):
            lista_Trans.append([str(cont),c,str(cont2)])
            pila_I.append(cont)
            pila_F.append(cont2)
            cont=cont+2
            cont2=cont2+2
				
        elif(c=='*'):
            lista_Trans, pila_I, pila_F = klean(cont, cont2,lista_Trans, pila_I, pila_F)
            cont=cont+2
            cont2=cont2+2
        elif(c=='|'):
            lista_Trans, pila_I, pila_F = union(cont, cont2,lista_Trans, pila_I, pila_F)
            cont=cont+2
            cont2=cont2+2
        elif(c=='+'):
            lista_Trans, pila_I, pila_F = posit(cont, cont2,lista_Trans, pila_I, pila_F)
            cont=cont+2
            cont2=cont2+2
        elif(c=='-'):
            lista_Trans, pila_I, pila_F = conc(lista_Trans, pila_I, pila_F)
    
    return lista_Trans, pila_I, pila_F


def createGraph(pila_I, pila_F, lista_Trans):
    qList = []
    #create nodes
    for i in range(pila_F[len(pila_F)-1]):
       q = NDFA_node(''.join(i))
       qList.append(q)
    #add edges for graph
    for i in range(len(lista_Trans)):
        edge = lista_Trans[i]
        qList[int(edge[0])] = NDFA_edge(edge[1], edge[len(edge)-1])
        qList[int(edge[0])].target = edge[len(edge)-1]

    return qList 


def startThompson(expresion):
    #1.- convert infix to postfix
    lpos,alfabeto,pila = infixToPostFix(expresion)
    print("Notacion posfija \n")
    print(lpos)
    #2.- see alphabet
    for j in range(len(alfabeto)-1, -1, -1):
        if alfabeto[j] in alfabeto[:j]:
            # print lista_a
            del(alfabeto[j])

    print("Alfabeto:\n")
    print(alfabeto)
    print("\n")
    #3.- apply thompson
    lista_Trans, pila_I, pila_F = thompson(lpos)
    print("lista thompson\n\n")
    print(lista_Trans)
    print("\n")
    #startup node
    print("inicio\n")
    print(pila_I,)
    print("\n")
    #end node
    print("Fin\n")
    print(pila_F,)

    #4.- Create graph
    qList = createGraph(pila_I,pila_F, lista_Trans)

