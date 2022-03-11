# Author: CCG 3/10/22

words = ["I", "am", "a", "full", "sentence"]

def smash(lst):
    string = ""
    for word in lst:
        if word != lst[-1]:
            string += word + " "
        else:
            string += word + "."
    print(string)

smash(words)
