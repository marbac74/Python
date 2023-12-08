from tuple import anagram_set
import shelve

def arch_anagrammi(stringa):
    """ La funzione chiama la funzione anagram_set e
    archivia la lista di anagrammi ottenuta in uno shelf 
    """
    anagrammi = anagram_set(stringa)
    try:
        db = shelve.open('anagrammi', 'c')
    except IOError:
        print('Errore apertura file: \'anagrammi\' non può essere aperto in scrittura')
    else:
        db[stringa] = anagrammi
        db.close()

def leggi_anagrammi(stringa):
    """ La funzione cerca la stringa nel database 'anagrammi'
    e, se presente, restituisce la lista dei suoi anagrammi
    """
    try:
        db = shelve.open('anagrammi', 'r')
    except IOError:
        print('Errore apertura file: \'anagrammi\' non può essere aperto in lettura')
    else:
        return db[stringa]