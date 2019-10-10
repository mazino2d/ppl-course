// 1711807
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

//------------------------------ PARSER ------------------------------//
//------------------------------------------------------------------------//
//------------------------------ Program ------------------------------//

program: (declaration)+ EOF;
declaration: vardecl | funcdecl;

//------------------------ Variable Declaration ----------------------//

vardecl: primtype varlist SEMI;
primtype: BOOLEANTYPE | INTTYPE
                | FLOATTYPE | STRINGTYPE;
varlist: var COMA varlist | var;
var: ID LSB INTLIT RSB | ID;

//------------------------ Function Declaration ----------------------//

funcdecl: functype ID LB paralist? RB blockstmt;
functype: primtype | arraytype | VOIDTYPE;
arraytype: primtype LSB RSB;
paralist: paradecl (COMA paradecl)*;
paradecl: primtype para;
para: ID (LSB RSB)?;


//------------------------ Block Statement ----------------------//

blockstmt: LP (vardecl | stmt)* RP;

stmt: blockstmt | ifstmt
    | whilestmt  | forstmt
    | breakstmt  | continuestmt
    | returnstmt | exprstmt
    ;

ifstmt: IF LB expr0 RB stmt (ELSE stmt)?;
whilestmt: DO stmt+ WHILE expr0 SEMI;
forstmt: FOR LB expr0 SEMI expr0 SEMI expr0 RB stmt;
breakstmt: BREAK SEMI;
continuestmt: CONTINUE SEMI;
returnstmt: RETURN (expr0)? SEMI;
exprstmt: expr0 SEMI;

//-------------------------- Expression ------------------------//

expr0: expr1 ASSIGN expr0 | expr1;
expr1: expr1 OR expr2 | expr2;
expr2: expr2 AND expr3 | expr3;
expr3: expr4 (EQ | NE) expr4 | expr4;
expr4: expr5 (LT | LE | GT | GE) expr5 | expr5;
expr5: expr5 (ADD | SUB) expr6 | expr6;
expr6: expr6 (MUL | DIV | MOD) expr7 | expr7;
expr7: (NOT | SUB) expr7 | expr8;
expr8: expr9 LSB  expr0 RSB | expr9;
expr9: LB expr0 RB | operand;

operand: INTLIT   | BOOLEANLIT | ID
            | FLOATLIT | STRINGLIT | calfunc;

calfunc: ID LB arglist RB;
arglist: (expr0 (COMA expr0)*)?;

//------------------------------ LEXER --------------------------------//
//-------------------------------------------------------------------------//
//-------------------------------- Literal --------------------------------//

INTLIT: Digit+;

FLOATLIT: Digit+ Dot (Digit)* Exponent?
	               | Digit* Dot (Digit)+ Exponent?
	               | Digit+ Exponent;

BOOLEANLIT: TRUE | FALSE;

STRINGLIT: '"' Character* '"' {
    temp = str(self.text)
    self.text = temp[1:-1]
};

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

EQ: '==';
NE: '!=';
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

//------------------------------ Comment ------------------------------//

CMTLINE: '//' ~[\n\r\f]* -> skip;
CMTBLOCK: '/''*' .*? '*''/' -> skip;
WS: [ \f\t\r\n]+ -> skip; // skip spaces, tabs, newlines

//------------------------------ Error token ------------------------------//

UNCLOSE_STRING: '"' Character* ([\b\f\r\n\t\\] | EOF) {
    esc = ['\b', '\t', '\n', '\f', '\r', '\\']
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
