from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
    def visitProgram(self, ctx:MCParser.ProgramContext):
        decllist = list()
        for x in ctx.declaration():
            decl = self.visitDeclaration(x)
            if isinstance(decl, list):
                decllist.extend(decl)
            else:
                decllist.append(decl)
        return Program(decllist)

    def visitDeclaration(self, ctx:MCParser.DeclarationContext):
        return self.visitChildren(ctx)

    def visitVardecl(self, ctx:MCParser.VardeclContext):
        primtype = self.visitPrimtype(ctx.primtype())
        varlist = self.visitVarlist(ctx.varlist())
        return [VarDecl(x[0], ArrayType(x[1], primtype)) if isinstance(x, tuple) else VarDecl(x, primtype) for x in varlist]

    def visitPrimtype(self, ctx:MCParser.PrimtypeContext):
        if ctx.INTTYPE(): return IntType()
        elif ctx.FLOATTYPE(): return FloatType()
        elif ctx.BOOLEANTYPE(): return BoolType()
        elif ctx.STRINGTYPE() : return StringType()

    def visitVarlist(self, ctx:MCParser.VarlistContext):
        if ctx.varlist() :
            return [self.visitVar(ctx.var())] + self.visitVarlist(ctx.varlist())
        else :
            return [self.visitVar(ctx.var())]
        
    def visitVar(self, ctx:MCParser.VarContext):
        if ctx.INTLIT() :
            return (Id(ctx.ID().getText()), IntLiteral(int(ctx.INTLIT().getText())))
        else :
            return Id(ctx.ID().getText())


    def visitFuncdecl(self, ctx:MCParser.FuncdeclContext):
        functiontype = self.visitFunctype(ctx.functype())
        functionname = Id(ctx.ID().getText())
        paralist = (self.visitParalist(ctx.paralist()) if ctx.paralist() else [])
        blockstmt = self.visitBlockstmt(ctx.blockstmt())
        return FuncDecl(functionname, paralist, functiontype, blockstmt)

    def visitFunctype(self, ctx:MCParser.FunctypeContext):
        if ctx.primtype() :  return self.visitPrimtype(ctx.primtype())
        elif ctx.arraytype() : return self.visitArraytype(ctx.arraytype())
        else : return VoidType()

    def visitArraytype(self, ctx:MCParser.ArraytypeContext):
        primtype = self.visitPrimtype(ctx.primtype())
        return ArrayPointerType(primtype)

    def visitParalist(self, ctx:MCParser.ParalistContext):
        return [self.visitParadecl(x) for x in ctx.paradecl()]

    def visitParadecl(self, ctx:MCParser.ParadeclContext):
        funcname = Id(ctx.ID().getText())
        primtype = self.visitPrimtype(ctx.primtype())
        if ctx.LSB() and ctx.RSB() :
            return VarDecl(funcname, ArrayPointerType(primtype))
        else :
            return VarDecl(funcname, primtype)

    def visitBlockstmt(self, ctx:MCParser.BlockstmtContext):
        return Block([])
    def visitStmt(self, ctx:MCParser.StmtContext):
        return self.visitChildren(ctx)
    def visitIfstmt(self, ctx:MCParser.IfstmtContext):
        return self.visitChildren(ctx)
    def visitWhilestmt(self, ctx:MCParser.WhilestmtContext):
        return self.visitChildren(ctx)
    def visitForstmt(self, ctx:MCParser.ForstmtContext):
        return self.visitChildren(ctx)
    def visitBreakstmt(self, ctx:MCParser.BreakstmtContext):
        return self.visitChildren(ctx)
    def visitContinuestmt(self, ctx:MCParser.ContinuestmtContext):
        return self.visitChildren(ctx)
    def visitReturnstmt(self, ctx:MCParser.ReturnstmtContext):
        return self.visitChildren(ctx)
    def visitExprstmt(self, ctx:MCParser.ExprstmtContext):
        return self.visitChildren(ctx)


    def visitExpr0(self, ctx:MCParser.Expr0Context):
        return self.visitChildren(ctx)
    def visitExpr1(self, ctx:MCParser.Expr1Context):
        return self.visitChildren(ctx)
    def visitExpr2(self, ctx:MCParser.Expr2Context):
        return self.visitChildren(ctx)
    def visitExpr3(self, ctx:MCParser.Expr3Context):
        return self.visitChildren(ctx)
    def visitExpr4(self, ctx:MCParser.Expr4Context):
        return self.visitChildren(ctx)
    def visitExpr5(self, ctx:MCParser.Expr5Context):
        return self.visitChildren(ctx)
    def visitExpr6(self, ctx:MCParser.Expr6Context):
        return self.visitChildren(ctx)
    def visitExpr7(self, ctx:MCParser.Expr7Context):
        return self.visitChildren(ctx)
    def visitExpr8(self, ctx:MCParser.Expr8Context):
        return self.visitChildren(ctx)
    def visitExpr9(self, ctx:MCParser.Expr9Context):
        return self.visitChildren(ctx)

    def visitOperand(self, ctx:MCParser.OperandContext):
        return self.visitChildren(ctx)
    def visitCalfunc(self, ctx:MCParser.CalfuncContext):
        return self.visitChildren(ctx)
    def visitArglist(self, ctx:MCParser.ArglistContext):
        return self.visitChildren(ctx)  
    