def justify(string, l_tab, r_tab):
    left = l_tab + len(string)
    right = r_tab - len(string)
    in_between = right - left
    print(' ' * l_tab, string, ' ' * in_between, string)

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end=' ')

def print_post():
    print('|        ', end=' ')

def print_beams():
    do_four(print_beam)
    print('+')

def print_posts():
    do_four(print_post)
    print('|')

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_four(print_row)
    print_beams()

print_grid()
