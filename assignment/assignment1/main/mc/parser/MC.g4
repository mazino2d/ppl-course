grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options {
	language = Python3;
}

program: mctype 'main' LB RB LP body? RP EOF;

mctype: INTTYPE | VOIDTYPE;

body: funcall SEMI;

exp: funcall | INTLIT;

funcall: ID LB exp? RB;

//------------------------------ Fragment ------------------------------//

fragment Digit: [0-9];

fragment Lowcase: [a-z];
fragment Uppercase: [A-Z];
fragment Letter: Lowcase | Uppercase;

fragment Character: ~[\b\f\r\n\t"\\] | Escape;
fragment Escape: '\\' [bfrnt"\\];
fragment IllegalEscape: '\\' ~[bfrnt"\\] ;

fragment Dot: '.';
fragment Underscore: '_';

fragment Exponent: [eE] '-'? Digit+;

//------------------------------ Keyword ------------------------------//

BOOLEANTYPE: 'boolean';
INTTYPE: 'int';
FLOATTYPE: 'float';
STRINGTYPE: 'string';
VOIDTYPE: 'void';

DO: 'do';
WHILE: 'while';
FOR: 'for';

BREAK: 'break';
CONTINUE: 'continue';

IF: 'if';
ELSE: 'else';

RETURN: 'return';

TRUE: 'true';
FALSE: 'false';

//------------------------------ Identifier ------------------------------//

ID: (Letter | Underscore) (Letter | Underscore | Digit)*;

//------------------------------ Operator ------------------------------//

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';

NOT: '!';
OR: '||';
AND: '&&';

EQUAL: '==';
NOT_EQUAL: '!=';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';

ASSIGN: '=';

//------------------------------ Separator ------------------------------//

LB: '(';
RB: ')';

LP: '{';
RP: '}';

LSB: '[';
RSB: ']';

COMA: ',';
SEMI: ';';

//------------------------------ Literal ------------------------------//

INTLIT: [0-9]+;

FLOATLIT:
	Digit+ Dot (Digit)* Exponent?
	| Digit* Dot (Digit)+ Exponent?
	| Digit+ Exponent;

BOOLEANLIT: TRUE | FALSE;

STRINGLIT: '"' Character* '"' {
    temp = str(self.text)
    self.text = temp[1:-1]
};

//------------------------------ Comment ------------------------------//

CMTLINE: '//' ~[\n\r]* -> skip;
CMTBLOCK: '/''*' .*? '*''/' -> skip;
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

//------------------------------ Error token ------------------------------//

UNCLOSE_STRING: '"' Character* ([\b\t\n\f\r"'\\] | EOF) {
    esc = ['\b', '\t', '\n', '\f', '\r', '"', '\\']
    temp = str(self.text)

    if temp[-1] in esc:
        raise UncloseString(temp[1:-1])
    else :
        raise UncloseString(temp[1:])
};

ILLEGAL_ESCAPE:'"' Character* IllegalEscape {
    temp = str(self.text)
    raise IllegalEscape(temp[1:])
};

ERROR_CHAR:.
{
    raise ErrorToken(self.text)
};
