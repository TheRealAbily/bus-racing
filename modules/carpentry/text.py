# CMD text control functions

def edge(**edges):
    # Edge Y:
    if 'y' in edges:
        edge_y = edges.get('y', 0)

        if isinstance(edge_y, int):
            if edge_y > 0:
                print('\n' * edge_y)
        
    # Edge X:
    if 'x' in edges:
        edge_x = edges.get('x', 0)
        
        if isinstance(edge_x, int):
            if edge_x > 0:
                print(' ' * edge_x)
