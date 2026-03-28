# Write your solution here
def no_shouting(array):
    results = []
    for item in array:
        if item.isupper() == False:
            print(item)
            results.append(item)
    return results

if __name__ == "__main__":
    print(no_shouting(["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]))

