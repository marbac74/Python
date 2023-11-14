import string

punteggiatura = string.punctuation
spaziatura = string.whitespace

def read_and_strip(in_text, out_text):
    file_in = open(in_text)
    file_out = open(out_text, 'w')
    for riga in file_in:
        riga = riga.lower()
        riga = riga.replace('\t', '')
        riga = riga.replace('\r', '')
        riga = riga.replace('\x0b', '')
        riga = riga.replace('\x0c', '')
        riga = riga.replace('.', '')
        riga = riga.replace(',', '')
        riga = riga.replace(';', '')
        riga = riga.replace(':', '')
        riga = riga.replace('!', '')
        riga = riga.replace('?', '')
        riga = riga.replace('(', '')
        riga = riga.replace(')', '')
        riga = riga.replace('"', '')
        riga = riga.replace('“', '')
        riga = riga.replace('”', '')
        riga = riga.replace('«', '')
        riga = riga.replace('»', '')
        riga = riga.replace('…', '')
        riga = riga.replace('\'', '')
        riga = riga.replace('‘', ' ')
        riga = riga.replace('’', ' ')
        file_out.write(riga)
    file_out.close()