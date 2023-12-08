def skip_gutenberg_info(file):
    filein = open(file)
    for line in filein:
        if line.startswith('*** START OF THE PROJECT'):
            break
    fileout = open('output.txt', 'w')
    for line in filein:
        if line.startswith('            *** END OF THE PROJECT'):
            break
        fileout.write(line)
    fileout.close()
    return True