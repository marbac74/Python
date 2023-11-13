import string

punteggiatura = string.punctuation
spaziatura = string.whitespace

def read_and_strip(text):
    fin = open(text)
    for riga in fin:
        riga = riga.strip()
        riga = riga.lower()
        riga = riga.replace('.', '')
        riga = riga.replace(',', '')
        riga = riga.replace(';', '')
        riga = riga.replace(':', '')
        riga = riga.replace('!', '')
        riga = riga.replace('?', '')
        riga = riga.replace('(', '')
        riga = riga.replace(')', '')
        riga = riga.replace('“', '')
        riga = riga.replace('”', '')
        riga = riga.replace('«', '')
        riga = riga.replace('»', '')
        riga = riga.replace('…', '')
        riga = riga.replace('‘', ' ')
        riga = riga.replace('’', ' ')
        print(riga)