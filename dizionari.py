def istogramma(stringa):
    d = dict()
    for c in stringa:
        d[c] = d.get(c, 0) + 1
    return d

def stampa_isto(isto):
    for item in isto:
        print(item, isto[item])

def lookup_inverso(dict, value):
    for key in dict:
        if dict[key] == value:
            return key
    raise LookupError('Il valore non compare nel dizionario')

def inverti_dict(diz):
    inverso = dict()
    for chiave in diz:
        valore = diz[chiave]
        if valore not in inverso:
            inverso[valore] = [chiave]
        else:
            inverso[valore].append(chiave)
    return inverso

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)