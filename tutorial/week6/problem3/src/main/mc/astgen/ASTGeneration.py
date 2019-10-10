from MCVisitor import MCVisitor
from MCParser import MCParser
from functools import reduce
from AST import *

class ASTGeneration(MCVisitor):
    def visitExp(self,ctx:MCParser.ExpContext):
        return Binary(ctx.COMPARE().getText(), self.visit(ctx.term(0)), self.visit(ctx.term(1))) if ctx.COMPARE() else self.visit(ctx.term(0))

    def visitTerm(self,ctx:MCParser.TermContext):
        return Binary(ctx.EXPONENT().getText(), self.visit(ctx.factor()), self.visit(ctx.term())) if ctx.EXPONENT() else self.visit(ctx.factor())

    def visitFactor(self,ctx:MCParser.FactorContext):
        dl = zip(ctx.ANDOR(), ctx.operand()[1:])
        return reduce(lambda x,y: Binary(y[0].getText(), x, self.visit(y[1])), dl, self.visit(ctx.operand(0)))
  
    def visitOperand(self,ctx:MCParser.OperandContext):
        if ctx.exp() :
            return self.visit(ctx.exp()) 
        elif ctx.INTLIT() :
            return IntLit(int(ctx.INTLIT().getText()))
        else:
            return BoolLit(True if (ctx.BOOLIT().getText() == "true") else False)
        