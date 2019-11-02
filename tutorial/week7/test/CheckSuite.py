import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_right(self):
        """Simple program"""
        input = Program([
             VarDecl('a',IntType()),
            FuncDecl(Id("main"),[],IntType(),Block([]))])

        expect = "['a', 'main']"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_1(self):
        """Redeclared program"""
        input = Program([
             VarDecl('a',IntType()),
             VarDecl('a',IntType()),
            FuncDecl(Id("main"),[],IntType(),Block([]))])

        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,402))
