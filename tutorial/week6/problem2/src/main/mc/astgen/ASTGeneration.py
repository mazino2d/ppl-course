from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
    def visitProgram(self,ctx:MCParser.ProgramContext):
        return Program(self.visit(ctx.vardecls()))

    def visitVardecls(self,ctx:MCParser.VardeclsContext):
        return [self.visit(ctx.vardecl())] + self.visit(ctx.vardecls()) if (ctx.vardecls()) else [self.visit(ctx.vardecl())]

    def visitVardecl(self,ctx:MCParser.VardeclContext):
        return VarDecl(self.visit(ctx.mctype()), self.visit(ctx.ids()))
  	
    def visitMctype(self,ctx:MCParser.MctypeContext):
        return IntType() if (ctx.INTTYPE()) else FloatType()

    def visitIds(self,ctx:MCParser.IdsContext):
        return [x.getText() for x in ctx.ID()]
