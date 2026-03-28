# Write your solution here
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
    print(column_correct(sudoku, 1))