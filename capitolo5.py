def triangolo(lato1, lato2, lato3):
    if lato1 >= (lato2 + lato3) or lato2 >= (lato1 + lato3) or lato3 >= (lato1 + lato2):
        print('No')
    else:
        print('Sì')

def chiedi_utente():
    lato1 = input('Digita il valore del primo lato del triangolo: \n')
    lato1 = int(lato1)
    lato2 = input('Digita il valore del secondo lato: \n')
    lato2 = int(lato2)
    lato3 = input('Digita il valore del terzo lato: \n')
    lato3 = int(lato3)
    triangolo(lato1, lato2, lato3)
    rifare = input('Vuoi provare con un\'altra terna di numeri?\nInserisci 1 per continuare, 0 per terminare: ')
    if rifare == '0':
        return
    if rifare == '1':
        chiedi_utente()
    else:
        print('Spiacenti, input non valido')
        return

chiedi_utente()
    
    
        
