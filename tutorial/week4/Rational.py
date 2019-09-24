class Rational :
    # greatest common divisor
    def __gcd(self, n, d): 
        if(d == 0): 
            return n 
        else: 
            return self.__gcd(d, n%d) 


    # constructor / instance attributes
    def __init__(self, numer=0, denom=1):
        if denom == 0 :
            raise SystemExit("denom must not be zero!")
        else:
            common = self.__gcd(numer, denom)
            self.numer = numer//common
            self.denom = denom//common
    # override add operator (rational)
    def __add__(self, other):
        if isinstance(other, int):
            return self + Rational(other)
        else:
            common = self.__gcd(self.numer, self.denom)
            new_numer = self.numer*other.denom + other.numer*self.denom
            new_denom = self.denom*other.denom
            return Rational(new_numer, new_denom)
    # override string convert method
    def __str__(self):
        return str(self.numer) + "/" + str(self.denom)


print(Rational(1,2) + 2)
