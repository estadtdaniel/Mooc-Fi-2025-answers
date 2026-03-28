#Adding items to an array based on user input
num = int(input("How many items:"))

i=1
array = []

while i <= num:
    item = int(input(f"Item {i}:"))
    array.append(item)
    i+=1
print(array)
    