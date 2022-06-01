import random
def random_list(n):
    mylist = [0]*n
    mylist
    if (n == 0) or (n < 0):
        return []
    else:
        for i in range(n):
            mylist[i] = random.randint(1,n)
        return mylist

def swap_min(numL):
    mmin = numL[0]
    index = 0
    for i in range(len(numL)):
        if numL[i] < mmin:
            mmin = numL[i]
            index = i
    numL[index] = numL[0]
    numL[0] = mmin

def list_string():
    mylist = []
    string = str(input("Enter a string: "))
    while string:
        string = str(input("Enter a string: "))
        if repeat(string) == True:
            mylist.append(string)
    for i in range(len(mylist)):
        print(mylist[i])

def repeat(string):
    count = 0
    for i in range(len(string)):
        for n in range(i+1, len(string)):
            if string[i] == string[n]:
                count+=1
    if count != 0:
        return True
    else:
        return False

def selection_sort():
    n = int(input("How many elements?: "))
    num_list = random_list(n)
    print(num_list)
    num = num_list[0]
    index = 0
    for i in range(len(num_list)):
        for n in range(i+1, len(num_list)):
            if num_list[n] < num_list[i]:
                num = num_list[n]
                index = n
                num_list[index] = num_list[i]
                num_list[i] = num
    print(num_list)

selection_sort()
            
    
