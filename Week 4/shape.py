# Creating a function that will print both a rectangle and triangle of a given character
def line(num,word):
    if word == "":
        print("*"*num)
    else:
        print(word[0]*num)

# t = triangle, r = rectangle
def shape(size_t,char_t,size_r,char_r):
    i=1
    while i<=size_t:
        line(i,char_t)
        i+=1
    
    i = 0
    while i<size_r:
        line(size_t, char_r)
        i+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "o")