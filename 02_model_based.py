grid=[
    ['S','','X','',''],
    ['','','','','X'],
    ['','X','','',''],
    ['','','','X',''],
    ['X','','','','G']
]

rows=len(grid)
cols=len(grid[0])

start=(0,0)
goal=(4,4)

visited=set()

moves=[
    (0,1), #right
    (1,0), #down
    (0,-1), #left
    (-1,0), #up
]

def is_valid(x,y):
    return(
        0<=x<rows and
        0<=y<cols and
        grid[x][y] != 'X' and (x,y) not in visited
    )
    
def dfs(position):
    x,y=position
    if position==goal:
        print("Goal reached !")
        return True
    
    visited.add(position)
    
    print("Agent at: ",position)
    
    for dx , dy in moves:
        nx=x+dx
        ny=y+dy
        
        if is_valid(nx,ny):
            if dfs((nx,ny)):
                return True
        
    return False

print("Grid :")

for row in grid:
    print(row)
    

print("\n Navigation start\n")
dfs(start)
print("\nVisited Cells :")
print(visited)