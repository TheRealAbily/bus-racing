# CMD text control functions

def edge(**edges):
    # Edge Y:
    if 'y' in edges:
        edge_y = edges.get('y', 0)

        if isinstance(edge_y, int):
            if edge_y < 0:
                edge_y = 0
        else:
            edge_y = 0
    else:
        edge_y = 0
        
    # Edge X:
    if 'x' in edges:
        edge_x = edges.get('x', 0)

        if isinstance(edge_x, int):
            if edge_x < 0:
                edge_x = 0
        else:
            edge_x = 0
    else:
        edge_x = 0
    
    # Show the spaces:
    print(('\n' * edge_y), (' ' * edge_x), end='', sep='')

def text(text, **options):
    # Edge Y:
    if 'y' in options:
        edge_y = options.get('y', 0)

        if not isinstance(edge_y, int):
            edge_y = 0
    else:
        edge_y = 0
        
    # Edge X:
    if 'x' in options:
        edge_x = options.get('x', 0)
        
        if not isinstance(edge_x, int):
            edge_x = 0
    else:
        edge_x = 0
    
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
    
    # Distance:
    if 'distance' in options:
        distance = options.get('distance', 0)
    else:
        distance = 0
    
    # Distance fix 1:
    if 'distance_1' in options:
        distance_1 = options.get('distance_1', 0)
    else:
        distance_1 = 0
    
    # Distance fix 2:
    if 'distance_2' in options:
        distance_2 = options.get('distance_2', 0)
    else:
        distance_2 = 0
    
    # Next lines:
    if 'next' in options:
        next_line = options.get('next', '\n')

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
    
    # Show the text:
    print(' ' * edge_y, ' ' * edge_x, symbol_end, (symbol_intr * (distance + distance_1)), text, (symbol_intr * (distance + distance_2)), symbol_end, end=('\n' * next_line), sep='')
