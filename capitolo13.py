import random

from dizionari import istogramma

def prepara_testo(in_text, out_text):
    file_in = open(in_text)
    file_out = open(out_text, 'w')
    line = 1
    for riga in file_in:
        if line < 250:
            line += 1
        else:
            riga = riga.lower()
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
            riga = riga.replace('--', ' ')
            riga = riga.replace('‘', ' ')
            riga = riga.replace('’', ' ') 
            file_out.write(riga)
    file_out.close()

def contaparole(in_file):
    fin = open(in_file)
    contaparole = 0
    for riga in fin:
        lista = riga.split()
        contaparole += len(lista)
    return contaparole

def vocabolario(in_file):
    fin = open(in_file)
    vocabolario = dict()
    for riga in fin:
        lista = riga.split()
        for parola in lista:
            vocabolario[parola] = vocabolario.get(parola, 0) + 1
    return vocabolario

def top20(in_file):
    vocab = vocabolario(in_file)
    top20 = []
    for item in vocab:
        if vocab[item] in sorted(vocab.values())[-20:]:
            top20.append({item:vocab[item]})
    return top20

def extravocab(text, vocab):
    parole_vocab = []
    parole_extra = []
    fin = open(vocab)
    for riga in fin:
        parola = riga.strip()
        parole_vocab.append(parola)
    txt = open(text)
    for riga in txt:
        lista = riga.split()
        for parola in lista:
            if parola not in parole_vocab:
                parole_extra.append(parola)
    return parole_extra

def estrai(stringa):
    isto = istogramma(stringa)
    isto_lista = []
    for elem in isto:
        isto_lista.extend([elem for i in range(isto[elem])])
    return random.choice(isto_lista)