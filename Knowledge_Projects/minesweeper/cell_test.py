
def update(cell, count):
    i = cell[0]
    j = cell[1]
    height = 8
    width = 8
    possible_bombs = []
    safes = []

    if count == 0:
        for n_i in range(i-1,i+2):
            for n_j in range(j-1,j+2):
                if n_i>-1 and n_i<height and n_j>-1 and n_j<width:
                    safes.append((n_i,n_j))
        return safes
    elif count > 0:
        for n_i in range(i-1,i+2):
            for n_j in range(j-1,j+2):
                if n_i>-1 and n_i<height and n_j>-1 and n_j<width and (n_i!=i or n_j!=j):
                    possible_bombs.append((n_i,n_j))
        return possible_bombs
    
cell = (0,0)
count = 0
safe_list = []
possible_list = []
flagged = []

while True:
    cell_input = input("Cell:")
    cell = (int(cell_input[0]), int(cell_input[1])) 
    count = int(input("Count:"))
    if count == 0:  
        safe = update(cell, count)   
        safe_list += safe
    if count > 0:
        possible = update(cell, count)
        possible_list += possible
    for place in possible_list[:]:
        if place in safe_list:
            possible_list.remove(place)
    for thing in possible_list:
        if thing in flagged:
            count -= 1
            possible_list.remove(thing)
    if len(possible_list) == count:
        for thing in possible_list[:]:
            flagged += [(thing)]
            possible_list.remove(thing)
            print (f"flagging {thing}")
    if count == 0:
        safe = update(cell, count)   
        safe_list += safe
        
    print(set(safe_list))
    print(set(possible_list))