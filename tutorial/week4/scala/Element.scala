

abstract class Element {
    def contents: Array[String]
    val height = contents.length
    val width = if(height == 0) 0 else contents(0).length
}

class ArrayElement(conts : Array[String]) extends Element {
    def contents: Array[String] = conts
}

class LineElement(s : String) extends ArrayElement (Array(s)) {
    override val width = s .length
    override val height = 1
}

class UniformElement(ch : Char, r : Int, c : Int) extends ArrayElement(Array()) {
    
}

object Element {
    def elem (contents : Array[String]): Element = new ArrayElement(contents)
    def elem(line:String): Element = new LineElement(line)
}
