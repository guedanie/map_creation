import os


def create_map():
    map = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,1,0,0],
            [0,0,0,0,0]
            ]
    return map


def print_map(map):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
        for row in map]))


def find_position(mylist, char):
     
    for sub_list in mylist: 
        if char in sub_list: 
            return (mylist.index(sub_list), sub_list.index(char)) 
    raise ValueError("'{char}' is not in list".format(char = char))

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


def main():
    os.system('clear')
    map = create_map()
    print_map(map)
    playing = True
    while playing:
        moving = True
        while moving:
            a, b = find_position(map, 1)
            movement = input("Where would you like to go? (N/E/S/W)")
            if a < 3 or b < 3:       
                os.system('clear')
                if movement == "N":
                    map = move_up(map)
                    print_map(map)
                if movement == "E":
                    map = move_right(map)
                    print_map(map)
                if movement == "S":
                    map = move_down(map)
                    print_map(map)
                if movement == "W":
                    map = move_left(map)
                    print_map(map)
            
            else: 
                print("You can't go further in that direction")
                moving = False   