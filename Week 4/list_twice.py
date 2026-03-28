# Creating an array of numbers in their input order then sorted order until the user types 0 to exit
array = []
while True:
    num = int(input("New item:"))
    array.append(num)
    if num == 0:
        print("Bye!")
        break
    print(f"The list now: {array}")
    print(f"The list in order: {sorted(array)}")