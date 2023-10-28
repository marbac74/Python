import time

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

def inverti_diz(diz):
    inverso = dict()
    for chiave in diz:
        valore = diz[chiave]
        inverso.setdefault(valore, []).append(chiave)
    return inverso

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

memo = {0:0, 1:1}

def memo_fibonacci(n):
    
    if n in memo:
        return memo[n]
    
    res = memo_fibonacci(n - 1) + memo_fibonacci(n - 2)
    memo[n] = res
    return res

start = time.time()
fibonacci(42)
print("Per calcolare fibonacci(42) sono passati ", time.time() - start, " secondi") 

second_start = time.time()
memo_fibonacci(42)
print("Per calcolare memo_fibonacci(42) sono passati ", time.time() - second_start, " secondi")

def controlla(stringa):
    inputfile = open('words.txt')
    dizionario = dict()
    for riga in inputfile:
        parola = riga.strip()
        dizionario[parola] = 'inserted'
    if stringa in dizionario:
        return True
    else:
        return False