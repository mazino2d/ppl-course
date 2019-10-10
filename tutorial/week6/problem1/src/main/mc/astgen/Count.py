from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class Count(MCVisitor):
    def visitProgram(self,ctx:MCParser.ProgramContext):
        return 1 + self.visit(ctx.vardecls())

    def visitMctype(self,ctx:MCParser.MctypeContext):
        return 5 + self.visit(ctx.mctype()) if (ctx.getChildCount() == 6) else 1

    def visitVardecls(self,ctx:MCParser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecls()) if (ctx.vardecls()) else self.visit(ctx.vardecl())
  	
    def visitVardecl(self,ctx:MCParser.VardeclContext):
        return 1 + self.visit(ctx.mctype()) + self.visit(ctx.ids())

    def visitIds(self,ctx:MCParser.IdsContext):
        return len(ctx.ID()) + len(ctx.COMMA())

