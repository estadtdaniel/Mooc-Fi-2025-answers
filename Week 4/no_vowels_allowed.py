# Write your solution here
def no_vowels(array):
    vowels = "aeiou"
    result = ""
 
    for letter in array:
        if letter not in vowels:
            result += letter
 
    return result

'''def no_vowels(array):
    word = ""
    vowels = ["a","e","i","o","u"]
    for item in array:
        if "a" in item:
            array = array.replace("a","")
        elif "e"  in item:
            array = array.replace("e","")
        elif "i"  in item:
            array = array.replace("i","")    
        elif "o"  in item:
            array = array.replace("o","")
        elif "u" in item:
            array = array.replace("u","")
    return array
'''
if __name__ == "__main__":
    print(no_vowels("this is an example"))