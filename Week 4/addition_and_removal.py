# Using user input to add numbers in sequential order 

array = []
i=0

while True: 
    print(f"The list is now {array}")

    check = input("a(d)d, (r)emove or e(x)it:")
    if check == "d":
        array.insert(i,i+1)
        i+=1
    elif check == "r":
        array.remove(i)
        i-=1
    elif check == "x":
        print("Bye!")
        break
