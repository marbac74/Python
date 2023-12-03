def somma_nidificata(lista):
    somma = 0
    for sottolista in lista:
        somma += sum(sottolista)
    return somma

def somma_cumulata(lista):
    somma = 0
    output = []
    for el in lista:
        nuovo = el + somma
        somma += el
        output.append(nuovo)
    return output

def mediani(lista):
    del lista[0]
    del lista[len(lista) - 1]
    return lista

def tronca(lista):
    del lista[0]
    lista.pop()
    return None

def ordinata(lista):
    index = 0
    while index < len(lista) - 1:
        if lista[index] > lista[index + 1]:
            return False
        index += 1
    return True

def anagramma(stringa1, stringa2):
    lista1 = list(stringa1)
    lista2 = list(stringa2)
    if len(lista1) != len(lista2):
        return False
    elif len(lista1) == len(lista2):
        for char in lista1:
            if char not in lista2:
                return False
            lista2.remove(char)
        return True
    
def ha_duplicati(lista):
    già_incontrati = []
    for el in lista:
        if el in già_incontrati:
            return True
        già_incontrati.append(el)
    return False

def wordlist1(inputfile):
    input = open(inputfile)
    lista = []
    for riga in input:
        parola = riga.strip()
        lista.append(parola)
    return len(lista)

def wordlist2(inputfile):
    input = open(inputfile)
    lista = []
    for riga in input:
        parola = riga.strip()
        lista = lista + [parola]
    return len(lista)

def bisezione(lista_parole, parola_da_cercare):
    ordinata = sorted(lista_parole)
    while len(ordinata) != 0:
        n = len(ordinata) // 2
        parola_mediana = ordinata[n]
        if parola_da_cercare == parola_mediana:
            return True
        elif parola_da_cercare < parola_mediana:
            ordinata = ordinata[:n]
        elif parola_da_cercare > parola_mediana:
            ordinata = ordinata[n+1:]
    return False