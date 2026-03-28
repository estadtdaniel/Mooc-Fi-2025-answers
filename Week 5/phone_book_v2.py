# Write your solution here
book = {}
while True:
    command = int(input("command (1 search, 2 add, 3 quit):"))

    if command == 3: 
        print("quitting...")
        break
    elif command == 2:
        name = input("name:")
        if name not in book:
            book[name] = []
        num = input("number:")
        book[name].append(num)
        
        print("ok!")
    elif command == 1: 
        name = input("name:")
        if name not in book:
            print("no number")
        else:
            i = 0
            for item in book[name]:
                print(item)
                