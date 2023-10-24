def una_minuscola1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def una_minuscola2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def una_minuscola3(s):
    flag = None
    for c in s:
        flag = c.islower()
    return flag

def una_minuscola4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def una_minuscola5(s):
    for c in s:
        if not c.islower():
            return False
    return True

def ruota_lettera(lettera, n):
    """Ruota una lettera di n posizioni.  Non cambia gli altri caratteri.

    lettera: una stringa di un solo carattere
    n: un intero

    Valore di ritorno: una stringa di un carattere
    """
    if lettera.isupper():
        inizio = ord('A')
    elif lettera.islower():
        inizio = ord('a')
    else:
        return lettera

    c = ord(lettera) - inizio
    i = (c + n) % 26 + inizio
    return chr(i)


def ruota_parola(parola, n):
    """Ruota una parola di n posizioni.

    parola: una stringa
    n: un intero (positivo o negativo)

    Valore di ritorno: una nuova stringa
    """
    nuova = ''
    for lettera in parola:
        nuova += ruota_lettera(lettera, n)
    return nuova