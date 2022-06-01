import random
#==========================================
# Purpose: This function's purpose is to find the first word of the each sentence
# with the given text format. 
# Input Parameter(s): This function only has one input parameter; 'fname'.
# This parameter is the file name that the function uses to find the first
# word of a given text.
# Return Value(s): This function returns a list titled 'text'. This list
# contains the first word of each sentence. 
#==========================================
def first_words(fname):
    text = []
    try:
        with open(fname, 'r') as file:
            text2 = file.readlines()
        for i in range(len(text2)):
            text3 = text2[i].split(' ')
            text.append(text3[0])
        return text
    except FileNotFoundError:
        return -1
#==========================================
# Purpose: This function's purpose is to make a dictionary including
# each individual word as a key, and the words proceeding that word as its keys.
# Input Parameter(s): This function only has one input parameter; 'fname'.
# 'fname' represents a file's name as a string.
# Return Value(s): This fuction returns a dictionary called 'text'.
#========================================== 
def next_words(fname):
    text = {}
    try:
        with open(fname, 'r') as file:
            text2 = file.readlines()
        for i in range(len(text2)):
            text3 = text2[i].split(' ')
            for n in range(len(text3)):
                text3[-1] = '.'
                if text3[n] != '.':
                    if text3[n] in text:
                        text[text3[n]].append(text3[n+1])
                    else:
                        text[text3[n]] = []
                        text[text3[n]].append(text3[n+1])
        return text
    except FileNotFoundError:
        return -1

#==========================================
# Purpose: This fuction produces ten sentences based on random choices
# from a list and from lists that are within dictionaries.
# Input Parameter(s): This function has only one input parameter; 'fname'.
# 'fname' is a string that represents a file name that we use in the function.
# Return Value(s): Nothing gets returned. Words sentences generated are printed.
#==========================================
def fanfic(fname):
    l = first_words(fname)
    d = next_words(fname)
    choice = ' '
    word = ' ' 
    for i in range(10):
        word = random.choice(l)
        print(word, end = ' ')
        choice = random.choice(d[word])
        print(choice, end = ' ')
        while choice != '.':
            choice = random.choice(d[choice])
            print(choice, end = ' ')
        print()

#==========================================
# Purpose: (What does the function do?)
# Input Parameter(s): (Each parameter by name and what it represents)
# Return Value(s): (What gets returned? Possibilities?)
#==========================================
def total_txt_size(directory):
    if type(directory) == int:
        return directory
    if type(directory) == dict:
        if directory == {}:
            return 0
        for i in directory.values():
           pass 

    return 400
        




















    
