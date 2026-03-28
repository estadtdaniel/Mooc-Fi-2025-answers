# Creating a function to determine if a word is a palindrome
# Used while loops with positive and negative indexing to see if values are equal

def palindromes(word):
    k = []
    for i in range(1,len(word)+1,1):
        if word[i-1] == word[-1*i]:
            k.append(1)
        else:
            #If not equal create a "false" value at each check
            k.append(0)
    if min(k) == 0:
        return False
    else:
        return True


while True:
    word = input("Please type in a palindrome:")

    if palindromes(word) == True:
        print(f"{word} is a palindrome!")
        break
    else:
        print(f"that wasn't a palindrome")