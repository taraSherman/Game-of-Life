'''
Three components:
    A property defined in a 1- or 2-dimensional space
    A mathematical rule to change this property for each step (generation) in the simulation
    A way to display or capture the state of the system as it evolves
    
To evaluate a single cell:
    Each cell has eight neighbors. A cell (i, j) is accessed on a grid [i][j], where i is row and j is col. the cell's value depends on the state of its neighbors in the previous step.
    
The Four Rules:
    1. Live cell that has less than 2 live neighbors will die
    2. Live cell with 2 or 3 live neighbors continues to live
    3. Live cell with 3 or more live neighbors will die
    4. Dead cell with exactly 3 live neighbors will come to life
    
    Toroidal boundary conditions (wraps vertically and horizontally)
    Algorithm to apply the four rules and run the simulation:
    1. Initialize the cells in the grid
    2. At each step, for each cell(i, j):
        a. Update cell(i, j) based on its neighbors, taking into account boundary conditions
        b. Update display of grid values.
        
Tools:
    numpy arrays (import numpy as np)
    matplotlib library (import matplotlib.pyplot as plt)
    matplotlib animation module (import matplotlib.animation as animation)
    
array([ [255, 255, 255, 255],
        [255, 255, 255, 255],
        [255, 255, 255, 255],
        [255, 255, 255, 0]])
        
Define a 2d numpy array of shape (3, 3) where each element of the array is an intger value. Then use plt.show() method to display this matrix of values as an image, and you pass in the interpolation option as nearest to get sharp edges for cells. Example: x = np.array([[0, 0, 255], [255, 255, 0], [0, 255, 0]] for black and white.

Initial conditions:
    Set an initial state for each cell (can be random or can add some specific patterns).
        Random:
            Use random module in numpy (Example: np.random.choice([0, 255], 4*4, p=[0.1, 0.9]).reshape(4, 4)). np.random.choice chooses a value from the list [0, 255]. Probability factor comes from parameter p=[0.1, 0.9] (gives 10% for black and 90% for white). choice() method creates a 1-dimensional array of 16 values; have to use .reshape to make it 2-dimensional.
        Pattern:
            Initialize grid to 0's then use a method to add a pattern at a particular row and column. Example:
                def addGlider(i, j, grid):    """adds a glider with top left cell at (i, j)"""
                    glider = np.array([[0, 0, 255],
                        [255, 0, 255],
                        [0, 255, 255]])
                    grid[i:i+3, j:j+3] = glider
                grid = np.zeros(N*N).reshape(N, N)
                addGlider(1, 1, grid)
            Define pattern using numpy array shape (3, 3). Use the numpy slice operation to copy this pattern array into the simulation’s two-dimensional grid, with its top-left corner placed at the coordinates you specify as i and j. Create an NxN array of 0's and then call the addGlider() method to initialize grid with the pattern.
            Other patterns: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns
            
Boundary conditions:
    array([ [255, 255, 255, 255],
            [255, 255, 255, 255],
            [255, 255, 255, 255],
            [255, 255, 255, 0]])
            
        For row i, last cell is grid[i][N-1]. Its neighbor to the right is grid[i][N], but with toroidal boundary conditions, grid[i][N] should be replaced by grid[i][0]. Best way to do that for all four boundaries is using modulo --> right = grid[i][(j+1) % N]
        When cell is on edge (j = N - 1), asking for cell to the right gives you (j + 1) % N; this sets j back to 0, making the right side of the grid wrap around to the left side. Do the same for the bottom and it wraps around to the top.
        newGrid = grid.copy() <-- makes a new copy of the grid
    for i in range(N):
        for j in range(N):
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] + 
                grid[(i-1)%N, j] + grid[(i+1)%N, j] + 
                grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + 
                grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)
                
Implementing the rules:
    PSEUDOCODE
    if the cell that is being accessed is alive and:
        if total neighbors is less than 2 OR greater than 3:
            current cell (newGrid[i, j]) dies
        else:
            if total neighbors is exactly 3:
                current cell comes to life
'''
