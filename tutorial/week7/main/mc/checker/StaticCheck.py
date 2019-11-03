
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

    def visitProgram(self,ast, c): 
        for x in ast.decl:
            c.append(self.visit(x, c))
        return c

    def visitFuncDecl(self,ast, c):
         # Name
        if ast.name.name in c:
            raise Redeclared(Function(), ast.name.name)
        else:
            local_envi = []
            # Param
            for x in ast.param:
                # name = self.visit(x, local_envi)
                name = x.variable
                
                if name in local_envi:
                    raise Redeclared(Parameter(), name)
                else :
                    local_envi.append(name)
            
            body = self.visit(ast.body, local_envi)
                    
            return ast.name.name

        

        
    
    def visitVarDecl(self, ast, c):
        name = ast.variable

        if name in c:
            raise Redeclared(Variable(), name)
        else:
            return name

    def visitBlock(self, ast, c):
        a = [c.append(self.visitVarDecl(x, c)) for x in ast.member]
    
