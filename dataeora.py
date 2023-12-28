import datetime

def to_string(int):
    """ Traduce in una stringa di tre caratteri il numero da 0 a 6
    che si riferisce al corrispondente giorno della settimana
    """
    giorni = ('Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom')
    enumerato = enumerate(giorni)
    for indice, giorno in enumerato:
        if indice == int:
            return giorno
        
def calcola_età(data_nascita):
    """ La funzione riceve come input una stringa con una 
    data di nascita e stampa l'età rispetto al tempo attuale
    di chi ha inserito la data e il numero di giorni, ore, 
    minuti e secondi che mancano al prossimo compleanno
    """
    nascita = datetime.datetime.strptime(data_nascita, '%d %m %Y')
    oggi = datetime.datetime.today()
    timedelta_obj = oggi - nascita
    anni, giorni = divmod(timedelta_obj.days, 365)
    print('Hai %d anni e %d giorni d\'età' % (anni, giorni))

def main():
    ora = datetime.datetime.now()
    print('Data:\t', to_string(ora.weekday()), ora.day, ora.month, ora.year)
    print('Ora:\t %.2d:%.2d:%.2d' % (ora.hour, ora.minute, ora.second))

if __name__ == '__main__':
    main()