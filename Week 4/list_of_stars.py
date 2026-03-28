# Write your solution here
def list_of_stars(array):
    for i in array:
        print("*"*i)
        i+=1

if __name__ == "__main__":
    list_of_stars([4,2,3,4])