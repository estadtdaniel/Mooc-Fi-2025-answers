# Write your solution here
def invert(dictionary: dict): 
    value = []
    keys = []
    for item in dictionary:
        value.append(dictionary[item])
        keys.append(item)
    i = 0
    dictionary.clear()
    for i in range(0,len(value),1):
        dictionary[value[i]] = keys[i]
    
        


if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
