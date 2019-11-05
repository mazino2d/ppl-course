
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
        #print(ast)
        #print(ast)
        #print()
        self.ast = ast

 
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c):
        program_envi = 0

        # check No Entry Point exception (2.7)
        for x in ast.decl: 
            if isinstance(x, FuncDecl):
                if x.name.name == 'main':
                    if isinstance(x.returnType, VoidType): program_envi = 1
        
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
        
        # vist list of local variable
        # TODO : check if return type of function is void
        # isReturn = False
        # for x in ast.body:
        #     if self.visit(x, ()) is True:
        #         isReturn = 


        # check if function exists
        if self.lookup(ast.name.name, c, lambda x: x.name):
            raise Redeclared(Function(), ast.name)
        else:
            return Symbol(ast.name.name, ast.returnType)

    def visitVarDecl(self, ast, c):
        # check if variable exists
        if self.lookup(ast.variable, c, lambda x: x.name):
            raise Redeclared(Variable(), ast.name)
        else:
            return Symbol(ast.variable, ast.varType)

    def visitCallExpr(self, ast, c): 
        at = [self.visit(x,(c[0],False)) for x in ast.param]
        
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(),ast.method.name)
        elif len(res.mtype.partype) != len(at):
            if c[1]:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        else:
            return res.mtype.rettype

    def visitIntLiteral(self,ast, c): 
        return IntType()
    

