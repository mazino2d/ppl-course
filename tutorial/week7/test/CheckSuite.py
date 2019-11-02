import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_diff_numofparam_stmt_use_ast(self):
        """More complex program"""
        input = Program([
            VarDecl('a',IntType()),
            FuncDecl(Id("main"),[],IntType(),Block([])), 
            FuncDecl(Id("main"),[],IntType(),Block([]))])
            
        expect = "['a', 'main', 'main']"
        self.assertTrue(TestChecker.test(input,expect,405))

