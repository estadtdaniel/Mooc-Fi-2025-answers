# Write your solution here
def transpose(matrix: list):
    matrix_copy = [row[:] for row in matrix]
    i = 0
    j = 0
    for i in range(0,len(matrix),1):
        for j in range(0,len(matrix),1):
            matrix[i][j] = matrix_copy[j][i]
    print(matrix)

        

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    #print(matrix)
    t = transpose(matrix)
    
