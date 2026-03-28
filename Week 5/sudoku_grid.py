# Write your solution here
def row_correct(sudoku: list, row_no: int):
    sudoku_row = sudoku[row_no]
    
    for item in sudoku_row:
        x = sudoku_row.count(item)
        if x > 1 and item > 0:
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    i = 0 
    x=[]
    for i in range(0,len(sudoku),1):
        x.append(sudoku[i][column_no])
    
    for item in x:
        y = x.count(item)
        if y > 1 and item > 0:
            return False
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    y = []
    for i in range(row_no,row_no + 3,1):
        for j in range(column_no,column_no + 3, 1):
            y.append(sudoku[i][j])
    
    for item in y:
        z = y.count(item)
        if z > 1 and item > 0:
            return False
    return True 

def sudoku_grid_correct(sudoku: list):
    tests = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
    a = []
    b = []
    c = []
    for item in tests:
        a.append(row_correct(sudoku,item[0]))
        b.append(column_correct(sudoku,item[1]))
        c.append(block_correct(sudoku,item[0],item[1]))
    a.sort()
    b.sort()
    c.sort()
    if a[0] == True and b[0] == True and c[0] == True:
        return True
    else:
        return False

    
if __name__ == "__main__":
    sudoku = [
        [ 6, 4, 9, 2, 8, 3, 1, 5, 7 ],
        [ 0, 5, 0, 6, 4, 9, 2, 3, 8 ],
        [ 2, 3, 8, 1, 5, 7, 6, 4, 9 ],
        [ 9, 2, 3, 8, 1, 5, 0, 6, 4 ],
        [ 7, 6, 4, 9, 2, 3, 8, 1, 5 ],
        [ 8, 1, 5, 7, 0, 4, 9, 2, 0 ],
        [ 5, 7, 6, 4, 9, 2, 3, 2, 1 ],
        [ 4, 0, 2, 3, 8, 1, 5, 0, 6 ],
        [ 3, 0, 1, 5, 0, 6, 4, 9, 0 ],
    ]
    print(sudoku_grid_correct(sudoku))
