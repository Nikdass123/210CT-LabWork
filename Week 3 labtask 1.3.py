def remstringchar(string):
    if not string:
        return string
    else:
        if string[0] in "aeiouAEIOU": # this checks if first char has aeiou
             return remstringchar(string[1:])# if first char has vowel then it removes 
        else:
             return string[0] + remstringchar(string[1:])#if first char not got vowel it moves to next

string = raw_input("Enter a word: ")
print remstringchar(string)
