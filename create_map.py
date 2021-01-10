

test = [[0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,0,0,0]
        ]


def print_map(map):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
        for row in map]))


def find_position(mylist, char): 
    ...:     for sub_list in mylist: 
    ...:         if char in sub_list: 
    ...:             return (mylist.index(sub_list), sub_list.index(char)) 
    ...:     raise ValueError("'{char}' is not in list".format(char = char))

def move_right(map):
    # first need to find current location

    a, b = find_position(map, 1)
    map[a][b] = 0
    map[a][b + 1] = 1

    return map 

    
def move_left(map):
    
    a, b = find_position(map, 1)
    map[a][b] = 0
    map[a][b - 1] = 1

    return map

def move_up(map):
    a, b = find_position(map, 1)
    map[a][b] = 0
    map[a - 1][b] = 1

    return map

def move_down(map):
    a, b = find_position(map, 1)
    map[a][b] = 0
    map[a + 1][b] = 1

    return map
