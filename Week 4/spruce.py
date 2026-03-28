# Creating a spruce of * based on a height value 
def spruce(num):
    i = num - 1
    j = 1
    print("a spruce!")
    # using i to define white space, and j for the shape
    while i>=0: 
        print(" "*i + "*"*j + " "*i)
        i-=1
        j+=2
    #creating the "stump"
    i = num - 1
    j = 1
    print(" "*i + "*"*j + " "*i)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)