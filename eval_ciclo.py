def eval_ciclo():
    while True:
        riga = input('Immetti un\'espressione da valutare: ')
        if (riga == 'fatto'):
            break
        else:
            print(eval(riga))
    print(riga)

eval_ciclo()