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

program  : mctype 'main' LB RB LP body? RP EOF ;

mctype: INTTYPE | VOIDTYPE ;

body: funcall SEMI;

exp: funcall | INTLIT ;

funcall: ID LB exp? RB ;

//------------------------------ Fragment ------------------------------//

fragment Digit: [0-9] ;

fragment Lowcase: [a-z] ;
fragment Uppercase: [A-Z] ;
fragment Letter: Lowcase | Uppercase;

fragment Dot: '.' ;
fragment Underscore: '_' ;

fragment Exponent: [eE] '-'? Digit+ ;

//------------------------------ Identifier ------------------------------//

ID: (Letter|Underscore) (Letter|Underscore|Digit)* ;

//------------------------------ Keyword ------------------------------//

BOOLEANTYPE: 'boolean' ;
INTTYPE: 'int' ;
FLOATTYPE: 'float' ;
STRINGTYPE: 'string' ;
VOIDTYPE: 'void' ;


DO: 'do' ;
WHILE: 'while' ;
FOR: 'for' ;

BREAK: 'break' ;
CONTINUE: 'continue' ;

IF: 'if' ;
ELSE: 'else' ;

RETURN: 'return' ;

TRUE: 'true' ;
FALSE: 'false' ;

//------------------------------ Keyword ------------------------------//

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

LB: '(' ;
RB: ')' ;

LP: '{' ;
RP: '}' ;

LSB: '[' ;
RSB: ']' ;

COMA: ',' ;
SEMI: ';' ;

//------------------------------ Literal ------------------------------//

INTLIT: '0' | [1-9] [0-9]+ ;

FLOATLIT
	: Digit+ Dot (Digit)* Exponent?
	| Digit* Dot (Digit)+ Exponent?
	| Digit+ Exponent
	;

BOOLEANLIT: TRUE|FALSE ;

STRINGLIT: ; 
// TODO 
// ? \n \b \a ... is the token ????
// 
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
