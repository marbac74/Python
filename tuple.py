from dizionari import istogramma, inverti_diz
from liste import anagramma
import janus_swi as janus

def sommatutto(*args):
    return sum(args)

def somma_pos_neg(lista):
    somma_pos = 0
    somma_neg = 0
    zero_counter = 0
    for item in lista:
        if item > 0:
            somma_pos += item
        elif item < 0:
            somma_neg += item
        else:
            zero_counter += 1
    return somma_pos, somma_neg, zero_counter

def corrispondenza(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False

def più_frequente(stringa):
    char_freq = istogramma(stringa)
    freq_dict = inverti_diz(char_freq)
    for item in janus.apply_once("tuple", "flatten", list(freq_dict.values())):
        print(item)

def anagram_set(stringa):
    output_dict = dict()
    anagrammabili = []
    input_file = open('words.txt')
    for riga in input_file:
        parola = riga.strip()
        if anagramma(parola, stringa):
            anagrammabili.append(parola)
    output_dict[stringa] = anagrammabili
    return janus.apply_once("tuple", "flatten", list(output_dict.values()))

def stampa_anagrammi():
    d = dict()
    for item in ['deltas', 'retainers', 'generating', 'resmelts']:
        d[item] = anagram_set(item)
    for el in d:
        print(d[el])