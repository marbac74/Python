def istogramma(stringa):
    d = dict()
    for c in stringa:
        d[c] = d.get(c, 0) + 1
    return d

def stampa_isto(isto):
    for item in isto:
        print(item, isto[item])