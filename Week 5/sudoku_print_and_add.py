# Write your solution here
def print_sudoku(sudoku:list):
    i = 0
    j = 0
    for i in range(0,len(sudoku),1):
        if i%3 == 0 and i!=0:
            print()
        for j in range(0,len(sudoku),1):
            if j%3 == 0 and j!=0:
                print(" ",end="")
            if sudoku[i][j] == 0 or sudoku[i][j] == "_":
                sudoku[i][j] = "_ "
            elif sudoku[i][j] != 0:
                x = sudoku[i][j]
                sudoku[i][j] = f"{x} "
            print(sudoku[i][j], end="")
        print()
        

def add_number(sudoku:list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number


if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    #print_sudoku(sudoku)
    add_number(sudoku,1,0,9)
    add_number(sudoku,0,0,3)
    print_sudoku(sudoku)
