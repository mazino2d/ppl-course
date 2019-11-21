
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
    Symbol("putLn",MType([],VoidType()))
    ]
    
              
    def __init__(self,ast):
        self.ast = ast
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c):
        self.list_function=[]
        self.func_call_func= None
        this_prog_global_envi=c[:]
        entry_point=False
        for x in ast.decl:
            if isinstance(x,VarDecl):
                this_prog_global_envi.append(self.visitVarDecl(x,this_prog_global_envi))
            elif isinstance(x,FuncDecl):
                if x.name.name=='main':
                    entry_point=True
                res= self.funcDecl(x,this_prog_global_envi)
                this_prog_global_envi.append(res)
                if res.name != 'main':
                    self.list_function.append(res)

        if not entry_point:
            raise NoEntryPoint()

        for x in ast.decl:
            if isinstance(x,FuncDecl):
                self.func_call_func= x.name.name
                self.visitFuncDecl(x,this_prog_global_envi)

        if len(self.list_function)==0:
            return 
        else:
            raise UnreachableFunction(self.list_function[0].name)        

    def visitVarDecl(self,ast,c):
        res= self.lookup(ast.variable,c,lambda x: x.name)
        if res is None:
            varType= self.visit(ast.varType,c)
            return Symbol(ast.variable,varType)
        else:
            raise Redeclared(Variable(),ast.variable)

    def funcDecl(self,ast,c):
        res= self.lookup(ast.name.name,c,lambda x: x.name)
        if not res is None:
            raise Redeclared(Function(),ast.name.name)          #2.1: Redeclare Function

        param_envi=[]
        param_type=[]
        for param in ast.param:
            if not param.variable in param_envi:
                param_envi.append(param.variable)
                paramType= self.visit(param.varType,c)
                param_type.append(paramType)
            else:
                raise Redeclared(Parameter(),param.variable)    #2.1: Redeclare parameter

        returnType= self.visit(ast.returnType,c)
        return Symbol(ast.name.name,MType(param_type,returnType))
        
    def visitFuncDecl(self,ast, c): 
      
        func_return=False
        local_envi=[]
        param_type=[]
        #reduce(lambda x,y: x + [self.visit(y,x)] if self.lookup(y.variable,x,lambda i: i.name) is None else raise Redeclared(Parameter(),y.variable),ast.param,local_envi)
        for param in ast.param:
            if self.lookup(param.variable,local_envi,lambda x: x.name) is None:
                local_envi.append(self.visit(param,[]))     #local_envi.append(Symbol(param.variable,param.varType)
                varType= self.visit(param.varType,c)
                param_type.append(varType)
            else:
                raise Redeclared(Parameter(),param.variable)    #2.1: Redeclare parameter
        returnType= self.visit(ast.returnType,c)
        #2.5: FunctionNotReturn
        #If Stmt | Func has more than one child: Must has Return

        '''rettype of function: VoidType'''
        if isinstance(returnType,VoidType):
            for member in ast.body.member:
                if isinstance(member,VarDecl):
                    local_envi+= [self.visitVarDecl(member,local_envi)]
                elif type(member) in (BinaryOp,UnaryOp,CallExpr,Id,ArrayCell,IntLiteral,FloatLiteral,StringLiteral,BooleanLiteral):
                    self.visit(member,[local_envi,c])
                else:
                    ref_envi=[local_envi,c]
                    self.visit(member,[ref_envi,False,returnType])

        else:
            '''Otherwise: '''
            if len(ast.body.member)==0:
                raise FunctionNotReturn(ast.name.name)

            elif len(ast.body.member)==1:
                if isinstance(ast.body.member[0],(Return,Block,If,Dowhile)):
                    ref_envi=[local_envi,c]
                    func_return= self.visit(ast.body.member[0],[ref_envi,False,returnType])
                    if func_return==False:
                        raise FunctionNotReturn(ast.name.name)
                else:
                    raise FunctionNotReturn(ast.name.name)

            elif len(ast.body.member)>1:
                func_return=False
                for member in ast.body.member:
                    if isinstance(member,Return):
                        func_return=True
                        break
                    else:
                        continue
                if func_return==False:
                    raise FunctionNotReturn(ast.name.name)

                for member in ast.body.member:
                    if isinstance(member,VarDecl):
                        local_envi+= [self.visitVarDecl(member,local_envi)]
                    elif type(member) in (BinaryOp,UnaryOp,CallExpr,Id,ArrayCell,IntLiteral,FloatLiteral,StringLiteral,BooleanLiteral):
                        self.visit(member,[local_envi,c])
                    else:
                        ref_envi=[local_envi,c]
                        self.visit(member,[ref_envi,False,returnType])

    def visitBlock(self,ast,c):
        trigger=True
        if len(ast.member)==0:
            trigger=False

        elif len(ast.member)==1:
            if isinstance(ast.member[0],(Block,Return,If,Dowhile)):
                trigger= self.visit(ast.member[0],c)                
            else:
                if isinstance(ast.member[0],(For,Break,Continue)):
                    self.visit(ast.member[0],c)
                elif isinstance(ast.member[0],VarDecl):
                    self.visit(ast.member[0],[])
                else:
                    self.visit(ast.member[0],c[0])
                trigger= False
        
        elif len(ast.member)>1:
            trigger=False
            trigger_child=False

            block_envi=[]
            for x in ast.member:
                if isinstance(x,VarDecl):
                    block_envi+= [self.visit(x,block_envi)]
                elif not type(x) in [BinaryOp,UnaryOp,CallExpr,Id,ArrayCell,IntLiteral,FloatLiteral,StringLiteral,BooleanLiteral]:
                    ref_block=[[block_envi]+c[0],c[1],c[2]]
                    trigger_child= self.visit(x,ref_block)
                else:
                    self.visit(x,[block_envi]+c[0])
                if trigger_child==True:
                    trigger=True

        return True if trigger==True else False
        
    def visitDowhile(self,ast,c):
        
        expr= self.visit(ast.exp,c[0])
        if not isinstance(expr,BoolType):
            raise TypeMismatchInStatement(ast)

        trigger= True
        if len(ast.sl)==0:
            trigger= False

        elif len(ast.sl)==1:
            if isinstance(ast.sl[0],(Block,Return,If,Dowhile)):
                trigger= self.visit(ast.sl[0],c)                
            else:
                if isinstance(ast.sl[0],(For,Break,Continue)):
                    self.visit(ast.sl[0],c)
                elif isinstance(ast.sl[0],VarDecl):
                    self.visit(ast.sl[0],[])
                else:
                    self.visit(ast.sl[0],c[0])
                trigger= False
        
        elif len(ast.sl)>1:
            trigger= False
            trigger_child= False
            block_envi=[]

            for x in ast.sl:
                if isinstance(x,VarDecl):
                    block_envi+= [self.visit(x,block_envi)] 
                elif not isinstance(x,Expr):
                    ref_block=[[block_envi]+c[0],c[1],c[2]]
                    trigger_child= self.visit(x,ref_block)
                else:
                    self.visit(x,[block_envi]+c[0])

                if trigger_child==True:
                    trigger= True

        return trigger

    def visitIf(self,ast,c):
        expr= self.visit(ast.expr,c[0])
        if not isinstance(expr,BoolType):
            raise TypeMismatchInStatement(ast)
        
        returnIf= True
        returnElse=True
        if isinstance(ast.thenStmt,(Return,Block,If,Dowhile)):
            returnIf= self.visit(ast.thenStmt,c)

        else:
            if isinstance(ast.thenStmt,(For,Break,Continue)):
                self.visit(ast.thenStmt,c)
            else:
                self.visit(ast.thenStmt,c[0])
            returnIf= False

        
        if ast.elseStmt is None:
            returnElse= False

        else:
            if isinstance(ast.elseStmt,(Return,Block,If,Dowhile)):
                returnElse= self.visit(ast.elseStmt,c)
            else: 
                if isinstance(ast.elseStmt,(For,Break,Continue)):
                    self.visit(ast.elseStmt,c)
                else:
                    self.visit(ast.elseStmt,c[0])
                returnElse= False

        
        return True if returnIf==True and returnElse==True else False

    def visitFor(self,ast,c):
        expr1= self.visit(ast.expr1,c[0])
        expr2= self.visit(ast.expr2,c[0])
        expr3= self.visit(ast.expr3,c[0])

        if not isinstance(expr1,IntType) or\
           not isinstance(expr2,BoolType) or\
           not isinstance(expr3,IntType):
           raise TypeMismatchInStatement(ast)
        
        if type(ast.loop) in (BinaryOp,UnaryOp,CallExpr,Id,ArrayCell,IntLiteral,FloatLiteral,StringLiteral,BooleanLiteral):
            self.visit(ast.loop,c[0])    
        else:
            self.visit(ast.loop,[c[0],True,c[2]])

    def visitReturn(self,ast,c):
        if ast.expr is None:
            if not isinstance(c[-1],VoidType):
                raise TypeMismatchInStatement(ast)
        elif isinstance(c[-1],VoidType):
            raise TypeMismatchInStatement(ast)
        else: 
            res = self.visit(ast.expr,c[0])

            if isinstance(c[-1],ArrayPointerType):
                if isinstance(res,(ArrayPointerType,ArrayType)):
                    if not isinstance(res.eleType,type(c[-1].eleType)):
                        raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInStatement(ast)
            elif isinstance(c[-1],FloatType):
                if not isinstance(res,(IntType,FloatType)):
                    raise TypeMismatchInStatement(ast)
            else:
                if not isinstance(res,type(c[-1])):
                    raise TypeMismatchInStatement(ast)
        return True

    def visitBreak(self,ast,c):
        if c[1] == False:
            raise BreakNotInLoop()

    def visitContinue(self,ast,c):
        if c[1] == False:
            raise ContinueNotInLoop()
    
    def visitCallExpr(self, ast, c): 

        at = [self.visit(x,c) for x in ast.param]

        for lst in c:
            res = self.lookup(ast.method.name,lst,lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(),ast.method.name)

        if len(res.mtype.partype) != len(at):
            raise TypeMismatchInExpression(ast)
        else:
            for i in range(0,len(at)):
                if isinstance(res.mtype.partype[i],ArrayPointerType):
                    if isinstance(at[i],(ArrayType,ArrayPointerType)):
                        if not isinstance(res.mtype.partype[i].eleType,type(at[i].eleType)):
                            raise TypeMismatchInExpression(ast)
                    else:
                        raise TypeMismatchInExpression(ast)
                elif isinstance(res.mtype.partype[i],FloatType) and isinstance(at[i],(FloatType,IntType)):
                    continue
                elif isinstance(res.mtype.partype[i],type(at[i])):
                    continue
                else: 
                    raise TypeMismatchInExpression(ast)

            if self.func_call_func != res.name:
                x= self.lookup(res.name,self.list_function,lambda x: x.name)
                if not x is None:
                    self.list_function.remove(res)

        return res.mtype.rettype

    def visitId(self,ast,c):

        res= None
        for lst in c:
            res= self.lookup(ast.name,lst,lambda x: x.name)
            if not res is None:
                break

        if res is None:
            raise Undeclared(Identifier(),ast.name)
        else:
            if not type(res.mtype) is MType:
                return res.mtype
            else:
                return res.mtype.rettype

    def visitArrayCell(self,ast,c):
        arr= self.visit(ast.arr,c)
        idx= self.visit(ast.idx,c)

        if not isinstance(arr,(ArrayType,ArrayPointerType)):
            raise TypeMismatchInExpression(ast)
        if not isinstance(idx,IntType):
            raise TypeMismatchInExpression(ast)

        return arr.eleType

    def visitUnaryOp(self,ast,c):
        op=ast.op
        expr=self.visit(ast.body,c)

        if op == '!':
            if isinstance(expr,BoolType):
                return BoolType()
            else: 
                raise TypeMismatchInExpression(ast)
        
        if op == '-':
            if isinstance(expr,(IntType,FloatType)):
                return expr
            else:
                raise TypeMismatchInExpression(ast)

    def visitBinaryOp(self,ast,c):
        op=ast.op
        left=self.visit(ast.left,c)
        right=self.visit(ast.right,c)

        def checkType(acceptType, returnType=None):
            if not isinstance(left, acceptType) or\
               not isinstance(right, acceptType):
                raise TypeMismatchInExpression(ast)

        if op in ['+','-','*','/']:
            checkType((IntType, FloatType))
            if isinstance(left, IntType) and\
               isinstance(right, IntType):
                return IntType()
            else:
                return FloatType()
        elif op == '%':
            checkType(IntType)
            return IntType()
        elif op in ['!=', '==']:
            checkType((IntType,BoolType))
            return BoolType()
        elif op in ['<', '<=', '>', '>=']:
            checkType((IntType, FloatType))
            return BoolType()
        elif op in ['&&', '||']:
            checkType(BoolType)
            return BoolType()
        elif op == '=':
            if not type(ast.left) in (Id,ArrayCell):
                raise NotLeftValue(ast.left)

            if isinstance(left,(VoidType,ArrayType,ArrayPointerType)):
                raise TypeMismatchInExpression(ast)
            if isinstance(left,FloatType):
                if not isinstance(right,(IntType,FloatType)):
                    raise TypeMismatchInExpression(ast)
            elif not isinstance(left,type(right)):
                raise TypeMismatchInExpression(ast)
            else:
                return left
        
    def visitIntLiteral(self,ast, c): 
        return IntType()

    def visitFloatLiteral(self,ast,c):
        return FloatType()
    
    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitIntType(self,ast,c):
        return IntType()

    def visitFloatType(self,ast,c):
        return FloatType()

    def visitStringType(self,ast,c):
        return StringType()

    def visitBoolType(self,ast,c):
        return BoolType()

    def visitVoidType(self,ast,c):
        return VoidType()
        
    def visitArrayType(self,ast,c):
        eleType= self.visit(ast.eleType,c)
        return ArrayType(ast.dimen,eleType)

    def visitArrayPointerType(self,ast,c):
        eleType= self.visit(ast.eleType,c)
        return ArrayPointerType(eleType)
