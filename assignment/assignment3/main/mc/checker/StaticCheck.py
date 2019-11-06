
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
        Symbol("getInt",MType([],IntType())),
        Symbol("putInt",MType([IntType()],VoidType())),
        Symbol("putIntLn",MType([IntType()],VoidType())),
        Symbol("getFloat",MType([],FloatType())),
        Symbol("putFloat",MType([FloatType()],VoidType())),
        Symbol("putFloatLn",MType([FloatType()],VoidType())),
        Symbol("putBool",MType([BoolType()],VoidType())),
        Symbol("putBoolLn",MType([BoolType()],VoidType())),
        Symbol("putString",MType([StringType()],VoidType())),
        Symbol("putStringLn",MType([StringType()],VoidType())),
        Symbol("putLn",MType([],VoidType())),
    ]
              
    def __init__(self,ast):
        # print(ast)
        # print(ast)
        # print()
        self.ast = ast

 
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c):
        program_envi = 0
        # check No Entry Point exception (2.7)
        for x in ast.decl:
            if isinstance(x, FuncDecl):
                if x.name.name == 'main':
                    if isinstance(x.returnType, VoidType): 
                        program_envi = 1; break
        
        if program_envi == 0 : raise NoEntryPoint()

        # visit global variable and function declaration
        program_envi = c[:]
        
        for x in ast.decl:
            program_envi += [self.visit(x, program_envi)]

        # return program environment
        return program_envi

    def visitFuncDecl(self,ast, c):
        local_envi = []

        # visit list of function parameter
        for x in ast.param:
            try:
                local_envi += [self.visit(x, local_envi)]
            except Redeclared as e:
                raise Redeclared(Parameter(), e.n)
        
        # vist block of function
        self.visit(ast.body, local_envi)

        # TODO : check if return type of function is void
        # isReturn = False
        
        # check if function exists
        if self.lookup(ast.name.name, c, lambda x: x.name):
            raise Redeclared(Function(), ast.name.name)
        else:
            return Symbol(ast.name.name, ast.returnType)

    def visitVarDecl(self, ast, c):
        # check if variable exists
        if self.lookup(ast.variable, c, lambda x: x.name):
            raise Redeclared(Variable(), ast.variable)
        else:
            return Symbol(ast.variable, ast.vze)

    def visitIntLiteral(self,ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitBinaryOp(self, ast, c):
        # TODO : Assignment operator, equal and not not_equal
        ############################
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)
        op = ast.op

        def checkType(acceptType, returnType=None):
            if not isinstance(left, acceptType) or\
               not isinstance(right, acceptType):
                raise TypeMismatchInExpression(ast)
        
        if op in ['+', '-', '*', '/']:
            checkType((IntType, FloatType))
            if isinstance(left, IntType) and\
               isinstance(right, IntType):
                return IntType()
            else:
                return FloatType()
        elif op in ['%']:
            checkType(IntType)
            return IntType()
        elif op in ['&&', '||']:
            checkType(BoolType)
            return BoolType()
        elif op in ['<', '<=', '>', '>=']:
            checkType((IntType, FloatType))
            return BoolType()
    
    def visitUnaryOp(self, ast, c):
        # TODO: Index operater
        ######################
        op = ast.op
        exp = self.visit(ast.Expr)

        if op == '-':
            if isinstance(exp, (IntType, FloatType)):
                return exp
            else:
                return TypeMismatchInExpression(ast)
        
        if op == '!':
            if isinstance(exp, BoolType):
                return BoolType()
            else:
                return TypeMismatchInExpression(ast)

    def visitBlock(self, ast, c):
        for x in ast.member:
            self.visit(x, c)



