'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    # If length of word is less than 2 it cant have occurance
    if len(word) < 2:
        return 0

    # Check to see if two consective letters are t and h
    if word[0] == "t" and word[1] == "h":
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])
        

    
