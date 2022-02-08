
#  Taking a 4x4 matrix
size = 4

def grid_view(grid):
    col_count = 0
    grid2 =[]
    for i in range(size):
        grid1 = []
        for j in range(size):
            if(col_count in grid):
                grid1.append(True)
            else:
                grid1.append(False)
            col_count += 1
        grid2.append(grid1)
    return grid2

def position_true(grid):
    position_obj = []
    for i in range(size):
        for j in range(size):
            pos_obj = []
            if(grid[i][j] == True):
                pos_obj.extend([i,j])
                position_obj.append(pos_obj)
    return position_obj

def neighbours(grid,i):
    true = []
    false = []

    if (i[1]-1 >= 0 and i[0]-1 >= 0):
        if( grid[i[0]-1][i[1]-1] == True):
            true.append('t')
        elif (grid[i[0]-1][i[1]-1] == False):
            pos_obj = []
            pos_obj.extend([i[0]-1,i[1]-1])
            false.append(pos_obj)
        
    if (i[0]-1 >= 0):
        if(grid[i[0]-1][i[1]] == True):
            true.append('t')
        elif (grid[i[0]-1][i[1]] == False):
            pos_obj=[]
            pos_obj.extend([i[0]-1, i[1]])
            false.append(pos_obj)
                
    if (i[1]+1 < size and i[0]-1 >= 0):
        if(grid[i[0]-1][i[1]+1] == True):
            true.append('t')

        elif (grid[i[0]-1][i[1]+1] == False):
            pos_obj = []
            pos_obj.extend([i[0]-1, i[1]+1])
            false.append(pos_obj)

    if (i[1]-1 >= 0):
        if(grid[i[0]][i[1]-1] == True):
            true.append('t')
        elif (grid[i[0]][i[1]-1] == False):
            pos_obj=[]
            pos_obj.extend([i[0], i[1]-1])
            false.append(pos_obj)
        
    if (i[1]+1 < size):
        if(grid[i[0]][i[1]+1] == True):
            true.append('t')
        elif (grid[i[0]][i[1]+1] == False):
            pos_obj=[]
            pos_obj.extend([i[0], i[1]+1])
            false.append(pos_obj)
        
    if (i[1]-1 >= 0 and i[0]+1 < size):
        if(grid[i[0]+1][i[1]-1] == True):
            true.append('t')
        elif (grid[i[0]+1][i[1]-1] == False):
            pos_obj=[]
            pos_obj.extend([i[0]+1, i[1]-1])
            false.append(pos_obj)

    if (i[0]+1 < size):
        if(grid[i[0]+1][i[1]] == True):
            true.append('t')
        elif (grid[i[0]+1][i[1]] == False):
            pos_obj=[]
            pos_obj.extend([i[0]+1, i[1]])
            false.append(pos_obj)
               
    if (i[1]+1 < size and i[0]+1 < size):
        if(grid[i[0]+1][i[1]+1] == True):
            true.append('t')
        elif (grid[i[0]+1][i[1]+1] == False):
            pos_obj=[]
            pos_obj.extend([i[0]+1, i[1]+1])
            false.append(pos_obj)
    return len(true),false

def status_change(grid):
    new_grid = grid
    return new_grid
