# Practice creating programs by creating a program that
# takes an input and forms a line based on no word or
# the first character of the word and a set length
def line(num,word):
    if word == "":
        print("*"*num)
    else:
        print(word[0]*num)

    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "word")
    line(3,"")