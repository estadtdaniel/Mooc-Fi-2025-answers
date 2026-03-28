# Creating a program that takes word inputs until the same word
# is typed, then outputs the number of different words 
array = []
count = 0 
while True:
    word = input("Word:")
    if word in array:
        break
    else:
        array.append(word)
        count+=1
print(f"You typed in {count} different words")