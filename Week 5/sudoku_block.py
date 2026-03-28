# Write your solution here
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

    
    
if __name__ == "__main__":
    sudoku = [
  [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],   # rivi 0
  [ 2, 2, 0, 0, 5, 0, 7, 0, 0 ],   # rivi 1
  [ 0, 2, 0, 3, 0, 0, 4, 0, 4 ],   # rivi 2
  [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],   # rivi 3
  [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],   # rivi 4
  [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],   # rivi 5
  [ 0, 0, 7, 8, 0, 3, 9, 6, 6 ],   # rivi 6
  [ 3, 0, 1, 0, 0, 0, 0, 0, 3 ],   # rivi 7
  [ 3, 0, 0, 0, 2, 0, 2, 0, 1 ],   # rivi 8
    ]
    print(block_correct(sudoku,1,2))