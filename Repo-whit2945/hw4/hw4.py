# Problem A: find_password
#==========================================
# Purpose:
#   Given an encrypted file, tries every possible four letter lowercase
#   password for that file until one works, and then returns the password.
# Input Parameter(s):
#   filename is a string representing the name of the encrypted file.
#   The file must be in the same folder as this script.
# Return Value:
#   Returns the password that successfully decrypts the given file
#==========================================

def find_password(filename):
    fp = open(filename)
    data = fp.read()

    #TODO: Try all possible four letter passwords, not just 'pwnd'
    password = ' '
    for first_letter in range(96,123):
        for second_letter in range(96,123):
            for third_letter in range(96,123):
                for forth_letter in range(96,123):
                    password = chr(first_letter) + chr(second_letter) + chr(third_letter) + chr(forth_letter) 
                    if decrypt(data,password):
                        return password
                    
#==========================================
# Purpose:
#   To find out if a number num is prime for function count_prime
# Input Parameter(s):
#   num; one number. This number is used to preform multiple calculations.
# Return Value:
#   Returns False if num is 1, and True if num is 2 right off the bat.
#   Otherwise, this function loops from 2 until the square root of num plus 1
#   finding the remainder of num and the iterated number
#   returns as soon as a remainder equals 0. If it doesn't then it return any
#   -thing after the loop then its assumed to be true.
#==========================================
def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for num2 in range(2, int(num**.5)+1):
        if (num%num2) == 0:
            return False
    return True

# Problem B: count_primes
#==========================================
# Purpose:
#   Prints out all prime numbers between low and high, inclusve, and
#   returns a count of how many there were.
# Input Parameter(s):
#   low is a positive integer 
#   high is a positive integer, which should be >= low
# Return Value:
#   Returns the number of prime numbers between low and high, inclusive
#==========================================
def count_primes(low, high):
    if low > high:
        return 0
    count = 0
    highh = high
    for i in range(low,high+1):
        if is_prime(i):
            print(i," is prime")
            count += 1
    return count


# Problem C: population
#==========================================
# Purpose:
#   Simulates the population of smallfish, middlefish, and bigfish over time
# Input Parameter(s):
#   small is an integer, the initial number of smallfish in the lake
#   middle is an integer, the initial number of middlefish in the lake
#   big is an integer, the initial number of bigfish in the lake
# Return Value:
#   Returns the number of weeks required for one of the populations to
#   fall below 10, or 100 if the populations are all still >= 10 after
#   100 weeks
#==========================================
def population(small, middle, big):
    for i in range(1,101):
        if(small < 10)or(middle < 10)or(big < 10):
            if i == 0:
                return i
            print("Week ", i, "- Small:", int(small)," Middle:", int(middle), " Big:", int(big), end=' ')
            print()
            return i
        small *= 1.1
        middle *= .95
        big *= .90
        s = small
        m = middle
        b = big
        small = .0002*m*s
        s -= small
        for f in range(int(s)):
            middle += .5
        middle = .00025*b*m
        m -= middle
        for ff in range(int(m)):
            big += .8
        if(small < 10)or(middle < 10)or(big < 10):
            if i == 0:
                return i
            print("Week ", i, "- Small:", int(small)," Middle:", int(middle), " Big:", int(big), end=' ')
            print()
            return i
        print("Week ", i, "- Small:", int(small)," Middle:", int(middle), " Big:", int(big), end=' ')
        print()
            
#DO NOT EDIT ANYTHING BELOW THIS LINE
#Below are helper functions used for decrypting the text files.
#You don't have to understand how any of these work.

# decrypt
#==========================================
# Purpose:
#   Check whether the password is correct for a given encrypted
#   file, and print out the decrypted contents if it is.
# Input Parameter(s):
#   data is a string, representing the contents of an encrypted file.
#   password is a four letter lowercase string, representing the password
#   used to encrypt/decrypt the file contents.
# Return Value:
#   Returns True if the password is correct and the file contents
#   were printed.  Returns False and prints nothing otherwise.
#==========================================
def decrypt(data, password):
    data = data.split('\n')
    if encode(password) == int(data[0]):
        print(vigenere(data[1],password))
        return True
    return False

# encode
#==========================================
# Purpose:
#   Turn a password into a ~9 digit number
# Input Parameter(s):
#   key is a four letter string representing a password
# Return Value:
#   Returns a number between 0 and 547120140, using modular exponentiation
#   to make it difficult to reverse engineer the password from the number.
#==========================================
def encode(key):
    total = 0
    for ltr in key:
        total += ord(ltr)
        total *= 123
    return pow(total,2011,547120141)

# vigenere
#==========================================
# Purpose:
#   Decipher a message using the Vigenere cipher
# Input Parameter(s):
#   msg a string, representing the encrypted message
#   key is a four letter string, representing the cipher key
# Return Value:
#   Returns a string representing the deciphered text
#==========================================
def vigenere(msg,key):
    i = 0
    out_msg = ''
    for ltr in msg:
        out_msg += chr((ord(ltr)-ord(key[i]))%28 +97)
        i = (i+1)%len(key)
    return out_msg.replace('{',' ').replace('|','.')
