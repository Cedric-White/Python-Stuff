def roundit(num):
    if(num < 0):
        num -= .5
    else:
        num += .5
    return int(num)
