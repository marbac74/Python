def countlines(filename):
    counter = 0
    for line in open(filename):
        counter += 1
    return counter

def sed(modello, sostituto, file1, file2):
    """ La funzione legge file1 e ne riscrive il contenuto
    in file2. Se la stringa modello compare in file1, essa
    viene sostituita dalla stringa sostituto in file2
    """

    fin = open(file1, 'r')
    fout = open(file2, 'w')
    
    # Viene usato un loop per leggere le righe del file
    
    for line in fin:
        if modello in line.lower():
            line = line.lower().replace(modello, sostituto)
        fout.write(line)
    
    fin.close()
    fout.close()

if __name__ == '__main__':
    print(countlines('cl.py'))