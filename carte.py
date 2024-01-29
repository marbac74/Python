import random

class Carta:
    """Rappresenta una carta da gioco
    attributi di classe: nomi_semi, nomi_valori
    attributi di istanza: seme, valore"""

    nomi_semi = [None, 'Fiori', 'Quadri', 'Cuori', 'Picche']
    nomi_valori = [None, 'Asso', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Fante', 'Regina', 'Re']

    def __init__(self, seme=0, valore=2):
        self.seme = seme
        self.valore = valore

    def __str__(self):
        return '{} di {}'.format(Carta.nomi_valori[self.valore], Carta.nomi_semi[self.seme])
    
    def __lt__(self, other):
        if self.seme < other.seme:
            return True
        elif self.seme > other.seme:
            return False
        else:
            return self.valore < other.valore

class Mazzo:
    """Rappresenta un mazzo di carte
    attributi: None"""

    def __init__(self):
        self.carte = []
        for seme in range(1, 5):
            for valore in range(1, 14):
                carta = Carta(seme, valore)
                self.carte.append(carta)
    
    def __str__(self):
        res = []
        for carta in self.carte:
            res.append(str(carta))
        return '\n'.join(res)
    
    def togli_carta(self):
        return self.carte.pop()
    
    def aggiungi_carta(self, carta):
        self.carte.append(carta)
    
    def mescola(self):
        random.shuffle(self.carte)

    def ordina(self):
        self.carte.sort()

class Mano(Mazzo):
    """Rappresenta una mano di carte da gioco"""

    def __init__(self, label=''):
        self.carte = []
        self.label = label