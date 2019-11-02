
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

    global_envi = []
            
    
    def __init__(self,ast):
        #print(ast)
        #print(ast)
        #print()
        self.ast = ast

 
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)
# Problem 1
    # def visitProgram(self,ast, c): 
    #     return [self.visit(x,c) for x in ast.decl]

    # def visitFuncDecl(self,ast, c): 
    #     return ast.name.name
    
    # def visitVarDecl(self, ast, c):
    #     return ast.variable

# Problem 1
    def visitProgram(self,ast, c): 
        for x in ast.decl:
            c.append(self.visit(x, c))
        return c

    def visitFuncDecl(self,ast, c): 
        name = ast.name.name

        if name in c:
            raise Redeclared(Function(), name)
        else:
            return name
    
    def visitVarDecl(self, ast, c):
        name = ast.variable

        if name in c:
            raise Redeclared(Variable(), name)
        else:
            return name

    
