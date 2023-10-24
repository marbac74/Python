def prima(stringa):
    return stringa[0]

def ultima(stringa):
    return stringa[-1]

def mezzo(stringa):
    return stringa[1:-1]

def palindromo(stringa):
    if len(stringa) <= 1:
        return True
    if prima(stringa) != ultima(stringa):
        return False
    else:
        return palindromo(mezzo(stringa))

print(palindromo('allen'))
print(palindromo('bob'))
print(palindromo('otto'))
print(palindromo('redivider'))
print(palindromo('aa'))