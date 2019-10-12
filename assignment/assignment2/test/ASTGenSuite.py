import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # Test variable declaration
    def test_single_variable_declaration(self):
        input = """int a;"""
        expect = "Program([VarDecl(a,IntType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,300))
    def test_single_array_declaration_float(self):
        input = """float a[5];"""
        expect = "Program([VarDecl(a,ArrayType(FloatType,5))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    def test_single_array_declaration_int(self):
        input = """int a[5];"""
        expect = "Program([VarDecl(a,ArrayType(IntType,5))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_multi_variable_declaration(self):
        input = """boolean a,b;"""
        expect = "Program([VarDecl(a,BoolType),VarDecl(b,BoolType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    def test_multi_array_declaration(self):
        input = """boolean a[10],b[5];"""
        expect = "Program([VarDecl(a,ArrayType(BoolType,10)),VarDecl(b,ArrayType(BoolType,5))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    def test_mix_variable_declaration(self):
        input = """boolean a,b[5];"""
        expect = "Program([VarDecl(a,BoolType),VarDecl(b,ArrayType(BoolType,5))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    # Test program with variable declaration
    def test_program_multi_variable_declaration(self):
        input = """int a; float b; boolean c;"""
        expect = "Program([VarDecl(a,IntType),VarDecl(b,FloatType),VarDecl(c,BoolType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    def test_program_multi_array_declaration(self):
        input = """int a[5]; float b[6]; boolean c[7];"""
        expect = "Program([VarDecl(a,ArrayType(IntType,5)),VarDecl(b,ArrayType(FloatType,6)),VarDecl(c,ArrayType(BoolType,7))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    def test_program_multi_variable_array_declaration(self):
        input = """int a; float b; string a[10]; boolean d[5];"""
        expect = "Program([VarDecl(a,IntType),VarDecl(b,FloatType),VarDecl(a,ArrayType(StringType,10)),VarDecl(d,ArrayType(BoolType,5))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test_program_multi_variable_array_declaration_hard(self):
        input = """int a,x; float b,z; string a[10], l[6], r; boolean d[5];"""
        expect = "Program([VarDecl(a,IntType),VarDecl(x,IntType),VarDecl(b,FloatType),VarDecl(z,FloatType),VarDecl(a,ArrayType(StringType,10)),VarDecl(l,ArrayType(StringType,6)),VarDecl(r,StringType),VarDecl(d,ArrayType(BoolType,5))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    def test_expr_recursion(self):
        input = """void main() {(((1)));}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([IntLiteral(1)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    # Test function parameter
    def test_function_para_empty(self):
        input = """int main() {}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    def test_function_single_para(self):
        input = """int main(int a) {}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,IntType)],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    def test_function_multi_para(self):
        input = """void main(boolean a, float b) {}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,BoolType),VarDecl(b,FloatType)],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    def test_function_single_array(self):
        input = """void main(boolean a[]) {}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(BoolType))],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    def test_function_multi_array(self):
        input = """void main(boolean a[], float b[]) {}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(BoolType)),VarDecl(b,ArrayTypePointer(FloatType))],VoidType,Block([]))])"
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
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([])),FuncDecl(Id(pow),[],ArrayTypePointer(FloatType),Block([])),VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    def test_program_multi_function_array(self):
        input = """int[] main() {} float[] pow() {} int a[5],b[5],c[5];"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([])),FuncDecl(Id(pow),[],ArrayTypePointer(FloatType),Block([])),VarDecl(a,ArrayType(IntType,5)),VarDecl(b,ArrayType(IntType,5)),VarDecl(c,ArrayType(IntType,5))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    # Test if statement
    def test_if_stmt_base(self):
        input = """void main() {if(true) print("hello");}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BooleanLiteral(true),CallExpr(Id(print),[StringLiteral(hello)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    def test_if__else_stmt_base(self):
        input = """void main() {if(true) print("hello"); else put(5);}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BooleanLiteral(true),CallExpr(Id(print),[StringLiteral(hello)]),CallExpr(Id(put),[IntLiteral(5)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    def test_if_stmt_hard(self):
        input = """void main() {if(true) {
                print("hello");
                int a;
                a = a + 100;
                a = a || 100;
                }
            }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BooleanLiteral(true),Block([CallExpr(Id(print),[StringLiteral(hello)]),VarDecl(a,IntType),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(100))),BinaryOp(=,Id(a),BinaryOp(||,Id(a),IntLiteral(100)))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    def test_if_else_stmt_hard(self):
        input = """void main() {if(a && b || c) print("hello"); else put(5);}"""
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
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(||,BinaryOp(&&,Id(a),Id(b)),Id(c)),Block([CallExpr(Id(print),[StringLiteral(hello)]),VarDecl(a,ArrayType(IntType,5)),VarDecl(b,ArrayType(StringType,10))]),Block([CallExpr(Id(HPC),[Id(kafka)])]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    
    # Test do while statement
    def test_do_while_base(self):
        input = """void main() {do print(); while(a==1);}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([CallExpr(Id(print),[])],BinaryOp(==,Id(a),IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test_do_while_medium(self):
        input = """void main() {do {int a[5]; print();} while(a==1&&2);}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([Block([VarDecl(a,ArrayType(IntType,5)),CallExpr(Id(print),[])])],BinaryOp(&&,BinaryOp(==,Id(a),IntLiteral(1)),IntLiteral(2)))]))])"
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
        input = """void main() {for(i=0;i && 1;i=i+1) {print();}}"""
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

    # TODO : Find bug !
    def test_array_cell_expr_hard(self):
        input = """void main() {(foo()[5])[5];}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([ArrayCell(ArrayCell(CallExpr(Id(foo),[]),IntLiteral(5)),IntLiteral(5))]))])"
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
        input = """void main() {a[5]; b[5];}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([ArrayCell(Id(a),IntLiteral(5)),ArrayCell(Id(b),IntLiteral(5))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_cal_func_multi_variable_array(self):
        input = """void main() {foo(a, b[6], c);}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([CallExpr(Id(foo),[Id(a),ArrayCell(Id(b),IntLiteral(6)),Id(c)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
    
    # # Test program with multi function declaration
    def test_multi_function_declaration(self):
        input = """void main() {} void main() {} void main() {}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([])),FuncDecl(Id(main),[],VoidType,Block([])),FuncDecl(Id(main),[],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    def test_multi_function_variable_declaration(self):
        input = """void main() {} int a; void main() {} float a[5];"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([])),VarDecl(a,IntType),FuncDecl(Id(main),[],VoidType,Block([])),VarDecl(a,ArrayType(FloatType,5))])"
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
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(*,Id(a),IntLiteral(2)));Block([For(BinaryOp(=,Id(b),IntLiteral(2));BinaryOp(==,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(*,Id(b),IntLiteral(2)));Block([VarDecl(a,IntType),VarDecl(b,StringType),BinaryOp(=,Id(b),BinaryOp(+,Id(a),IntLiteral(1)))]))])),For(BinaryOp(=,Id(d),IntLiteral(1));BinaryOp(!=,Id(d),IntLiteral(1));BinaryOp(=,Id(d),BinaryOp(+,Id(d),IntLiteral(1)));Block([VarDecl(e,IntType),BinaryOp(=,Id(e),Id(d))])),For(BinaryOp(=,Id(c),IntLiteral(100));BinaryOp(!=,Id(c),IntLiteral(0));BinaryOp(=,Id(c),BinaryOp(%,Id(c),IntLiteral(2)));Block([For(BinaryOp(=,Id(d),IntLiteral(1000));BinaryOp(>,Id(d),IntLiteral(0));BinaryOp(=,Id(d),BinaryOp(%,Id(d),IntLiteral(10)));Block([VarDecl(e,IntType),BinaryOp(=,Id(e),Id(d)),VarDecl(d,StringType),BinaryOp(=,Id(d),Id(e))]))]))]))])"
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
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(*,Id(a),IntLiteral(2)));Block([For(BinaryOp(=,Id(b),IntLiteral(2));BinaryOp(==,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(*,Id(b),IntLiteral(2)));Block([For(BinaryOp(=,Id(c),IntLiteral(100));BinaryOp(!=,Id(c),IntLiteral(0));BinaryOp(=,Id(c),BinaryOp(%,Id(c),IntLiteral(2)));Block([For(BinaryOp(=,Id(d),IntLiteral(1000));BinaryOp(>,Id(d),IntLiteral(0));BinaryOp(=,Id(d),BinaryOp(%,Id(d),IntLiteral(10)));Block([VarDecl(e,IntType),BinaryOp(=,Id(e),Id(d)),VarDecl(d,StringType),BinaryOp(=,Id(d),Id(e))]))]))]))]))]))])"
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
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType),For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(100));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([For(BinaryOp(=,Id(b),IntLiteral(1));BinaryOp(<,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));Block([For(BinaryOp(=,Id(c),IntLiteral(1));BinaryOp(<,Id(c),IntLiteral(50));BinaryOp(=,Id(c),BinaryOp(+,Id(c),IntLiteral(1)));Block([If(Id(c),Block([VarDecl(rlt,StringType),BinaryOp(=,Id(rlt),Id(c))]))]))]))]))]))])"
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
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),VarDecl(b,FloatType),VarDecl(c,StringType),For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(10)),IntLiteral(0));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(2)),IntLiteral(0)),Block([For(BinaryOp(=,Id(b),IntLiteral(0));BinaryOp(!=,Id(b),IntLiteral(1));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(2)));Block([VarDecl(a,IntType),VarDecl(b,FloatType),BinaryOp(=,Id(b),Id(a)),For(BinaryOp(=,Id(b),IntLiteral(1));BinaryOp(==,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));Block([VarDecl(c,StringType),BinaryOp(=,Id(c),Id(b)),If(Id(c),Block([VarDecl(a,FloatType),VarDecl(d,StringType),BinaryOp(=,Id(d),Id(c))]))]))]))]))]))]))])"
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
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),VarDecl(b,FloatType),VarDecl(c,StringType),For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(10)),IntLiteral(0));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(2)),IntLiteral(0)),Block([For(BinaryOp(=,Id(b),IntLiteral(0));BinaryOp(!=,Id(b),IntLiteral(1));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(2)));Block([VarDecl(a,IntType),VarDecl(b,FloatType),BinaryOp(=,Id(b),Id(a))]))]))]))]))])"
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
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([For(BinaryOp(=,Id(b),IntLiteral(2));BinaryOp(==,BinaryOp(%,Id(b),IntLiteral(10)),IntLiteral(0));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));Block([VarDecl(c,IntType),VarDecl(d,FloatType),BinaryOp(=,Id(c),Id(b)),BinaryOp(=,Id(d),Id(a))]))]))]))])"
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
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,BoolType),For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([For(BinaryOp(=,Id(b),IntLiteral(0));BinaryOp(!=,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));Block([BinaryOp(=,Id(c),Id(b))])),BinaryOp(=,Id(b),BinaryOp(+,Id(a),IntLiteral(1)))]))]))])"
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
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,BoolType),For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(2)),IntLiteral(0)),Block([BinaryOp(=,Id(c),BooleanLiteral(false)),BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)))]))]))]))])"
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
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),BooleanLiteral(true)),If(BooleanLiteral(true),Block([If(BinaryOp(==,Id(a),BooleanLiteral(true)),Block([If(UnaryOp(!,Id(a)),Block([BinaryOp(=,Id(a),BooleanLiteral(false)),VarDecl(b,StringType),BinaryOp(=,Id(b),Id(a)),If(Id(b),Block([VarDecl(c,BoolType),BinaryOp(=,Id(c),Id(b)),If(UnaryOp(!,Id(c)),Block([VarDecl(d,IntType),BinaryOp(=,Id(d),Id(c)),If(BinaryOp(||,BinaryOp(==,Id(d),Id(c)),UnaryOp(!,Id(c))),Block([VarDecl(e,StringType),BinaryOp(=,Id(e),Id(d))]),Block([VarDecl(e,StringType),BinaryOp(=,Id(e),Id(d))]))]),Block([VarDecl(d,IntType),BinaryOp(=,Id(d),Id(e)),VarDecl(t,BoolType),BinaryOp(=,Id(t),Id(e)),If(BinaryOp(&&,Id(d),UnaryOp(!,Id(e))),Block([VarDecl(t,StringType),BinaryOp(=,Id(t),Id(d))]))]))]))]),Block([If(BinaryOp(&&,BinaryOp(||,BinaryOp(==,Id(a),Id(b)),BinaryOp(!=,Id(c),Id(b))),BinaryOp(>,Id(a),Id(b))),Block([VarDecl(e,IntType),BinaryOp(=,Id(e),Id(a))]))]))]))]))]))])"
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
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),BooleanLiteral(true)),If(BooleanLiteral(true),Block([If(BinaryOp(==,Id(a),BooleanLiteral(true)),Block([If(UnaryOp(!,Id(a)),Block([BinaryOp(=,Id(a),BooleanLiteral(false)),VarDecl(b,StringType),BinaryOp(=,Id(b),Id(a))]),Block([VarDecl(b,StringType),BinaryOp(=,Id(b),Id(a))]))]),Block([BinaryOp(=,Id(a),BooleanLiteral(false))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,374))


    def test_more_simple_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(putIntLn),[IntLiteral(4)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,375))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """int main () {
            getIntLn();
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(getIntLn),[])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,376))
    def test_true_and_false(self):
           
        input = """void f(int a,float b, float c){
            true && false || (2 > 3/5);
        }"""
        expect = "Program([FuncDecl(Id(f),[VarDecl(a,IntType),VarDecl(b,FloatType),VarDecl(c,FloatType)],VoidType,Block([BinaryOp(||,BinaryOp(&&,BooleanLiteral(true),BooleanLiteral(false)),BinaryOp(>,IntLiteral(2),BinaryOp(/,IntLiteral(3),IntLiteral(5))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
    def test_more_call_function(self):
        input = """int main () {
            putIntLn(4);
            ar[12];
            foo(a[10],r);
            break;continue;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(putIntLn),[IntLiteral(4)]),ArrayCell(Id(ar),IntLiteral(12)),CallExpr(Id(foo),[ArrayCell(Id(a),IntLiteral(10)),Id(r)]),Break(),Continue()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
    def test_if_and_have_not_semiconlon(self):
        input = """int main () {
            if( (c > x) < d){
                int a,b;
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(<,BinaryOp(>,Id(c),Id(x)),Id(d)),Block([VarDecl(a,IntType),VarDecl(b,IntType)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,379))
    def test_if_in_if(self):
        input = """int foo () {
            if (a+1) {{{{if(b+a) foo();}}}} else {if (c+d) t+a; else func(a(b(c)))[f+6*d()];}
        }"""
        expect = "Program([FuncDecl(Id(foo),[],IntType,Block([If(BinaryOp(+,Id(a),IntLiteral(1)),Block([Block([Block([Block([If(BinaryOp(+,Id(b),Id(a)),CallExpr(Id(foo),[]))])])])]),Block([If(BinaryOp(+,Id(c),Id(d)),BinaryOp(+,Id(t),Id(a)),ArrayCell(CallExpr(Id(func),[CallExpr(Id(a),[CallExpr(Id(b),[Id(c)])])]),BinaryOp(+,Id(f),BinaryOp(*,IntLiteral(6),CallExpr(Id(d),[])))))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,380))
    def test_array_type_and_invol(self):
        input = """int[] ham(int a[], float b[]) {
            return;
        }"""
        expect = "Program([FuncDecl(Id(ham),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(b,ArrayTypePointer(FloatType))],ArrayTypePointer(IntType),Block([Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,381))
    def test_do_while(self):
        input = """void fo() {
            do{ f(foo(fr(aaa(e(r()))))); } while a>d;
        }"""
        expect = "Program([FuncDecl(Id(fo),[],VoidType,Block([Dowhile([Block([CallExpr(Id(f),[CallExpr(Id(foo),[CallExpr(Id(fr),[CallExpr(Id(aaa),[CallExpr(Id(e),[CallExpr(Id(r),[])])])])])])])],BinaryOp(>,Id(a),Id(d)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,382))
    def test_bool_in_do(self):
        input = """int main () {
           do{ true;} while d>a;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([BooleanLiteral(true)])],BinaryOp(>,Id(d),Id(a)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,383))
    def test_if_in_do_while(self):
        input = """float d () {
           do if (a==s) {if (t>a) if (d>=e) if (a<y) if (r<=o) {x+1;}} while foo();
        }"""
        expect = "Program([FuncDecl(Id(d),[],FloatType,Block([Dowhile([If(BinaryOp(==,Id(a),Id(s)),Block([If(BinaryOp(>,Id(t),Id(a)),If(BinaryOp(>=,Id(d),Id(e)),If(BinaryOp(<,Id(a),Id(y)),If(BinaryOp(<=,Id(r),Id(o)),Block([BinaryOp(+,Id(x),IntLiteral(1))])))))]))],CallExpr(Id(foo),[]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_func_decl_for_if(self):
        input = """int foo(int a){
            for(i = 0;i!= 100; i=i+1){
                if(i%2==0) i=i*2;
                else i = i -1;
            }
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType)],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(!=,Id(i),IntLiteral(100));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(i),IntLiteral(2)),IntLiteral(0)),BinaryOp(=,Id(i),BinaryOp(*,Id(i),IntLiteral(2))),BinaryOp(=,Id(i),BinaryOp(-,Id(i),IntLiteral(1))))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_func_decl_if_var(self):
        input = """int main() {
            if(true) a=10;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([If(BooleanLiteral(true),BinaryOp(=,Id(a),IntLiteral(10)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_var_many_decl(self):
        input = """int a; float b,c,d[3]; boolean e; string s; """
        expect = "Program([VarDecl(a,IntType),VarDecl(b,FloatType),VarDecl(c,FloatType),VarDecl(d,ArrayType(FloatType,3)),VarDecl(e,BoolType),VarDecl(s,StringType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_func_println(self):
        input = """void b(int a[],int b){
                          int a;a=1;println(a);
                          {
                            int b;b=1;
                            println(b);
                          }
                }"""
        expect = "Program([FuncDecl(Id(b),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(b,IntType)],VoidType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),IntLiteral(1)),CallExpr(Id(println),[Id(a)]),Block([VarDecl(b,IntType),BinaryOp(=,Id(b),IntLiteral(1)),CallExpr(Id(println),[Id(b)])])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_func_empty(self):
        input = """void Calculate(){}"""
        expect = "Program([FuncDecl(Id(Calculate),[],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_func_decl_foo(self):
        input = """void foo(){
                boolean b ;
                b = true;
                if( !b == false) 
                    println(" b is true");
            }"""
        expect = "Program([FuncDecl(Id(foo),[],VoidType,Block([VarDecl(b,BoolType),BinaryOp(=,Id(b),BooleanLiteral(true)),If(BinaryOp(==,UnaryOp(!,Id(b)),BooleanLiteral(false)),CallExpr(Id(println),[StringLiteral( b is true)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_func_many_func(self):
        input = """
        void main(){
            int oddSum, evenSum,arr[10],i;
            oddSum = evenSum =0;
            for(i=0;i<10;i=i+1)
                arr[i]=i;
            for(i=0;i<10;i=i+1){
                if(arr[i]%2==0)
                    evenSum = evenSum + arr[i];
                else
                    oddSum = oddSum + arr[i];
            }        
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(oddSum,IntType),VarDecl(evenSum,IntType),VarDecl(arr,ArrayType(IntType,10)),VarDecl(i,IntType),BinaryOp(=,Id(oddSum),BinaryOp(=,Id(evenSum),IntLiteral(0))),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));BinaryOp(=,ArrayCell(Id(arr),Id(i)),Id(i))),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,ArrayCell(Id(arr),Id(i)),IntLiteral(2)),IntLiteral(0)),BinaryOp(=,Id(evenSum),BinaryOp(+,Id(evenSum),ArrayCell(Id(arr),Id(i)))),BinaryOp(=,Id(oddSum),BinaryOp(+,Id(oddSum),ArrayCell(Id(arr),Id(i)))))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_func_switch_case(self):
        input = """
                void main(){
                    int mark;
                }
                void result(int mark){
                  if(mark<5)
                    println("Trung binh");
                  else if (5<=mark&&mark<8)
                    println("Kha");
                  else
                    println("Gioi");
                }        
        """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(mark,IntType)])),FuncDecl(Id(result),[VarDecl(mark,IntType)],VoidType,Block([If(BinaryOp(<,Id(mark),IntLiteral(5)),CallExpr(Id(println),[StringLiteral(Trung binh)]),If(BinaryOp(&&,BinaryOp(<=,IntLiteral(5),Id(mark)),BinaryOp(<,Id(mark),IntLiteral(8))),CallExpr(Id(println),[StringLiteral(Kha)]),CallExpr(Id(println),[StringLiteral(Gioi)])))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_func_break_continue(self):
        input = """
                void main(){
                    int i;
                    for(i=0;i<10;i=i+1)
                    {
                      println(i);
                      if(i == 5)
                        continue;
                      if(i==9)
                        break;
                    }
                }        
        """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(i,IntType),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([CallExpr(Id(println),[Id(i)]),If(BinaryOp(==,Id(i),IntLiteral(5)),Continue()),If(BinaryOp(==,Id(i),IntLiteral(9)),Break())]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_func_do_while(self):
        input = """
                void main(){
                    int i;
                    i = 0;
                    do 
                      println(i);
                      i=i+1;
                      if(i==9)
                        break;
                    while(i<10);
                }         
        """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(i,IntType),BinaryOp(=,Id(i),IntLiteral(0)),Dowhile([CallExpr(Id(println),[Id(i)]),BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1))),If(BinaryOp(==,Id(i),IntLiteral(9)),Break())],BinaryOp(<,Id(i),IntLiteral(10)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_maximum_recursion(self):
        input = """
        void main() {n = ((((((((((((((((((((((((((((((((((((((((((((((((((((((((((n))))))))))))))))))))))))))))))))))))))))))))))))/2))))))))));}
                """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(n),BinaryOp(/,Id(n),IntLiteral(2)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_easy_recursion(self):
        input = """
        void main() {n = ((((((n))/2))));}
                """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(n),BinaryOp(/,Id(n),IntLiteral(2)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_func_recursion(self):
        input = """
        void main() {print();{print();}{print();}{print();}{print();}{print();}{print();}{print();}{print();}{print();}}
                """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([CallExpr(Id(print),[]),Block([CallExpr(Id(print),[])]),Block([CallExpr(Id(print),[])]),Block([CallExpr(Id(print),[])]),Block([CallExpr(Id(print),[])]),Block([CallExpr(Id(print),[])]),Block([CallExpr(Id(print),[])]),Block([CallExpr(Id(print),[])]),Block([CallExpr(Id(print),[])]),Block([CallExpr(Id(print),[])])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_for_recursion(self):
        input = """
        void main() {for(1;1;1) for(1;1;1) for(1;1;1) for(1;1;1) for(1;1;1) for(1;1;1) for(1;1;1) for(1;1;1) print();}
                """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(IntLiteral(1);IntLiteral(1);IntLiteral(1);For(IntLiteral(1);IntLiteral(1);IntLiteral(1);For(IntLiteral(1);IntLiteral(1);IntLiteral(1);For(IntLiteral(1);IntLiteral(1);IntLiteral(1);For(IntLiteral(1);IntLiteral(1);IntLiteral(1);For(IntLiteral(1);IntLiteral(1);IntLiteral(1);For(IntLiteral(1);IntLiteral(1);IntLiteral(1);For(IntLiteral(1);IntLiteral(1);IntLiteral(1);CallExpr(Id(print),[])))))))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_do_while_recursion(self):
        input = """
        void main() {do do do do do do print(); while true; while true; while true; while true; while true; while true;}
                """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([Dowhile([Dowhile([Dowhile([Dowhile([Dowhile([CallExpr(Id(print),[])],BooleanLiteral(true))],BooleanLiteral(true))],BooleanLiteral(true))],BooleanLiteral(true))],BooleanLiteral(true))],BooleanLiteral(true))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,399))