import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # Test variable declaration
    def test_single_variable_declaration(self):
        input = """int a;"""
        expect = "Program([VarDecl(Id(a),IntType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,300))
    def test_single_array_declaration_float(self):
        input = """float a[5];"""
        expect = "Program([VarDecl(Id(a),ArrayType(FloatType,IntLiteral(5)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    def test_single_array_declaration_int(self):
        input = """int a[5];"""
        expect = "Program([VarDecl(Id(a),ArrayType(IntType,IntLiteral(5)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_multi_variable_declaration(self):
        input = """boolean a,b;"""
        expect = "Program([VarDecl(Id(a),BoolType),VarDecl(Id(b),BoolType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    def test_multi_array_declaration(self):
        input = """boolean a[10],b[5];"""
        expect = "Program([VarDecl(Id(a),ArrayType(BoolType,IntLiteral(10))),VarDecl(Id(b),ArrayType(BoolType,IntLiteral(5)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    def test_mix_variable_declaration(self):
        input = """boolean a,b[5];"""
        expect = "Program([VarDecl(Id(a),BoolType),VarDecl(Id(b),ArrayType(BoolType,IntLiteral(5)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    # Test program with variable declaration
    def test_program_multi_variable_declaration(self):
        input = """int a; float b; boolean c;"""
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType),VarDecl(Id(c),BoolType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    def test_program_multi_array_declaration(self):
        input = """int a[5]; float b[6]; boolean c[7];"""
        expect = "Program([VarDecl(Id(a),ArrayType(IntType,IntLiteral(5))),VarDecl(Id(b),ArrayType(FloatType,IntLiteral(6))),VarDecl(Id(c),ArrayType(BoolType,IntLiteral(7)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    def test_program_miss_semi_colon(self):
        input = """int a; float b"""
        expect = "Program([VarDecl(Id(a),IntType),None,None])"
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test_program_wrong_variable_type(self):
        input = """intl a; float b"""
        expect = "Program([])"
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    def test_program_empty(self):
        input = """"""
        expect = "Program([])"
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    # # Test function parameter
    def test_function_para_empty(self):
        input = """int main() {}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    def test_function_single_para(self):
        input = """int main(int a) {}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(Id(a),IntType)],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    def test_function_multi_para(self):
        input = """void main(boolean a, float b) {}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(Id(a),BoolType),VarDecl(Id(b),FloatType)],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    def test_function_single_array(self):
        input = """void main(boolean a[]) {}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(Id(a),ArrayTypePointer(BoolType))],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    def test_function_multi_array(self):
        input = """void main(boolean a[], float b[]) {}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(Id(a),ArrayTypePointer(BoolType)),VarDecl(Id(b),ArrayTypePointer(FloatType))],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    # Test program with function parameter
    def test_function_type_array(self):
        input = """int[] main() {}"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test_function_void_type_array(self):
        input = """void main() {}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    def test_program_multi_function(self):
        input = """int[] main() {} float[] pow() {}"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([])),FuncDecl(Id(pow),[],ArrayTypePointer(FloatType),Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    def test_program_multi_function_variable(self):
        input = """int[] main() {} float[] pow() {} int a,b,c;"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([])),FuncDecl(Id(pow),[],ArrayTypePointer(FloatType),Block([])),VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    def test_program_multi_function_array(self):
        input = """int[] main() {} float[] pow() {} int a[5],b[5],c[5];"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([])),FuncDecl(Id(pow),[],ArrayTypePointer(FloatType),Block([])),VarDecl(Id(a),ArrayType(IntType,IntLiteral(5))),VarDecl(Id(b),ArrayType(IntType,IntLiteral(5))),VarDecl(Id(c),ArrayType(IntType,IntLiteral(5)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    # Test if statement
    def test_if_stmt_base(self):
        input = """void main() {if(true) print("hello");}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BooleanLiteral(true),CallExpr(Id(print),[StringLiteral(hello)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    def test_if__else_stmt_base(self):
        input = """void main() {if(true) print("hello"); else put(5)}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BooleanLiteral(true),CallExpr(Id(print),[StringLiteral(hello)]),CallExpr(Id(put),[IntLiteral(5)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    def test_if_stmt_hard(self):
        input = """void main() {if(true) {
                print("hello");
                int a = 10;
                a = a + 100;
                a = a || 100;
                }
            }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BooleanLiteral(true),Block([CallExpr(Id(print),[StringLiteral(hello)]),VarDecl(Id(a),IntType),IntLiteral(10),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(100))),BinaryOp(=,Id(a),BinaryOp(||,Id(a),IntLiteral(100)))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    def test_if_else_stmt_hard(self):
        input = """void main() {if(a && b || c) print("hello"); else put(5)}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(||,BinaryOp(&&,Id(a),Id(b)),Id(c)),CallExpr(Id(print),[StringLiteral(hello)]),CallExpr(Id(put),[IntLiteral(5)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test_if_else_stmt_mix(self):
        input = """void main() {
            if(a && b || c) {
                print("hello");
                int a[5];
                string b[10];
            }
            else {
                HPC(kafka);
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(||,BinaryOp(&&,Id(a),Id(b)),Id(c)),Block([CallExpr(Id(print),[StringLiteral(hello)]),VarDecl(Id(a),ArrayType(IntType,IntLiteral(5))),VarDecl(Id(b),ArrayType(StringType,IntLiteral(10)))]),Block([CallExpr(Id(HPC),[Id(kafka)])]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    
    # Test do while statement
    def test_do_while_base(self):
        input = """void main() {do print(); while(a==1);}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([CallExpr(Id(print),[])],BinaryOp(==,Id(a),IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test_do_while_medium(self):
        input = """void main() {do {int a[5]; print();} while(a==1&&2);}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([Block([VarDecl(Id(a),ArrayType(IntType,IntLiteral(5))),CallExpr(Id(print),[])])],BinaryOp(&&,BinaryOp(==,Id(a),IntLiteral(1)),IntLiteral(2)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    def test_do_while_hard(self):
        input = """void main() {do {if(true) print();} while(func(a[5]));}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([Block([If(BooleanLiteral(true),CallExpr(Id(print),[]))])],CallExpr(Id(func),[ArrayCell(Id(a),IntLiteral(5))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    
    # Test for statemet
    def test_for_base(self):
        input = """void main() {for(i=0;i<10;i=i+1) print();}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));CallExpr(Id(print),[]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    def test_for_medium(self):
        input = """void main() {for(i=0;i && 1;i=i+1) {print();}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(&&,Id(i),IntLiteral(1));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([CallExpr(Id(print),[])]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    def test_for_hard(self):
        input = """void main() {for(i = 1+a[6];a[i]>=(2/5);i = 10/i) print();}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(i),BinaryOp(+,IntLiteral(1),ArrayCell(Id(a),IntLiteral(6))));BinaryOp(>=,ArrayCell(Id(a),Id(i)),BinaryOp(/,IntLiteral(2),IntLiteral(5)));BinaryOp(=,Id(i),BinaryOp(/,IntLiteral(10),Id(i)));CallExpr(Id(print),[]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
        
    # Test break and continue
    def test_break(self):
        input = """void main() {for(i = 1+a[6];a[i]>=(2/5);i = 10/i) break;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(i),BinaryOp(+,IntLiteral(1),ArrayCell(Id(a),IntLiteral(6))));BinaryOp(>=,ArrayCell(Id(a),Id(i)),BinaryOp(/,IntLiteral(2),IntLiteral(5)));BinaryOp(=,Id(i),BinaryOp(/,IntLiteral(10),Id(i)));Break())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_continue(self):
        input = """void main() {for(i = 1+a[6];a[i]>=(2/5);i = 10/i) continue;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(i),BinaryOp(+,IntLiteral(1),ArrayCell(Id(a),IntLiteral(6))));BinaryOp(>=,ArrayCell(Id(a),Id(i)),BinaryOp(/,IntLiteral(2),IntLiteral(5)));BinaryOp(=,Id(i),BinaryOp(/,IntLiteral(10),Id(i)));Continue())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    
    def test_assign(self):
        input = """void main() {a = 5;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),IntLiteral(5))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    
    def test_or(self):
        input = """void main() {a = a || 0;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(||,Id(a),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_and(self):
        input = """void main() {a = a && 0;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(&&,Id(a),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_equal(self):
        input = """void main() {a = a == 0;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(==,Id(a),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_not_equal(self):
        input = """void main() {a = a != 0;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(!=,Id(a),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_less_than(self):
        input = """void main() {a = a < 0;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(<,Id(a),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_less_equal(self):
        input = """void main() {a = a <= 0;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(<=,Id(a),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_great_than(self):
        input = """void main() {a = a > 0;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(>,Id(a),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_great_equal(self):
        input = """void main() {a = a >= 0;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(>=,Id(a),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_add(self):
        input = """void main() {a = a + 0;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_subtract(self):
        input = """void main() {a = a - 0;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(-,Id(a),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_mul(self):
        input = """void main() {a = a * 0;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(*,Id(a),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_div(self):
        input = """void main() {a = a / 0;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(/,Id(a),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_mod(self):
        input = """void main() {a = a % 0;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(%,Id(a),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_not(self):
        input = """void main() {a = !a;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),UnaryOp(!,Id(a)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_sub(self):
        input = """void main() {a = -a;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),UnaryOp(-,Id(a)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    # Test array cell

    def test_array_cell_base(self):
        input = """void main() {a[5];}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([ArrayCell(Id(a),IntLiteral(5))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    
    def test_array_cell_medium(self):
        input = """void main() {a[5+x];}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([ArrayCell(Id(a),BinaryOp(+,IntLiteral(5),Id(x)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_array_cell_hard(self):
        input = """void main() {a[pow(2,3)];}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([ArrayCell(Id(a),CallExpr(Id(pow),[IntLiteral(2),IntLiteral(3)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_array_cell_expr_base(self):
        input = """void main() {(5+x)[a];}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([ArrayCell(BinaryOp(+,IntLiteral(5),Id(x)),Id(a))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_array_cell_expr_medium(self):
        input = """void main() {foo()[5];}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([ArrayCell(CallExpr(Id(foo),[]),IntLiteral(5))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_array_cell_expr_hard(self):
        input = """void main() {foo()[5][5][5];}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([ArrayCell(CallExpr(Id(foo),[]),IntLiteral(5)),IntLiteral(5),IntLiteral(5)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_array_cell_expr_super_hard(self):
        input = """void main() {foo(foo(foo(foo()[5])[5])[5])[5];}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([ArrayCell(CallExpr(Id(foo),[ArrayCell(CallExpr(Id(foo),[ArrayCell(CallExpr(Id(foo),[ArrayCell(CallExpr(Id(foo),[]),IntLiteral(5))]),IntLiteral(5))]),IntLiteral(5))]),IntLiteral(5))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_cal_func_base(self):
        input = """void main() {foo();}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([CallExpr(Id(foo),[])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
    
    def test_cal_func_single_variable(self):
        input = """void main() {foo(a);}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([CallExpr(Id(foo),[Id(a)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_cal_func_single_array(self):
        input = """void main() {foo(a[5]);}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([CallExpr(Id(foo),[ArrayCell(Id(a),IntLiteral(5))])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_cal_func_multi_variable(self):
        input = """void main() {foo(a, b, c);}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([CallExpr(Id(foo),[Id(a),Id(b),Id(c)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_cal_func_multi_array(self):
        input = """void main() {a[5], b[5]);}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([ArrayCell(Id(a),IntLiteral(5)),ArrayCell(Id(b),IntLiteral(5))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_cal_func_multi_variable_array(self):
        input = """void main() {foo(a, b[6], c);}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([CallExpr(Id(foo),[Id(a),ArrayCell(Id(b),IntLiteral(6)),Id(c)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
    
    # Test program with multi function declaration
    def test_multi_function_declaration(self):
        input = """void main() {} void main() {} void main() {}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([])),FuncDecl(Id(main),[],VoidType,Block([])),FuncDecl(Id(main),[],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    def test_multi_function_variable_declaration(self):
        input = """void main() {} int a; void main() {} float a[5];"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([])),VarDecl(Id(a),IntType),FuncDecl(Id(main),[],VoidType,Block([])),VarDecl(Id(a),ArrayType(FloatType,IntLiteral(5)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    # Test long program
    def test_long_program_1(self):
        input = r"""void main(){
            for (a=1;a<10;a=a*2){
                for(b=2;b==10;b=b*2){
                    int a;
                    string b;
                    b = a + 1;
                }
            }
            for(d=1;d!=1;d=d+1){
                int e;
                e = d;
            }
            for(c=100;c!=0;c=c%2){
                for(d=1000;d>0;d=d%10){
                    int e;
                    e = d;
                    string d;
                    d = e;
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(*,Id(a),IntLiteral(2)));Block([For(BinaryOp(=,Id(b),IntLiteral(2));BinaryOp(==,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(*,Id(b),IntLiteral(2)));Block([VarDecl(Id(a),IntType),VarDecl(Id(b),StringType),BinaryOp(=,Id(b),BinaryOp(+,Id(a),IntLiteral(1)))]))])),For(BinaryOp(=,Id(d),IntLiteral(1));BinaryOp(!=,Id(d),IntLiteral(1));BinaryOp(=,Id(d),BinaryOp(+,Id(d),IntLiteral(1)));Block([VarDecl(Id(e),IntType),BinaryOp(=,Id(e),Id(d))])),For(BinaryOp(=,Id(c),IntLiteral(100));BinaryOp(!=,Id(c),IntLiteral(0));BinaryOp(=,Id(c),BinaryOp(%,Id(c),IntLiteral(2)));Block([For(BinaryOp(=,Id(d),IntLiteral(1000));BinaryOp(>,Id(d),IntLiteral(0));BinaryOp(=,Id(d),BinaryOp(%,Id(d),IntLiteral(10)));Block([VarDecl(Id(e),IntType),BinaryOp(=,Id(e),Id(d)),VarDecl(Id(d),StringType),BinaryOp(=,Id(d),Id(e))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_long_program_2(self):
        input = r"""void main(){
            for (a=1;a<10;a=a*2){
                for(b=2;b==10;b=b*2){
                    for(c=100;c!=0;c=c%2){
                        for(d=1000;d>0;d=d%10){
                            int e;
                            e = d;
                            string d;
                            d = e;
                        }
                    }
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(*,Id(a),IntLiteral(2)));Block([For(BinaryOp(=,Id(b),IntLiteral(2));BinaryOp(==,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(*,Id(b),IntLiteral(2)));Block([For(BinaryOp(=,Id(c),IntLiteral(100));BinaryOp(!=,Id(c),IntLiteral(0));BinaryOp(=,Id(c),BinaryOp(%,Id(c),IntLiteral(2)));Block([For(BinaryOp(=,Id(d),IntLiteral(1000));BinaryOp(>,Id(d),IntLiteral(0));BinaryOp(=,Id(d),BinaryOp(%,Id(d),IntLiteral(10)));Block([VarDecl(Id(e),IntType),BinaryOp(=,Id(e),Id(d)),VarDecl(Id(d),StringType),BinaryOp(=,Id(d),Id(e))]))]))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,366))
    
    def test_long_program_3(self):
        input = r"""void main(){
            int a,b,c;
            for (a=1;a<100;a=a+1){
                for(b=1;b<10;b=b+1){
                    for(c=1;c<50;c=c+1){
                        if (c){
                            string rlt;
                            rlt = c;
                        }
                    }
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(100));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([For(BinaryOp(=,Id(b),IntLiteral(1));BinaryOp(<,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));Block([For(BinaryOp(=,Id(c),IntLiteral(1));BinaryOp(<,Id(c),IntLiteral(50));BinaryOp(=,Id(c),BinaryOp(+,Id(c),IntLiteral(1)));Block([If(Id(c),Block([VarDecl(Id(rlt),StringType),BinaryOp(=,Id(rlt),Id(c))]))]))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_long_program_4(self):
        input = r"""void main(){
            int a;
            float b;
            string c;
            for (a=1; a % 10 == 0; a=a+1){
                if (a % 2 == 0){
                    for (b=0; b != 1;b=b+2){
                        int a;
                        float b;
                        b = a;
                        for (b=1;b==10;b=b+1){
                            string c;
                            c = b;
                            if (c){
                                float a;
                                string d;
                                d = c;
                            }
                        }
                    }
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType),VarDecl(Id(c),StringType),For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(10)),IntLiteral(0));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(2)),IntLiteral(0)),Block([For(BinaryOp(=,Id(b),IntLiteral(0));BinaryOp(!=,Id(b),IntLiteral(1));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(2)));Block([VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType),BinaryOp(=,Id(b),Id(a)),For(BinaryOp(=,Id(b),IntLiteral(1));BinaryOp(==,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));Block([VarDecl(Id(c),StringType),BinaryOp(=,Id(c),Id(b)),If(Id(c),Block([VarDecl(Id(a),FloatType),VarDecl(Id(d),StringType),BinaryOp(=,Id(d),Id(c))]))]))]))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_long_program_5(self):
        input = r"""void main(){
            int a;
            float b;
            string c;
            for (a=1; a % 10 == 0; a=a+1){
                if (a % 2 == 0){
                    for (b=0; b != 1;b=b+2){
                        int a;
                        float b;
                        b = a;
                    }
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType),VarDecl(Id(c),StringType),For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(10)),IntLiteral(0));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(2)),IntLiteral(0)),Block([For(BinaryOp(=,Id(b),IntLiteral(0));BinaryOp(!=,Id(b),IntLiteral(1));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(2)));Block([VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType),BinaryOp(=,Id(b),Id(a))]))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_long_program_6(self):
        input = r"""void main(){
            for (a=1;a<10;a=a+1){
                for(b=2;b%10==0;b=b+1){
                    int c;
                    float d;
                    c = b;
                    d = a;
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([For(BinaryOp(=,Id(b),IntLiteral(2));BinaryOp(==,BinaryOp(%,Id(b),IntLiteral(10)),IntLiteral(0));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));Block([VarDecl(Id(c),IntType),VarDecl(Id(d),FloatType),BinaryOp(=,Id(c),Id(b)),BinaryOp(=,Id(d),Id(a))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_long_program_7(self):
        input = r"""void main(){
            int a;
            int b;
            boolean c;
            for (a=1; a < 10; a=a+1){
                for (b=0; b != 10; b=b+1){
                    c = b;
                }
                b = a + 1;
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),BoolType),For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([For(BinaryOp(=,Id(b),IntLiteral(0));BinaryOp(!=,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));Block([BinaryOp(=,Id(c),Id(b))])),BinaryOp(=,Id(b),BinaryOp(+,Id(a),IntLiteral(1)))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_long_program_8(self):
        input = r"""void main(){
            int a;
            int b;
            boolean c;
            for (a=1; a < 10; a=a+1){
                if (a % 2 == 0){
                    c = false;
                    b = b + 1;
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),BoolType),For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(2)),IntLiteral(0)),Block([BinaryOp(=,Id(c),BooleanLiteral(false)),BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_long_program_9(self):
        input = r"""void main(){
            int a;
            a = true;
            if (true){
                if (a == true){
                    if (!a){
                        a = false;
                        string b;
                        b = a;
                        if (b){
                            boolean c;
                            c = b;
                            if (!c){
                                int d;
                                d = c;
                                if (d == c || !c){
                                    string e;
                                    e = d;
                                }
                                else{
                                    string e;
                                    e = d;
                                }
                            }
                            else{
                                int d;
                                d = e;
                                boolean t;
                                t = e;
                                if (d && !e){
                                    string t;
                                    t = d;
                                }
                            }
                        }
                    }
                    else{
                        if ((a == b || c != b) && a > b){
                            int e;
                            e = a;
                        }
                    }
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(Id(a),IntType),BinaryOp(=,Id(a),BooleanLiteral(true)),If(BooleanLiteral(true),Block([If(BinaryOp(==,Id(a),BooleanLiteral(true)),Block([If(UnaryOp(!,Id(a)),Block([BinaryOp(=,Id(a),BooleanLiteral(false)),VarDecl(Id(b),StringType),BinaryOp(=,Id(b),Id(a)),If(Id(b),Block([VarDecl(Id(c),BoolType),BinaryOp(=,Id(c),Id(b)),If(UnaryOp(!,Id(c)),Block([VarDecl(Id(d),IntType),BinaryOp(=,Id(d),Id(c)),If(BinaryOp(||,BinaryOp(==,Id(d),Id(c)),UnaryOp(!,Id(c))),Block([VarDecl(Id(e),StringType),BinaryOp(=,Id(e),Id(d))]),Block([VarDecl(Id(e),StringType),BinaryOp(=,Id(e),Id(d))]))]),Block([VarDecl(Id(d),IntType),BinaryOp(=,Id(d),Id(e)),VarDecl(Id(t),BoolType),BinaryOp(=,Id(t),Id(e)),If(BinaryOp(&&,Id(d),UnaryOp(!,Id(e))),Block([VarDecl(Id(t),StringType),BinaryOp(=,Id(t),Id(d))]))]))]))]),Block([If(BinaryOp(&&,BinaryOp(||,BinaryOp(==,Id(a),Id(b)),BinaryOp(!=,Id(c),Id(b))),BinaryOp(>,Id(a),Id(b))),Block([VarDecl(Id(e),IntType),BinaryOp(=,Id(e),Id(a))]))]))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_long_program_10(self):
        input = r"""void main(){
            int a;
            a = true;
            if (true){
                if (a == true){
                    if (!a){
                        a = false;
                        string b;
                        b = a;
                    }
                    else{
                        string b;
                        b = a;
                    }
                }
                else{
                    a = false;
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(Id(a),IntType),BinaryOp(=,Id(a),BooleanLiteral(true)),If(BooleanLiteral(true),Block([If(BinaryOp(==,Id(a),BooleanLiteral(true)),Block([If(UnaryOp(!,Id(a)),Block([BinaryOp(=,Id(a),BooleanLiteral(false)),VarDecl(Id(b),StringType),BinaryOp(=,Id(b),Id(a))]),Block([VarDecl(Id(b),StringType),BinaryOp(=,Id(b),Id(a))]))]),Block([BinaryOp(=,Id(a),BooleanLiteral(false))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,374))


    # def test_hard_program_1(self):
    #     input = """int a[5];"""
    #     expect = "Program([VarDecl(Id(a),ArrayType(IntType,IntLiteral(5)))])"
    #     self.assertTrue(TestAST.checkASTGen(input,expect,375))

    # def test_hard_program_2(self):
    #     input = """int a[5];"""
    #     expect = "Program([VarDecl(Id(a),ArrayType(IntType,IntLiteral(5)))])"
    #     self.assertTrue(TestAST.checkASTGen(input,expect,376))

    # def test_hard_program_3(self):
    #     input = """int a[5];"""
    #     expect = "Program([VarDecl(Id(a),ArrayType(IntType,IntLiteral(5)))])"
    #     self.assertTrue(TestAST.checkASTGen(input,expect,377))

    # def test_hard_program_4(self):
    #     input = """int a[5];"""
    #     expect = "Program([VarDecl(Id(a),ArrayType(IntType,IntLiteral(5)))])"
    #     self.assertTrue(TestAST.checkASTGen(input,expect,378))

    # def test_hard_program_5(self):
    #     input = """int a[5];"""
    #     expect = "Program([VarDecl(Id(a),ArrayType(IntType,IntLiteral(5)))])"
    #     self.assertTrue(TestAST.checkASTGen(input,expect,379))

    # def test_hard_program_6(self):
    #     input = """int a[5];"""
    #     expect = "Program([VarDecl(Id(a),ArrayType(IntType,IntLiteral(5)))])"
    #     self.assertTrue(TestAST.checkASTGen(input,expect,380))

    # def test_hard_program_7(self):
    #     input = """int a[5];"""
    #     expect = "Program([VarDecl(Id(a),ArrayType(IntType,IntLiteral(5)))])"
    #     self.assertTrue(TestAST.checkASTGen(input,expect,381))

    # def test_hard_program_8(self):
    #     input = """int a[5];"""
    #     expect = "Program([VarDecl(Id(a),ArrayType(IntType,IntLiteral(5)))])"
    #     self.assertTrue(TestAST.checkASTGen(input,expect,382))

    # def test_hard_program_9(self):
    #     input = """int a[5];"""
    #     expect = "Program([VarDecl(Id(a),ArrayType(IntType,IntLiteral(5)))])"
    #     self.assertTrue(TestAST.checkASTGen(input,expect,383))

    # def test_hard_program_10(self):
    #     input = """int a[5];"""
    #     expect = "Program([VarDecl(Id(a),ArrayType(IntType,IntLiteral(5)))])"
    #     self.assertTrue(TestAST.checkASTGen(input,expect,384))
    