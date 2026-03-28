# Write your solution here
letters = {}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(0,26,1):
    letters[i] = alphabet[i]

layer = int(input("Layers:"))
size = 2*layer - 1

array = [[0]*size for i in range(size)]

for i in range(0,size,1):
    for j in range(i,size-i,1):
        array[i][j] = letters[layer - i-1] #top row
        array[size-i-1][j] = letters[layer - i-1] #bottom row
        array[j][i] = letters[layer - i-1] #left side
        array[j][size-i-1] = letters[layer - i-1] #right side

for i in range(0,size,1):
    print()
    for j in range(0,size,1):
        print(array[i][j], end="")


