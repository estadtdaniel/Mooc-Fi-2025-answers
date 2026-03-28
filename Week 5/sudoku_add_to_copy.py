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

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku_copy = [row[:] for row in sudoku]

    sudoku_copy[row_no][column_no] = number
    return sudoku_copy

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    #print_sudoku(sudoku)
    sudoku_2 = copy_and_add(sudoku,1,1,5)
    #print(sudoku_2)
    print_sudoku(sudoku_2)