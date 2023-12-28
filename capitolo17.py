def int_in_tempo(secondi):
    tempo = Tempo()
    minuti, tempo.secondi = divmod(secondi, 60) # type: ignore
    tempo.ore, tempo.minuti = divmod(minuti, 60) # type: ignore
    return tempo

class Tempo:
    """Rappresenta un'ora del giorno
    attributi: ore, minuti, secondi"""

    def __init__(self, ore=0, minuti=0, secondi=0):
        self.ore = ore
        self.minuti = minuti
        self.secondi = secondi

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.ore, self.minuti, self.secondi)
    
    def in_int(self):
        minuti = self.ore * 60 + self.minuti
        secondi = minuti * 60 + self.secondi
        return secondi
    
    def incremento(self, secondi):
        secondi += self.in_int()
        return int_in_tempo(secondi)
    
    def viene_dopo(self, other):
        return self.in_int() > other.in_int()
    
class Canguro:
    """Rappresenta un oggetto-canguro:
    attributi: nome, contenuto_tasca"""

    def __init__(self, nome=None, contenuto_tasca=None):
        """Inizializza un oggetto-canguro, ha due parametri opzionali:
        una stringa nome (default=None), una lista contenuto_tasca (default=None)"""
        self.nome = nome
        if contenuto_tasca == None:
            contenuto_tasca = []
        self.contenuto_tasca = contenuto_tasca

    def __str__(self):
        """Restituisce una stringa di una tupla col nome del canguro e il contenuto della sua tasca"""
        return '(%s, %s)' % (self.nome, self.contenuto_tasca)

    def intasca(self, oggetto):
        """Aggiunge un oggetto al contenuto della tasca del canguro"""
        self.contenuto_tasca.append(oggetto)