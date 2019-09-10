# Generated from /home/kraken/ppl-course/assignment/assignment1/main/mc/parser/MC.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\62")
        buf.write("(\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\5\2\23\n\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\5\3\5\5\5\37\n\5\3\6\3\6\3\6\5\6$\n\6\3\6\3\6\3\6")
        buf.write("\2\2\7\2\4\6\b\n\2\3\4\2\5\5\b\b\2%\2\f\3\2\2\2\4\27\3")
        buf.write("\2\2\2\6\31\3\2\2\2\b\36\3\2\2\2\n \3\2\2\2\f\r\5\4\3")
        buf.write("\2\r\16\7\3\2\2\16\17\7#\2\2\17\20\7$\2\2\20\22\7%\2\2")
        buf.write("\21\23\5\6\4\2\22\21\3\2\2\2\22\23\3\2\2\2\23\24\3\2\2")
        buf.write("\2\24\25\7&\2\2\25\26\7\2\2\3\26\3\3\2\2\2\27\30\t\2\2")
        buf.write("\2\30\5\3\2\2\2\31\32\5\n\6\2\32\33\7*\2\2\33\7\3\2\2")
        buf.write("\2\34\37\5\n\6\2\35\37\7+\2\2\36\34\3\2\2\2\36\35\3\2")
        buf.write("\2\2\37\t\3\2\2\2 !\7\23\2\2!#\7#\2\2\"$\5\b\5\2#\"\3")
        buf.write("\2\2\2#$\3\2\2\2$%\3\2\2\2%&\7$\2\2&\13\3\2\2\2\5\22\36")
        buf.write("#")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'boolean'", "'int'", "'float'", 
                     "'string'", "'void'", "'do'", "'while'", "'for'", "'break'", 
                     "'continue'", "'if'", "'else'", "'return'", "'true'", 
                     "'false'", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'!'", "'||'", "'&&'", "'=='", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "'='", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "BOOLEANTYPE", "INTTYPE", 
                      "FLOATTYPE", "STRINGTYPE", "VOIDTYPE", "DO", "WHILE", 
                      "FOR", "BREAK", "CONTINUE", "IF", "ELSE", "RETURN", 
                      "TRUE", "FALSE", "ID", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "NOT", "OR", "AND", "EQUAL", "NOT_EQUAL", "LT", 
                      "GT", "LE", "GE", "ASSIGN", "LB", "RB", "LP", "RP", 
                      "LSB", "RSB", "COMA", "SEMI", "INTLIT", "FLOATLIT", 
                      "BOOLEANLIT", "STRINGLIT", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_mctype = 1
    RULE_body = 2
    RULE_exp = 3
    RULE_funcall = 4

    ruleNames =  [ "program", "mctype", "body", "exp", "funcall" ]

    EOF = Token.EOF
    T__0=1
    BOOLEANTYPE=2
    INTTYPE=3
    FLOATTYPE=4
    STRINGTYPE=5
    VOIDTYPE=6
    DO=7
    WHILE=8
    FOR=9
    BREAK=10
    CONTINUE=11
    IF=12
    ELSE=13
    RETURN=14
    TRUE=15
    FALSE=16
    ID=17
    ADD=18
    SUB=19
    MUL=20
    DIV=21
    MOD=22
    NOT=23
    OR=24
    AND=25
    EQUAL=26
    NOT_EQUAL=27
    LT=28
    GT=29
    LE=30
    GE=31
    ASSIGN=32
    LB=33
    RB=34
    LP=35
    RP=36
    LSB=37
    RSB=38
    COMA=39
    SEMI=40
    INTLIT=41
    FLOATLIT=42
    BOOLEANLIT=43
    STRINGLIT=44
    WS=45
    UNCLOSE_STRING=46
    ILLEGAL_ESCAPE=47
    ERROR_CHAR=48

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mctype(self):
            return self.getTypedRuleContext(MCParser.MctypeContext,0)


        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def body(self):
            return self.getTypedRuleContext(MCParser.BodyContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_program




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.mctype()
            self.state = 11
            self.match(MCParser.T__0)
            self.state = 12
            self.match(MCParser.LB)
            self.state = 13
            self.match(MCParser.RB)
            self.state = 14
            self.match(MCParser.LP)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.ID:
                self.state = 15
                self.body()


            self.state = 18
            self.match(MCParser.RP)
            self.state = 19
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MctypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MCParser.INTTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(MCParser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_mctype




    def mctype(self):

        localctx = MCParser.MctypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mctype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            _la = self._input.LA(1)
            if not(_la==MCParser.INTTYPE or _la==MCParser.VOIDTYPE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(MCParser.FuncallContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_body




    def body(self):

        localctx = MCParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.funcall()
            self.state = 24
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(MCParser.FuncallContext,0)


        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp




    def exp(self):

        localctx = MCParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exp)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.funcall()
                pass
            elif token in [MCParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(MCParser.INTLIT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_funcall




    def funcall(self):

        localctx = MCParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(MCParser.ID)
            self.state = 31
            self.match(MCParser.LB)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.ID or _la==MCParser.INTLIT:
                self.state = 32
                self.exp()


            self.state = 35
            self.match(MCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





