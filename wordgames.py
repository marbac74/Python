def niente_e(parola):
    for lettera in parola:
        if lettera == 'e':
            return False
    return True

def evita(parola, vietate):
    for lettera in parola:
        if lettera in vietate:
                return False
    return True

def usa_solo(parola, letteredausare):
    for lettera in parola:
        if lettera not in letteredausare:
                return False
    return True

def usa_tutte(parola, richieste):
    for lettera in richieste:
        if lettera not in parola:
            return False
    return True               

def alfabetica(parola):
    contatore = 0
    while contatore < (len(parola) - 1):
        if parola[contatore] > parola[contatore + 1]:
            return False
        contatore = contatore + 1
    return True

def tre_doppie(parola):
    conta_doppie = 0
    indice = 0
    while indice < (len(parola) - 1):
        if parola[indice] == parola[indice + 1]:
            conta_doppie = conta_doppie + 1
            if conta_doppie == 3:
                return True
            indice = indice + 2
        else:
            indice = indice + 1 - 2 * conta_doppie
            conta_doppie = 0
    return False

def ha_palindromo(intero, inizio, lunghezza):
    """Controlla se la rappresentazione a stringa di intero ha un palindromo
    intero: un intero
    inizio: posizione di partenza nella stringa
    lunghezza: lunghezza del palindromo da controllare
    """
    stringa = str(intero)[inizio:inizio+lunghezza]
    if stringa[::-1] == stringa:
        return True
    else:
        return False

    
def controlla(intero):
    if (ha_palindromo(intero, 2, 4) and
        ha_palindromo(intero+1, 1, 5) and
        ha_palindromo(intero+2, 1, 4) and
        ha_palindromo(intero+3, 0, 6)):
        return True
    else:
        return False

def controlla_tutti():
    """Enumera i numeri a sei cifre e stampa quelli che superano il test
    """
    intero = 100000
    while intero <= 999996:
        if controlla(intero):
            print(intero)
        intero = intero + 1

def stringa_verificata(stringa):
    if stringa.startswith('0'):
        return stringa[1:]
    else:
        return stringa

def genera_coppie_età(differenza):
    """Genera coppie di età palindromiche a due cifre comprese tra 00 e 99"""

    print('Daughter\'s age', ' ', 'Mother\'s age')

    intero = 0

    while intero < 100:

        stringa = str(intero)

        if len(stringa) < 2:
            stringa = stringa.zfill(2)

        accoppiate = stringa + stringa[::-1]

        if accoppiate == accoppiate[::-1] and eval(stringa_verificata(accoppiate[2:4])) - eval(stringa_verificata(accoppiate[0:2])) == differenza:
            print(accoppiate[0:2], '\t\t', accoppiate[2:4])

        intero = intero + 1

for i in range(18, 46, 9):
    genera_coppie_età(i)
    print()


"""
wordcount = 0
words_without_e = 0

for riga in input_file:
    wordcount = wordcount + 1
    if niente_e(riga):
        words_without_e = words_without_e + 1

percentage = words_without_e / wordcount
print(percentage)
"""