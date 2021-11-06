from .operators import union
from .operators import klean
from .operators import conc
from .operators import posit
from automatas.NDFA.NDFA_edge import NDFA_edge
from automatas.NDFA.NDFA_node import NDFA_node
from automatas.automata import automata
from regexParser.parser import get_sigma
from regexParser.infixToPostfix import infixToPostfix

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
        elif(c=='.'):
            lista_Trans, pila_I, pila_F = conc(lista_Trans, pila_I, pila_F)
    
    return lista_Trans, pila_I, pila_F


def createGraph(pila_I, pila_F, lista_Trans):
    qList = []
    #create nodes
    for i in range(pila_F[len(pila_F)-1]+1):
       q = NDFA_node('q'+str(i))
       qList.append(q)
    #add edges for graph
    for i in range(len(lista_Trans)):
        edge = lista_Trans[i]
        nfda_edge = NDFA_edge(edge[1], qList[int(edge[2])])
        qList[int(edge[0])].edges.append(nfda_edge)
    
    qList[pila_F[1]].final = True 
    return qList 


def startThompson(expresion):
    #1.- convert infix to postfix
    #lpos,alfabeto,pila = infixToPostfix(expresion)
    lpos = list(infixToPostfix(expresion))
    alfabeto = list(get_sigma(expresion))

    #print("Notacion posfija \n")
    #print(lpos)
    #2.- see alphabet
    for j in range(len(alfabeto)-1, -1, -1):
        if alfabeto[j] in alfabeto[:j]:
            # print lista_a
            del(alfabeto[j])

    #print("Alfabeto:\n")
    #print(alfabeto)
    #print("\n")
    #3.- apply thompson
    lista_Trans, pila_I, pila_F = thompson(lpos)
    #print("lista thompson\n\n")
    #print(lista_Trans)
    #print("\n")
    #startup node
    #print("inicio\n")
    #print(pila_I,)
    #print("\n")
    #end node
    #print("Fin\n")
    #print(pila_F,)

    #4.- Create graph
    qList = createGraph(pila_I,pila_F, lista_Trans)
    aut1 = automata(qList[int(pila_I[1])], qList, set(alfabeto))
    #aut1.show('AFND')
    return aut1

