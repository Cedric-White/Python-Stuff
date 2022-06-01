class Rational:
    def __init__(self,num=0,den=1):
        self.numerator = num
        if den == 0:
            self.denominator = 1
        else:
            self.denominator = den
    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        elif self.numerator == 0:
            return str(0)
        else:
            return str(self.numerator) + '/' + str(self.denominator)

class SpaceCoins:
    def __init__(self, p=0, n=0):
        if n >= 8:
            p += (n//8)
            n = n%8
            self.ningis = n
            self.pues = p
        if n < 0:
            while n < 0:
                n += 8
                p -= 1
            self.ningis = n
            self.pues = p
        self.pues = p
        self.ningis = n
    def __str__(self):
        if self.ningis == 0 and self.pues == 0:
            return str(0) + '*'
        elif self.ningis == 0:
            return str(self.pues) + '^'
        elif self.pues == 0:
            return str(self.ningis) + '*'
        else:
            return str(self.pues) + '^' + str(self.ningis) + '*'
    def __add__(self, other):
        return SpaceCoins(self.pues+other.pues, self.ningis+other.ningis)
    def __sub__(self, other):
        return SpaceCoins(self.pues-other.pues, self.ningis-other.ningis)
    def __mul__(self, other):
        return SpaceCoins(self.pues*other.pues, self.ningis*other.ningis)

class Vec2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'
    def get_values(self):
        return [self.x, self.y]
    def set_values(self, l):
        self.x = l[0]
        self.y = l[1]
    def __add__(self, other):
        return Vec2(self.x+other.x, self.y+other.y)
    def __mul__(self, n):
        return Vec2(self.x*n, self.y*n)
    
    
