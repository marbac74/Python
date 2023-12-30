class Carta:
    """Rappresenta una carta da gioco
    attributi di classe: nomi_semi, nomi_valori
    attributi di istanza: seme, valore"""

    nomi_semi = ['Fiori', 'Quadri', 'Cuori', 'Picche']
    nomi_valori = [None, 'Asso', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Fante', 'Regina', 'Re']

    def __init__(self, seme=0, valore=2):
        self.seme = seme
        self.valore = valore

    def __str__(self):
        return '{} di {}'.format(Carta.nomi_valori[self.valore], Carta.nomi_semi[self.seme])