#Creating a program to determine if two words are anagrams 
def anagrams(word1,word2):
    word_1s=sorted(word1)
    word_2s=sorted(word2)
    if word_1s == word_2s:
        return True
    else:
        return False
if __name__ == "__main__":
    anagrams("spice","splice")
    anagrams("cat","tac")