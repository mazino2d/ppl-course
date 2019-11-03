import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_right(self):
        """Redeclared program"""
        input = Program([
                VarDecl('t',IntType()),
            FuncDecl(Id("main"),[],IntType(),Block([]))])

        expect = "['main', 't']"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_global(self):
        """Redeclared program"""
        input = Program([
                VarDecl('a',IntType()),
                VarDecl('a',IntType()),
                FuncDecl(Id("main"),[],IntType(),Block([]))])

        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclared_local(self):
        """Redeclared program"""
        input = Program([
                FuncDecl(Id("main"),[],IntType(),Block([
                    VarDecl('a',IntType()),
                    VarDecl('a',IntType())
                ]))
            ])

        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_para(self):
        """Redeclared program"""
        input = Program([
                FuncDecl(Id("main"),[VarDecl('a',IntType())],IntType(),Block([
                    VarDecl('a',IntType())
                ]))
            ])

        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,404))
