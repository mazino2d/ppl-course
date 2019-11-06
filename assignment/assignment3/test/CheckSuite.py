import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_simple_main_program(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_no_main_program(self):
        input = Program([FuncDecl(Id("abc"),[],VoidType(),Block([]))])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_global_variable(self):
        input = Program([
            FuncDecl(Id("main"),[],VoidType(),Block([])),
            VarDecl('a', IntType()), VarDecl('a', IntType())
            ])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclared_parameter(self):
        input = Program([FuncDecl(Id("main"),[
            VarDecl('a', IntType()), VarDecl('a', IntType())
        ],VoidType(),Block([]))])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,403))
    
    def test_redeclared_function(self):
        input = Program([
            FuncDecl(Id("main"),[],VoidType(),Block([])),
            FuncDecl(Id("a"),[],VoidType(),Block([])),
            FuncDecl(Id("a"),[],VoidType(),Block([]))])
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_type_mismatch_plus_op(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([
            BinaryOp("+",StringLiteral("a"),StringLiteral("a"))
        ]))])
        expect = "Type Mismatch In Expression: BinaryOp(+,StringLiteral(a),StringLiteral(a))"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_type_mismatch_subtract_op(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([
            BinaryOp("-",BooleanLiteral("true"),StringLiteral("a"))
        ]))])
        expect = "Type Mismatch In Expression: BinaryOp(-,BooleanLiteral(true),StringLiteral(a))"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_type_mismatch_multiple_op(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([
            BinaryOp("+",BooleanLiteral("true"),IntLiteral(10))
        ]))])
        expect = "Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(true),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_type_mismatch_division_op(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([
            BinaryOp("/",BooleanLiteral("true"),IntLiteral(10))
        ]))])
        expect = "Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(true),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_type_mismatch_module_op(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([
            BinaryOp("%",FloatLiteral(10.5),IntLiteral(10))
        ]))])
        expect = "Type Mismatch In Expression: BinaryOp(%,FloatLiteral(10.5),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,409))
    
    def test_type_mismatch_or_op(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([
            BinaryOp("||",FloatLiteral(10.5),IntLiteral(10))
        ]))])
        expect = "Type Mismatch In Expression: BinaryOp(||,FloatLiteral(10.5),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_type_mismatch_and_op(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([
            BinaryOp("&&",FloatLiteral(10.5),IntLiteral(10))
        ]))])
        expect = "Type Mismatch In Expression: BinaryOp(&&,FloatLiteral(10.5),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_type_mismatch_plus_op_right(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([
            BinaryOp("+",FloatLiteral(2.5),FloatLiteral(10))
        ]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_type_mismatch_module_op_right(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([
            BinaryOp("%",IntLiteral(2),IntLiteral(10))
        ]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_type_mismatch_less_op(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([
            BinaryOp("<",StringLiteral('a'),IntLiteral(10))
        ]))])
        expect = "Type Mismatch In Expression: BinaryOp(<,StringLiteral(a),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_type_mismatch_great_op(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([
            BinaryOp(">",StringLiteral('a'),IntLiteral(10))
        ]))])
        expect = "Type Mismatch In Expression: BinaryOp(>,StringLiteral(a),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_type_mismatch_less_op_right(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([
            BinaryOp("<",IntLiteral(10),IntLiteral(10))
        ]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_type_mismatch_great_op_right(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([
            BinaryOp(">",IntLiteral(10),IntLiteral(10))
        ]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,417))

    # def test_type_mismatch_negative_op_right(self):
    #     input = Program([FuncDecl(Id("main"),[],VoidType(),Block([
    #         UnaryOp("-",IntLiteral(10))
    #     ]))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,418))
    
    # def test_type_mismatch_negative_op(self):
    #     input = Program([FuncDecl(Id("main"),[],VoidType(),Block([
    #         UnaryOp("-",BooleanLiteral(10))
    #     ]))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,419))