def union(elem1, elem2, lista_Trans, pila_I, pila_F):
    ini = elem1
    fin = elem2
    in1 = pila_I.pop()
    in2 = pila_I.pop()
    f1 = pila_F.pop()
    f2 = pila_F.pop()
    inicio = ini
    f = fin
    lista_Trans.append([str(inicio), '_', str(in1)])
    lista_Trans.append([str(inicio), '_', str(in2)])
    lista_Trans.append([str(f1), '_', str(f)])
    lista_Trans.append([str(f2), '_', str(f)])
    pila_I.append(inicio)
    pila_F.append(f)
    
    return lista_Trans, pila_I, pila_F

def klean(elem1, elem2, lista_Trans, pila_I, pila_F):
    ini = elem1
    fin = elem2

    ini1 = pila_I.pop()
    fin1 = pila_F.pop()

    lista_Trans.append([str(ini), '_', str(fin)])
    lista_Trans.append([str(ini), '_', str(ini1)])
    lista_Trans.append([str(fin1), '_', str(ini1)])
    lista_Trans.append([str(fin1), '_', str(fin)])

    pila_I.append(ini)
    pila_F.append(fin)

    return lista_Trans, pila_I, pila_F

def posit(elem1, elem2, lista_Trans, pila_I, pila_F):
    ini = elem1
    fin = elem2
    ini1 = pila_I.pop()
    fin1 = pila_F.pop()

    lista_Trans.append([str(ini), '_', str(ini1)])
    lista_Trans.append([str(fin1), '_', str(ini1)])
    lista_Trans.append([str(fin1), '_', str(fin)])

    pila_I.append(ini)
    pila_F.append(fin)

    return lista_Trans, pila_I, pila_F

def sust(elem1, elem2, lista_Trans):
    for i in lista_Trans:
        print("i: "+str(i))
        print("elem2: "+str(elem2))
        print("elem1: ")
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

def conc2(lista_Trans, pila_I, pila_F):
    print("pilaInicio"+str(pila_I))
    print("pilaFin"+str(pila_F))
    print("---------------------------")
    ini = pila_I.pop()
    fin = pila_I.pop()
    ini1 = pila_F.pop()
    fin1 = pila_F.pop()
    lista_Trans.append([str(ini), '_', str(ini1)])
    lista_Trans.append([str(fin1), '_', str(ini1)])
    lista_Trans.append([str(fin1), '_', str(fin)])

    pila_I.append(ini)
    pila_F.append(fin)