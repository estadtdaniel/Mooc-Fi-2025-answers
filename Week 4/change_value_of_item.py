# Replace a value in an array based on user input
num = [1,2,3,4,5]

while True: 
    index = int(input("Index:"))
    if index == -1:
        break
    val = int(input("New Value:"))
    num[index] = val
    print(num)