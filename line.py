# CMD decoration functions for the main program

from math import floor

def line(symbol, count, **options):
    # Start and end symbols:
    if 'points' in options:
        symbol_end = options.get('points', '')
    else:
        symbol_end = ''
    
    # Symbol intermediate
    if 'intr' in options:
        symbol_intr = options.get('intr', '')
    else:
        symbol_intr = ''
    
    # Edge X:
    if 'x' in options:
        edge_x = options.get('x', 0)

        # Convert the variable to int:
        if not isinstance(edge_x, int):
            try:
                edge_x = int(edge_x)
            except ValueError:
                edge_x = 0
    else:
        edge_x = 0
    
    # Point left:
    symbol_left = options.get('left', '')
    
    # Point right:
    symbol_right = options.get('right', '')
    
    # Edge Y:
    if 'y' in options:
        edge_y = options.get('y', 0)

        # Convert the variable to int:
        if not isinstance(edge_y, int):
            try:
                edge_y = int(edge_y)
            except ValueError:
                edge_y = 0
    else:
        edge_y = 0
    
    # Next lines:
    if 'next' in options:
        next_line = options.get('next', 1)

        # Convert the variable to int:
        if not isinstance(next_line, int):
            try:
                next_line = int(next_line)
            except ValueError:
                next_line = 1
        
        # Check the count:
        if next_line < 0:
            next_line = 0
    else:
        next_line = 1
    
    # Switch:
    switch = options.get('switch', 0)
    
    # Check the count:
    if isinstance(count, int):
        count = 1 if count < 1 else count
    else:
        count = 1
    
    # Less length:
    less = options.get('less', False)

    count = (count - floor(count / 2)) if less == True else count

    # Show the line 1/2:
    print(('\n' * edge_y), (' ' * edge_x), symbol_left, symbol_end, end='', sep='')

    # Show the line 2/2:
    if count > 1 and symbol_intr != '':
        if switch == True:
            print((f'{symbol}{symbol_intr}') * (count - 1), symbol, symbol_end, symbol_right, end=('\n' * next_line), sep='')
        else:
            print((f'{symbol_intr}{symbol}') * (count - 1), symbol_intr, symbol_end, symbol_right, end=('\n' * next_line), sep='')
    else:
        print(symbol * count, symbol_end, symbol_right, end=('\n' * next_line), sep='')
