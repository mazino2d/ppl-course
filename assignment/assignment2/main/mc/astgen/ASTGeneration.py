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
        instructionList = []
        for x in ctx.instruction():
            ins =  self.visitInstruction(x)
            if isinstance(ins, list):
                instructionList.extend(ins)
            else:
                instructionList.append(ins)
        return Block(instructionList)

    def visitInstruction(self, ctx:MCParser.InstructionContext):
        return self.visitChildren(ctx)

    def visitStmt(self, ctx:MCParser.StmtContext):
        return self.visitChildren(ctx)

    def visitIfstmt(self, ctx:MCParser.IfstmtContext):
        expr = self.visitExpr0(ctx.expr0())
        thenStmt = self.visitStmt(ctx.stmt(0))
        elseStmt =  self.visitStmt(ctx.stmt(1)) if ctx.ELSE() else None

        return If(expr, thenStmt, elseStmt)

    def visitWhilestmt(self, ctx:MCParser.WhilestmtContext):
        expr = self.visitExpr0(ctx.expr0())
        stmtList = [self.visitStmt(x) for x in ctx.stmt()]
        return Dowhile(stmtList, expr)
        
    def visitForstmt(self, ctx:MCParser.ForstmtContext):
        expr1 = self.visitExpr0(ctx.expr0(0))
        expr2 = self.visitExpr0(ctx.expr0(1))
        expr3 = self.visitExpr0(ctx.expr0(2))
        loop = self.visitStmt(ctx.stmt())
        return For(expr1, expr2, expr3, loop)

    def visitBreakstmt(self, ctx:MCParser.BreakstmtContext):
        return Break()

    def visitContinuestmt(self, ctx:MCParser.ContinuestmtContext):
        return Continue()

    def visitReturnstmt(self, ctx:MCParser.ReturnstmtContext):
        return Return(self.visitExpr0(ctx.expr0())) if ctx.expr0() else Return()

    def visitExprstmt(self, ctx:MCParser.ExprstmtContext):
        return self.visitExpr0(ctx.expr0())

    def visitExpr0(self, ctx:MCParser.Expr0Context):
        if ctx.ASSIGN():
            op = ctx.ASSIGN().getText()
            left = self.visitExpr1(ctx.expr1())
            right = self.visitExpr0(ctx.expr0())
            return BinaryOp(op, left, right)
        else:
            return self.visitExpr1(ctx.expr1())

    def visitExpr1(self, ctx:MCParser.Expr1Context):
        if ctx.OR():
            op = ctx.OR().getText()
            left = self.visitExpr1(ctx.expr1())
            right = self.visitExpr2(ctx.expr2())
            return BinaryOp(op, left, right)
        else:
            return self.visitExpr2(ctx.expr2())

    def visitExpr2(self, ctx:MCParser.Expr2Context):
        if ctx.AND():
            op = ctx.AND().getText()
            left = self.visitExpr2(ctx.expr2())
            right = self.visitExpr3(ctx.expr3())
            return BinaryOp(op, left, right)
        else:
            return self.visitExpr3(ctx.expr3())

    def visitExpr3(self, ctx:MCParser.Expr3Context):
        if ctx.EQ():
            left = self.visitExpr4(ctx.expr4(0))
            right = self.visitExpr4(ctx.expr4(1))
            op = ctx.EQ().getText()
            return BinaryOp(op, left, right)
        elif ctx.NE():
            left = self.visitExpr4(ctx.expr4(0))
            right = self.visitExpr4(ctx.expr4(1))
            op = ctx.NE().getText()
            return BinaryOp(op, left, right)
        else:
            return self.visitExpr4(ctx.expr4(0))

    def visitExpr4(self, ctx:MCParser.Expr4Context):
        if ctx.LT():
            left = self.visitExpr5(ctx.expr5(0))
            right = self.visitExpr5(ctx.expr5(1))
            op = ctx.LT().getText()
            return BinaryOp(op, left, right)
        elif ctx.LE():
            left = self.visitExpr5(ctx.expr5(0))
            right = self.visitExpr5(ctx.expr5(1))
            op = ctx.LE().getText()
            return BinaryOp(op, left, right)
        elif ctx.GT():
            left = self.visitExpr5(ctx.expr5(0))
            right = self.visitExpr5(ctx.expr5(1))
            op = ctx.GT().getText()
            return BinaryOp(op, left, right)
        elif ctx.GE():
            left = self.visitExpr5(ctx.expr5(0))
            right = self.visitExpr5(ctx.expr5(1))
            op = ctx.GE().getText()
            return BinaryOp(op, left, right)
        else:
            return self.visitExpr5(ctx.expr5(0))

    def visitExpr5(self, ctx:MCParser.Expr5Context):
        if ctx.ADD():
            op = ctx.ADD().getText()
            left = self.visitExpr5(ctx.expr5())
            right = self.visitExpr6(ctx.expr6())
            return BinaryOp(op, left, right)
        elif ctx.SUB():
            op = ctx.SUB().getText()
            left = self.visitExpr5(ctx.expr5())
            right = self.visitExpr6(ctx.expr6())
            return BinaryOp(op, left, right)
        else:
            return self.visitExpr6(ctx.expr6())
            
    def visitExpr6(self, ctx:MCParser.Expr6Context):
        if ctx.MUL():
            op = ctx.MUL().getText()
            left = self.visitExpr6(ctx.expr6())
            right = self.visitExpr7(ctx.expr7())
            return BinaryOp(op, left, right)
        elif ctx.DIV():
            op = ctx.DIV().getText()
            left = self.visitExpr6(ctx.expr6())
            right = self.visitExpr7(ctx.expr7())
            return BinaryOp(op, left, right)
        elif ctx.MOD():
            op = ctx.MOD().getText()
            left = self.visitExpr6(ctx.expr6())
            right = self.visitExpr7(ctx.expr7())
            return BinaryOp(op, left, right)
        else:
            return self.visitExpr7(ctx.expr7())

    def visitExpr7(self, ctx:MCParser.Expr7Context):
        if ctx.NOT():
            op = ctx.NOT().getText()
            body = self.visitExpr7(ctx.expr7())
            return UnaryOp(op, body)
        elif ctx.SUB():
            op = ctx.SUB().getText()
            body = self.visitExpr7(ctx.expr7())
            return UnaryOp(op, body)
        else:
            return self.visitExpr8(ctx.expr8())

    def visitExpr8(self, ctx:MCParser.Expr8Context):
        if ctx.LSB() and ctx.RSB():
            arr = self.visitExpr9(ctx.expr9())
            idx = self.visitExpr0(ctx.expr0())
            return ArrayCell(arr, idx)
        else:
            return self.visitExpr9(ctx.expr9())

    def visitExpr9(self, ctx:MCParser.Expr9Context):
        if ctx.LB() and ctx.RB():
            return self.visitExpr0(ctx.expr0())
        else:
            return self.visitOperand(ctx.operand())

    def visitOperand(self, ctx:MCParser.OperandContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.BOOLEANLIT():
            return BooleanLiteral(True if ctx.BOOLEANLIT().getText() == "true" else False)
        elif ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visitCalfunc(ctx.calfunc())

    def visitCalfunc(self, ctx:MCParser.CalfuncContext):
        method = Id(ctx.ID().getText())
        param = self.visitArglist(ctx.arglist())
        return CallExpr(method, param)
        
    def visitArglist(self, ctx:MCParser.ArglistContext):
        return [self.visitExpr0(x) for x in ctx.expr0()]
    