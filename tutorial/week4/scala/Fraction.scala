package fraction

class Fraction(n:Int, d:Int) {
    require(d != 0) // Int / Zero = Inf !

    private val g = gcd(n.abs, d.abs)
    private def gcd(a:Int, b:Int):Int = 
        if(b == 0) a else gcd(b, a%b)

    val numer = n/g // numerator
    val denom = d/g // denominator

    def this(n:Int) = this(n,1)
    def this() = this(0,1)

    def + (rhs:Fraction):Fraction = 
        new Fraction(
            numer*rhs.denom + rhs.numer*denom,
            denom*rhs.denom // a/b + c/d = (ad + bc)/bd
        )

    def + (rhs:Int):Fraction = 
        new Fraction(
            numer + rhs*denom,
            denom // a/b + c = (a + bc)/b
        )

    def * (rhs:Fraction):Fraction = 
        new Fraction(
            numer*rhs.numer,
            denom*rhs.denom // a/b * c/d = ac/bd
        )

    def * (rhs:Int):Fraction = 
        new Fraction(
            numer*rhs,
            denom // a/b * c = ac/b
        )

    override def toString = numer + "/" + denom
}
