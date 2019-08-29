grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::member {
def emit(self):
    tk = self.type
    if tk == UNCLOSE_STRING:       
        result = super.emit();
        raise UncloseString(result.text);
    elif tk == ILLEGAL_ESCAPE:
        result = super.emit();
        raise IllegalEscape(result.text);
    elif tk == ERROR_CHAR:
        result = super.emit();
        raise ErrorToken(result.text); 
    else:
        return super.emit();
}

options{
	language=Python3;
}

fragment DIGIT: [0-9];
fragment LOWCASE: [a-z];
fragment NEGATIVE: '-';
fragment DOT: '.';
fragment SINGLEQUOTE: '\'';
fragment DOUBLEQUOTE: '\'\'';
fragment EXPONENT: [eE] NEGATIVE? DIGIT+;
 
program: mctype 'main' LB RB LP body? RP EOF ;

mctype: INTTYPE | VOIDTYPE ;

body: funcall SEMI;

exp: funcall | INTLIT ;

funcall: ID LB exp? RB ;

ID: LOWCASE(LOWCASE|DIGIT)*;

INTTYPE: 'int' ;

VOIDTYPE: 'void' ;

INTLIT: [0-9]+;

FLOATLIT
	: DIGIT+ DOT (DIGIT)* EXPONENT?
	| DIGIT* DOT (DIGIT)+ EXPONENT?
	| DIGIT+ EXPONENT
	;

STRLIT : SINGLEQUOTE (DOUBLEQUOTE | ~('\''))*? SINGLEQUOTE;

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SEMI: ';' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
