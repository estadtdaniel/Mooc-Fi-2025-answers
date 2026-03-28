#Creating a set of functions that will output the first, second, and last word in a sentence
def first_word(word):
    i = 0
    while True:
        #walk through a sentence until it sees white space 
        if word[i] == " ":
            j = i
            return(word[0:j])
            break
        else:
            i+=1

def second_word(word):
    #Using the first word function to determine the initial length to skip
    word_1 = len(first_word(word))
    #remove that defined first word from the sentence 
    word = word[word_1+1:]

    i = 0
    while True:
        #If statement for scenarios where there is only two words
        if i == len(word):
            j = i
            return(word[0:j])
            break
        #Else if walk through the word until white space is found
        elif word[i] == " ":
            j = i
            return(word[0:j])
            break
        else:
            i+=1

def last_word(word):
    i = 0
    while True:
        #Using negative indexing to find the last word 
        if word[i] == " ":
            return(word[i+1:])
            break
        else:
            i-=1
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "first second third fourth"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))