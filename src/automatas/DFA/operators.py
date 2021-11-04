def union(elem1, elem2, lista_Trans, pila_I, pila_F):
    ini = elem1
    fin = elem2
    in1 = pila_I.pop()
    in2 = pila_I.pop()
    f1 = pila_F.pop()
    f2 = pila_F.pop()
    inicio = ini
    f = fin
    lista_Trans.append([str(inicio), '@', str(in1)])
    lista_Trans.append([str(inicio), '@', str(in2)])
    lista_Trans.append([str(f1), '@', str(f)])
    lista_Trans.append([str(f2), '@', str(f)])
    pila_I.append(inicio)
    pila_F.append(f)
    
    return lista_Trans, pila_I, pila_F

def klean(elem1, elem2, lista_Trans, pila_I, pila_F):
    ini = elem1
    fin = elem2

    ini1 = pila_I.pop()
    fin1 = pila_F.pop()

    lista_Trans.append([str(ini), '@', str(fin)])
    lista_Trans.append([str(ini), '@', str(ini1)])
    lista_Trans.append([str(fin1), '@', str(ini1)])
    lista_Trans.append([str(fin1), '@', str(fin)])

    pila_I.append(ini)
    pila_F.append(fin)

    return lista_Trans, pila_I, pila_F

def posit(elem1, elem2, lista_Trans, pila_I, pila_F):
    ini = elem1
    fin = elem2
    ini1 = pila_I.pop()
    fin1 = pila_F.pop()

    lista_Trans.append([str(ini), '@', str(ini1)])
    lista_Trans.append([str(fin1), '@', str(ini1)])
    lista_Trans.append([str(fin1), '@', str(fin)])

    pila_I.append(ini)
    pila_F.append(fin)

    return lista_Trans, pila_I, pila_F

def sust(elem1, elem2, lista_Trans):
    for i in lista_Trans:
        if i[0] == str(elem2):
            i[0] = str(elem1)

    return lista_Trans
    
def conc(lista_Trans, pila_I, pila_F):
    ini1 = pila_I.pop()
    ini2 = pila_I.pop()
    fin1 = pila_F.pop()
    fin2 = pila_F.pop()
    lista_Trans = sust(fin2, ini1, lista_Trans)
    pila_I.append(ini2)
    pila_F.append(fin1)

    return lista_Trans, pila_I, pila_F