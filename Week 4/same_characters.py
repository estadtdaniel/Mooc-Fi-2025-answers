#Creating a function to return whether the location within a word contains the same letter
def same_chars(word,n1,n2):
    word_len = len(word)
    #Create condition for when index checks are outside word length
    if n1 >= word_len or n2 >= word_len:
        return False
    elif word[n1] == word[n2]:
        return True
    else:
        return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("aba", 0, 2))