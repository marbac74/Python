frutto = 'pompelmo'
prefissi = 'JKLMNOPQ'
suffisso = 'ack'

def palindromo(stringa):
    if stringa[::-1] == stringa:
        return True
    else:
        return False

def ordine_inverso(stringa):
    indice = -1
    while indice >= -(len(stringa)):
        lettera = stringa[indice]
        print(lettera)
        indice = indice - 1

for lettera in prefissi:
    if lettera == 'O' or lettera == 'Q':
        print(lettera + 'u' + suffisso)
    else:
        print(lettera + suffisso)

def trova(parola, lettera, inizio):
    indice = inizio
    while indice < len(parola):
        if parola[indice] == lettera:
            return indice
        indice = indice + 1
    return -1

def conta(parola, lettera):
    contatore = 0
    for car in parola:
        if car == lettera:
            contatore = contatore + 1
    print(contatore)

def al_contrario(parola1, parola2):
    if len(parola1) != len(parola2):
        return False
    
    i = 0
    j = len(parola1) - 1

    while j >= 0:
        if parola1[i] != parola2[j]:
            return False
        i = i + 1
        j = j - 1
    return True