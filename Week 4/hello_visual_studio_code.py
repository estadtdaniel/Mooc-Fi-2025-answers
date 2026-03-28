# Preliminary coding to familiarize with Visual Studio 
while True:
    word = input("Editor:")
    #using the lower to ignore capital letters for making comparison easier
    word_lower = word.lower()  
    
    if word_lower == "word" or word_lower == "notepad":
        print("awful")
    elif word_lower == "visual studio code":
        print("an excellent choice!")
        break
    else:
        print("not good")