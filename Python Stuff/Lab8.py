import random
def remove_punc(text, punc):
    for i in punc:
        text = text.replace(i, '')
    return text

def wordcount(fname):
    try:
        f = open(fname, 'r')
        text = f.read()
        text = text.split()
        num = 0
        for i in text:
            num+=1
        return num
    except FileNotFoundError:
        print("Bad file name")
        return -1
    
def csv_func():
    name = str(input("Give me a file name: "))
    f = open(name, 'w')
    for i in range(1, 1001):
        rand = str(random.randint(-1000,1000))
        i = str(i)
        f.write(i + ', ' + rand + '\n')
    f.close()

def f_m_M():
    name = str(input("Give me a file name: "))
    try:
        f = open(name, 'r')
        text = f.read()
        print(text)
        text = text.split()
        print(text)
        num = int(text[1])
        num2 = int(text[1])
        count = 0
        for i in text:
            if count%2 != 0:
                if num < int(i):
                    num = int(i)
                if num2 > int(i):
                    num2 = int(i)
            count+=1
        return num, num2
    except FileNotFoundError:
        print("Bad file name")
        return -1

def tyler():
    name = str(input("Give me a file name: "))
    try:
        f = open(name, 'r')
        text = f.read()
        text = text.split(',')
        print(text)
        for i in range(15):
            print(i,text[i])
        print()
        for i in range(21,len(text)):
            if i%22 == 3:
                print(text[i], end=' ')
            if i%22 == 13:
                word = text[i]
                word = word[:-1]
                print(word, end=' ')
                print()
    except FileNotFoundError:
        print("Bad file name")
        return -1
    
    
            
