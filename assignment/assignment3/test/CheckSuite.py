import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_no_entry_point1(self):
        """ No Entry Point """
        input = """
        int main1(){}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_no_entry_point2(self):
        """ No Entry Point """
        input = """
        int main1(){}
        int main2(){}
        int main3(){}
        int main4(){}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclare_global_var1(self):
        """ Global Variable Redeclared """
        input = """
        int a;
        boolean a;
        void main(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def test_redeclare_global_var2(self):
        """ Global Variable Redeclared """
        input = """
        int a;
        boolean b;
        string c;
        float d;
        float a;
        void main(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclare_func1(self):
        """ Function Redeclared """
        input = """
        int main(){return 1;}
        void main(){}
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclare_func2(self):
        """ Function Redeclared """
        input = """
        void main1(){}
        void main2(){}
        int main3(){return 1;}
        int main(){return 0;}
        boolean main1(){return true;}
        """
        expect = "Redeclared Function: main1"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclare_param1(self):
        """ Parameter Redeclared """
        input = """
        void main(int a, boolean a){}
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclare_param2(self):
        """ Parameter Redeclared """
        input = """
        void main(int a, boolean b){}
        int main2(int a, string b, float a){
            return a;
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_id_undeclared1(self):
        input = """void main(){
            a = a + 1;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_id_undeclared2(self):
        """ Undeclared Identifier """
        input = """
        int a;
        void main(){
            a = a + 1;
            a = a - b;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_id_undeclared3(self):
        """ Undeclared Identifier """
        input = """
        void main(){
            float a;
            int b;
            a = a + 1;
            a = a - b;
            a = a / c;
        }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_func_undeclared1(self):
        """ Undeclared Function """
        input = """
        void main(){
            print("Hello");
        }
        """
        expect = "Undeclared Function: print"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_func_undeclared2(self):
        """ Undeclared Function """
        input = """
        void main(){
            int num;
            putInt(num);
            print(getInt());
        }
        """
        expect = "Undeclared Function: print"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_func_undeclared3(self):
        """ Undeclared Function """
        input = """
        int main(){
            int a;
            int b;
            a = sum(a, b);
            a = sub(a, b);
            return a;
        }
        int sum(int a, int b){
            return a + b;
        }
        """
        expect = "Undeclared Function: sub"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_mismatch_condition_ifstmt1(self):
        """ Mismatch Condition(Void) If Statement """
        input = """
        void main(){
            if (print()){}
        }
        void print(){}
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(print),[]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_mismatch_condition_ifstmt2(self):
        """ Mismatch Condition(Int) If Statement """
        input = """
        void main(){
            int a;
            if (getNum(a)){}
        }
        int getNum(int num){
            return num;
        }
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(getNum),[Id(a)]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_mismatch_condition_ifstmt3(self):
        """ Mismatch Condition(String) If Statement """
        input = """
        void main(){
            string a;
            a = "Hello";
            if (getString(a)){}
            else {}
        }
        string getString(string a){
            return a;
        }
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(getString),[Id(a)]),Block([]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_mismatch_condition_ifstmt4(self):
        """ Mismatch Condition(Float) If Statement """
        input = """
        void main(){
            int a;
            a = 1;
            int b;
            b = 5;
            if (div(a, b)){}
            else {}
        }
        float div(int a, int b){
            float rlt;
            rlt = a / b;
            return rlt;
        }
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(div),[Id(a),Id(b)]),Block([]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,417))

    # TODO: error
    def test_mismatch_condition_ifstmt5(self):
        """ Mismatch Condition(Array) If Statement """
        input = """
        void main(){
            float a[25];
            if (div(a)){}
            else{}
        }
        float[] div(float a[]){
            int i;
            for (i = 0; i < 5; i = i+1){
                a[i] = 1;
            }
            return a;
        }
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(div),[Id(a)]),Block([]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_mismatch_condition_dowhilestmt1(self):
        """ Mismatch Condition(Int) Dowhile Statement """
        input = """
        void main(){
            do {} while(1);
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_mismatch_condition_dowhilestmt2(self):
        """ Mismatch Condition(Float) Dowhile Statement """
        input = """
        void main(){
            int a;
            do {} while(getFloatingPoint(a));
        }
        float getFloatingPoint(int a){
            return a * 1.0;
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],CallExpr(Id(getFloatingPoint),[Id(a)]))"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_mismatch_condition_dowhilestmt3(self):
        """ Mismatch Condition(String) Dowhile Statement """
        input = """
        void main(){
            string str;
            do {} while(getStr(str));
        }
        string getStr(string str){
            return str;
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],CallExpr(Id(getStr),[Id(str)]))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_mismatch_condition_dowhilestmt4(self):
        """ Mismatch Condition(Void) Dowhile Statement """
        input = """
        void main(){
            int a;
            do {} while(putInt(a));
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],CallExpr(Id(putInt),[Id(a)]))"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_mismatch_condition_dowhilestmt5(self):
        """ Mismatch Condition(Array) Dowhile Statement """
        input = """
        void main(){
            int a[25];
            do {} while(a);
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],Id(a))"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_mismatch_condition_forstmt1(self):
        """ Mismatch Condition(Int) For Statement """
        input = """
        void main(){
            int i;
            for (i = 1; i + 1; i = i + 1){}
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(+,Id(i),IntLiteral(1));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([]))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_mismatch_condition_forstmt2(self):
        """ Mismatch Condition(Float) For Statement """
        input = """
        void main(){
            int i;
            for (i = 1; i + getFloat(); i = i + 1){}
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(+,Id(i),CallExpr(Id(getFloat),[]));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([]))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_mismatch_condition_forstmt3(self):
        """ Mismatch Condition(Void) For Statement """
        input = """
        void main(){
            int i;
            for (i = 1; putLn(); i = i + 1){}
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));CallExpr(Id(putLn),[]);BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([]))"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_mismatch_condition_forstmt4(self):
        """ Mismatch Condition(String) For Statement """
        input = """
        void main(){
            int i;
            string a;
            for (i = 1; a; i = i + 1){}
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));Id(a);BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([]))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_mismatch_condition_forstmt5(self):
        """ Mismatch Condition(Array) For Statement """
        input = """
        void main(){
            int i;
            string a[25];
            for (i = 1; a; i = i + 1){}
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));Id(a);BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([]))"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_mismatch_condition_forstmt6(self):
        """ Mismatch Condition(Expr) For Statement """
        input = """
        void main(){
            int i;
            int a;
            int b;
            for (i = 1; add(a, b) / sub(a, b); i = i + 1){}
        }
        int add(int a, int b){
            return a + b;
        }
        int sub(int a, int b){
            return a - b;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(/,CallExpr(Id(add),[Id(a),Id(b)]),CallExpr(Id(sub),[Id(a),Id(b)]));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([]))"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_mismatch_exp1_forstmt1(self):
        """ Mismatch Expr1(Float) For Statement """
        input = """
        void main(){
            float i;
            for (i = 1; i < 10; i = i + 1){
                if (i == 10)
                    return;
            }
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,Id(i),IntLiteral(10)),Return())]))"
        self.assertTrue(TestChecker.test(input,expect,430))
    def test_undecl_identifier(self):
        input = """
        
        void main(){
            a = 10;
        }   
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_undecl_identifier_beyond_scope(self):
        input = """
        
        void main(){
            {
                float a;
            }
            a = 10.1;
        }   
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_undecl_identifier_beyond_many_scope(self):
        input = """
        
        void main(){
            {
                
                {
                    {
                        string b;
                    }
                    b = "dai";
                }
            }
            
        }   
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_correct_vardecl(self):
        input = """
        
        void main(){
            int a;
            {
                {
                    a = 1;
                }
            }
            
        }   
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_break_not_in_loop(self):
        input = """
        
        void main(){
            break;
        }   
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_break_not_in_loop_stmt_if(self):
        input = """
        int a;
        void main(){
            a = 1;
            if(true){
                break;
            }
        }   
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_break_not_in_loop_stmt_if_else(self):
        input = """
        int a;
        void main(){
            a = 1;
            if(true){
                a = a+2;
            }
            else 
                break;
        }   
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_continue_not_in_loop(self):
        input = """
        
        void main(){
            continue;
        }   
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_continue_not_in_loop_stmt_if(self):
        input = """
        int a;
        void main(){
            a = 1;
            if(true){
                continue;
            }
        }   
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_continue_not_in_loop_stmt_if_else(self):
        input = """
        int a;
        void main(){
            a = 1;
            if(true){
                a = a+2;
            }
            else 
                continue;
        }   
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_unreachable_func(self):
        input = """
        
        void a(){
            
        }
        void foo(){
            a();
        }
        
        void main(){
            
        }   
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_unreachable_func_nested_block(self):
        input = """
        
        void a(){
            
        }
        void b(){}
        void foo(){
            { 
                a();
            }
        }
        
        void main(){
            {
                {
                    foo();
                }
            }
        }   
        """
        expect = "Unreachable Function: b"
        self.assertTrue(TestChecker.test(input,expect,442))


    def test_unreachable_func_with_recursion(self):
        input = """
        
        void a(){
            a();
        }
        void b(){
            b();
            b();
        }
        void foo(){
            foo();
        }
        
        void main(){
            a();
            {
                b();
            }
        }   
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_not_left_value_with_var(self):
        input = """
        int a ;
        void main(){
            a + 1 = 10 ;
        }   
        """
        expect = "Not Left Value: BinaryOp(+,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_not_left_value_with_exp_left_not_storage(self):
        input = """
        int a ;
        void main(){
            3 = a;
        }   
        """
        expect = "Not Left Value: IntLiteral(3)"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_not_left_value_with_exp_left_not_storage_function(self):
        input = """
        int foo(){
            return 1;
        }
        void main(){
            3 + 1 = foo();
        }   
        """
        expect = "Not Left Value: BinaryOp(+,IntLiteral(3),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_not_left_value_with_function(self):
        input = """
        int foo(){
            return 1;
        }
        void main(){
            foo() = 10 ;
        }   
        """
        expect = "Not Left Value: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_not_left_value_with_arraycell(self):
        input = """
        int a[6],b[7],c[8];
        void main(){
            b[1] + 1 = c[7] + 10;
        } 
        """
        expect = "Not Left Value: BinaryOp(+,ArrayCell(Id(b),IntLiteral(1)),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_correct_left_value_with_var(self):
        input = """
        int a,b,c;
        void main(){
            a = b = c = 10;
        }   
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_correct_left_value_with_var(self):
        input = """
        int a,b,c;
        void main(){
            a = b = c = (10+3)/4 + 5*9 - 2;
        }   
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_correct_left_value_with_arraycell(self):
        input = """
        int a[6],b[7],c[8];
        void main(){
            a[1] = a[2] = a[4] + 10;
        }   
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_correct_left_value_with_arraycell_2(self):
        input = """
        int a[6],b[7],c[8];
        void main(){
            a[1] = b[1] = c[7] + 10%5;
        }   
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_TypeMismatchExpr_ArrayCell_with_type_idx_float(self):
        input = """
        void main(){
            int a[5];
            a[1.2] = 5;
        }   
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLiteral(1.2))"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_TypeMismatchExpr_ArrayCell_with_type_idx_string(self):
        input = """
        void main(){
            int a[5];
            a["1"] = 9;
        }   
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),StringLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_TypeMismatchExpr_ArrayCell_with_type_idx_bool(self):
        input = """
        void main(){
            int a[5];
            a[true] = 9;
        }   
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_TypeMismatchExpr_ArrayCell_with_type_arr_int(self):
        input = """
        void main(){
            int a;
            a[5] = 10;
        }   
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_TypeMismatchExpr_ArrayCell_with_type_arr_string(self):
        input = """
        void main(){
            string a;
            a[5] = 10;
        }   
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_correct_ArrayCell_with_type_arr_ArrayPointer(self):
        input = """
        void main(int a[], float b){
            a[1] = 9;
        }   
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,458))


    def test_TypeMismatchInExpression_IntType_BoolType(self):
        input = """
        void main(){int a; a = true;}   
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_TypeMismatchInExpression_Sum_IntType_StringType(self):
        input = """
        void main(){int a; string b; a = 1 + b;}   
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,460))
    def test__simple_arrayInttype_and_exp_on_int(self):
        input = """
        int a[12];
        int func(){
            a[0] = 2;
            a[1] = 3;
            return  a[0] + 4 + a[1];
        }
        void main(){
            a[2] = func();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,461))
    def test__simple_nested_LB_and_RB_and_exp_on_string(self):
        input = """
        int a[12];
        int func(){
            if(((1 == 2))){
                return a[2];
            }
            else return a[2]+a[3];
        }
        void main(){
            a[4] = func();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,462))
    def test__arraycell_type_int_and_return_float(self):
        input = """
        int a[12];
        float func(){
            if(((1 == 2))){
                return a[2];
            }
            else return a[2]+a[3];
        }
        void main(){
            a[4] = func();
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(a),IntLiteral(4)),CallExpr(Id(func),[]))"
        self.assertTrue(TestChecker.test(input,expect,463))
    def test__nested_func(self):
        input = """
        int a[12];
        float func(){
            if(true){
                return foo1();
            }
            else return a[2]+a[3]*foo1()-foo2(a[4]);
        }
        void main(){
            float b;
            b = func();
        }
        int foo1(){
            return 1;
        }
        float foo2(int x){
            return x;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,464))
    def test__simple_redecl_arraytype(self):
        input = """
        int a[12];
        int func(){
            a[0] = 2;
            a[1] = 3;
            return  a[0] + 4 + a[1];
        }
        void main(){
            int a;
            a[2] = func();
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,465))
    def test_rename_main_func(self):
        input = """
        int i;
        int f(){
            int main;
            main =200;
            return main;
        }
        void main(){
            int main;
            main = f();
            putIntLn(main);
            {
                int i;
                float main;
                int f;
                main = f = i = 100;
                putIntLn(f);
            }
            putIntLn(main);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,466))
    def test_nested_nested_func(self):
        input = """
        int a[12];
        int func(int x){
            return func(func(func(func(x))));
        }
        void main(){
            a[2] = func(a[0]);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,467))
    def test_arraypointer_and_array_nested_in_exp(self):
        input = """
        int[] func(int x){
            int a[10];
            return a;
        }
        void main(){
            int x,a,b[5],c[9];
            func(x+a)[x+b[1]*c[b[2]-a%b[c[6]%2]]]= b[func(b[1-c[5]])[x+c[b[c[4]]]]*c[b[4]-1]];
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,468))
    def test_not_left_value_in_nested_assigmnet(self):
        input = """
        void main(){
            float a,b,c,d;
            a = b+c+d;
            a = b+c+d=d;
        }
        """
        expect = "Not Left Value: BinaryOp(+,BinaryOp(+,Id(b),Id(c)),Id(d))"
        self.assertTrue(TestChecker.test(input,expect,469))
    def test_type_miss_match_exp_float_in_if(self):
        input = """
        void main(){
            float a,b,c,d;
            if(a){
                a = a+1;
            }
            else b = b-c;
        }
        """
        expect = "Type Mismatch In Statement: If(Id(a),Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))]),BinaryOp(=,Id(b),BinaryOp(-,Id(b),Id(c))))"
        self.assertTrue(TestChecker.test(input,expect,470))
    def test_type_nested_unaryOp(self):
        input = """
        void main(){
            float a,b;
            int c,d,e;
            a = -----c+--d--b----e;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,471))
    def test_break_in_dowhile_not_in_block(self):
        input = """
        void main(){
            int a,b,c;
            do
                a = 1;
                b = a*2;
                c = b-a+b*b;
                break;
                continue;
            while(!(a>0));
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,472))
    def test_simple_arraytype_string(self):
        input = """
        void main(){
            int a,b,c;
            string f[5];
            f[0] = "hello";
            f[1] = "hi";
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,473))
    def test_simple_index_in_array_not_integer(self):
        input = """
        void main(){
            int a,c;
            float b;
            b = 1;
            string f[5];
            f[0] = "hello";
            f[b] = "hi";
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(f),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,474))
    def test_simple_return_stmt_and_unaryop_and_assigment(self):
        input = """
        boolean main(){
            int a,b,c;
            return !(a>=(b = c));
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,475))
    def test_simple__un_not_left_value_in_nested_assigmnet(self):
        input = """
        void main(){
            float a,b,c,d;
            a = b+c+d;
            a = b-(c = d*(a = a-1));
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,476))
    def test_another_func_call_main_func_int_in_float(self):
        input = """
        boolean main(){
            float a;
            a = foo();
            return true;
        }
        float foo(){
            int a[5];
            if(main()){
                int a;
                return a;
            }
            return a[2];
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,477))
    def test_type_miss_match_stmt_Int_pointer_in_Float_pointer(self):
        input = """
        boolean main(){
            float a[5];
            foo();
            return true;
        }
        float[] foo(){
            int a[5];
            if(main()){
                float a[4];
                return a;
            }
            return a;
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,478))
    def test_simple_return_in_dowhile_and_for_not_in_block(self):
        input = """
        float main(){
            int a,b,c,d;
            for(1; true; 2) return a;
            do 
                return b;
            while(!(a==b));
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,479))
    def test_simple_Prime_number_program(self):
        input = """
        int main()
        {
            int low, high, i, flag;
            putIntLn(low);
            putIntLn(high);
            
            do
            {
                flag = 0;
                for(i = 2; i <= low/2; i = i+1)
                {
                    if(low % i == 0)
                    {
                        flag = 1;
                        break;
                    }
                }
                if (flag == 0)
                   i = getInt();
                low = low +1;
            }while (low < high);
            return 0;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,480))
    def test_lhs_of_assignment_operator_is_not_array_cell(self):
        """LHS of assignment operator is not array cell """
        input = """
                int hung(int a, float b[], string c) {
                    return 23123;
                }
               void main(){
                    float hunG[23];
                    int a;
                    a = a + 1;
                    putInt(a);
                    a = a* 1;
                    hung(2, hunG, "32");
                    (hunG[23] + 2) = 43;
                    return;
                }
                """
        expect = "Not Left Value: BinaryOp(+,ArrayCell(Id(hunG),IntLiteral(23)),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,481))
    
    def test_factorial_program(self):
        """Factorial program """
        input = """
                int func1(int n){
                    if (n == 0)
                        return 1;
                    else
                        return n * func1(n - 1);
                }
                int func2(int x){
                    return 32;
                }
                int main() {
                    int n, result;
                    n = 4;
                    result = func1(n);
                    return result;
                }
                """
        expect = "Unreachable Function: func2"
        self.assertTrue(TestChecker.test(input,expect,482))
    
    def test_random_program(self):
        """Random program """
        input = """
                int a, b, c, d, t;
                void main1() {
                    foo();
                    return;
                }
                int foo () {
                    main1();
                    if (a+1 == 4) {{{{if(b+a == 2) foo();}}}} else {if (c+d == 32) a = 32; else a = 341;}
                    return 23;
                }
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,483))
    
    def test_calsum_program(self):
        """Calsum program """
        input = """
                void main(){
                    int oddSum, evenSum,arr[10],i;
                    oddSum = evenSum = 0;
                    for(i=0;i<10;i=i+1)
                        arr[i]=i;
                    for(i=0;i<10;i=i+1){
                        if(arr[i]%2==0)
                            evenSum = evenSum + arr[i];
                        else
                            oddSum = oddSum + arr[i];
                    }
                }  
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,484))
    
    def test_calsumrandom_program(self):
        """Calsumrandom Program """
        input = """
                int main1() {
                    return 23;
                }
                int main()
                {
                    int i, n;
                    int S;
                    S = 0;
                    i = 1;
                    do
                    {
                        S = S + i;
                        i = i + 1;
                    }while(i <= n);
                    return 0;
                } 
                """
        expect = "Unreachable Function: main1"
        self.assertTrue(TestChecker.test(input,expect,485))
    
    def test_calrandom_program(self):
        """Calrandom Program """
        input = """
                int main()
                {
                    int a, b, i, n;
                    float x, S, T;
                    float M;
                    do
                    {
                        if(n < 1)
                        {
                            a + b - 3213;
                        }
                    }while(n < 1);
                    S = 0;
                    T = 1;
                    M = 0;
                    i = 1;

                    do
                    {
                        T = T * x;
                        M = M + i;
                        S = S + T/M;
                        i = i + 1;
                        2 = i;
                    }
                    while(i <= n);
                    return 0;
                }
                """
        expect = "Not Left Value: IntLiteral(2)"
        self.assertTrue(TestChecker.test(input,expect,486))
    
    def test_calnumofdayinmonth_program(self):
        """Calnumofdayinmonth Program """
        input = """
               int main(){return 1;}
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,487))
    
    def test_printVND_program(self):
        """PrintVND Program """
        input = """
                void getch() {
                    return;
                }
                int main()
                {
                    int i, j, k;
                    for (i = 0; i <= 200; i = i + 1)
                        for (j = 0; j <= 100; j = j + 1)
                            for (k = 0; k <= 40; k = k + 1)
                                if (i * 1000 + j * 2000 + k * 5000 == 200000)
                                    printf("%d to 1000(VND) -  %d to 2000(VND) - %d to 5000(VND) ", i, j, k);
                
                    getch();
                    return 0;
                }
                """
        expect = "Undeclared Function: printf"
        self.assertTrue(TestChecker.test(input,expect,488))
    
    def test_calPower_n_program(self):
        """CalPower Program """
        input = """
                float Power_n(float x, int n)
                {
                    float result;
                    result = 1;
                    do
                    {
                        n = n - 1;
                        result = result * x;
                    }while(n > 0);
                    return result;
                }
                float qPower_n(float x, int n)
                {
                    float result;
                    result = 1;
                    do
                    {
                        if(n % 2 == 1)
                        {
                            result = result * x;
                        }
                        x = x * x;
                        n = n / 2;
                    }while(n != 0);
                    return result;
                }
                int main()
                {
                    float x;
                    x = 4;
                    int n;
                    n = 2;
                    float z;
                    z = qPower_n(x, n);
                    return 23;
                } 
                """
        expect = "Unreachable Function: Power_n"
        self.assertTrue(TestChecker.test(input,expect,489))
    
    def test_calsumofintegers_program(self):
        """Calsumofintegers Program """
        input = """
                int main1() {
                    return 23;
                }
                int main()
                {
                    int i, n;
                    int S;
                    S = 0;
                    for (i = 0; i < n; i = i + 1)
                        S = S + i;
                    return S;
                }   
                """
        expect = "Unreachable Function: main1"
        self.assertTrue(TestChecker.test(input,expect,490))
    
    def test_calimulj_program(self):
        """Calimulj Program """
        input = """
                int main()
                {
                    int i, j;
                    int result;
                    for(i = 1; i <= 10; i = i + 1)
                    {
                        for(j = 2; j <= 9; j = j + 1)
                        {
                            result = i * j;
                        }
                    }
                    break;
                    return result;
                }
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,491))
    
    def test_calucln_program(self):
        """Calucln Program """
        input = """
                int main()
                {
                    int a, b;
                    a = 2;
                    b = 6;
                    do
                    {
                        if(a > b)
                        {
                            a = a - b;
                            return;
                        }
                        else
                            b = b - a;
                    }while(a != b);      
                    return 23;              
                }
                """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,492))
    
    def test_calfibonacci_program(self):
        """Calfibonacci Program """
        input = """
                void printf(string c, int d) {
                    return;
                }
                int main() {
                    int a, b, c, i, n;

                    n = 6;

                    a = b = 1;
                    printf("In day Fibonacci: ", 2);

                    for(i = 1; i <= n-2; i = i + 1) {
                        c = a + b;
                        printf("%d ", c);
                        
                        a = b;
                        b = c;
                    }
                    float a;
                    return 0;
                }
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,493))
    
    def test_ptbac2_program(self):
        """Ptbac2 Program """
        input = """
                void printf(string c) {
                    return ;
                }
                int main()
                {
                    int a, b, c; 

                    printf("Nhap vao a = ");

                    printf("Nhap vao b = ");

                    printf("Nhap vao c = ");

                    if (a == 0)
                    {
                        if (b == 0) 
                        {
                            if (c == 0)
                            {
                                printf("Phuong trinh co vo so nghiem");
                            }
                            else
                            {
                                printf("Phuong trinh vo nghiem");
                            }
                        }
                        else
                        {

                            float x;
                            x = -c/b;
                            printf("Phuong trinh co nghiem duy nhat");
                        }
                    }
                    else
                    {
                        float Denta;
                        Denta = b * b - 4 * a * c;
                        if (Denta < 0)
                        {
                            printf("Phuong trinh vo nghiem");
                        }
                        else 
                        {
                            float x1;
                            x1 = (-b + sqrt(Denta)) / (2 * a);
                            float x2;
                            x2 = (-b - sqrt(Denta)) / (2 * a);
                            printf("Phuong trinh co 2 nghiem phan biet");
                        }
                    }
                    return 0;
                }
                """
        expect = "Undeclared Function: sqrt"
        self.assertTrue(TestChecker.test(input,expect,494))
    
    def test_calpermutation_program(self):
        """CalPermutation Program """
        input = """
                int factorial(int n) {
                    int f;

                    for(f = 1; n > 1; n = n - 1)
                        f = f*n;

                    return f;
                }

                int npr(int n,int r) {
                    return factorial(n)/factorial(n-r);
                }

                int main() {
                    int n, r, result;

                    n = 4;
                    r = 3;
                    npr(n, r) = result;
                    return npr(n, r);
                }
                """
        expect = "Not Left Value: CallExpr(Id(npr),[Id(n),Id(r)])"
        self.assertTrue(TestChecker.test(input,expect,495))
    
    def test_calfloydtriangle_program(self):
        """CalFloydTriangle Program """
        input = """
                void printf(string c) {
                    return c;
                }
                int main() {
                    int n,i,j,k;

                    k = 1;

                    n = 5;

                    printf("Ve tam giac Floyd: ");
                    for(i = 1; i <= n; i = i + 1) {
                        for(j=1;j <= i; j = j + 1)
                            k = k + 1;
                        printf("");
                    }
                    
                    return 0;
                }
                """
        expect = "Type Mismatch In Statement: Return(Id(c))"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_printoddoreven_program(self):
        """PrintOddorEven Program """
        input = """
                void printf(string c, int d) {
                    return;
                }
                int main() {
                    int even;
                    int odd;
                    even = 24;
                    odd = 31;
                    if (even && 2 == 0) {
                        printf("%d la so chan", even);
                    } else {
                        printf("%d la so le", even);
                    }
                    if (odd % 2 != 0 ) {
                        printf("%d la so le", odd);
                    } else {
                        printf("%d la so chan", odd);
                    }
                    return 0;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(even),BinaryOp(==,IntLiteral(2),IntLiteral(0)))"
        self.assertTrue(TestChecker.test(input,expect,497))
    
    def test_printnumber_program(self):
        """PrintNumber Program """
        input = """
                void printf(string c, int d) {
                    main1();
                    return;
                }
                int main1() {
                    int number;
                    number = -2;
                    if (number >= 0)
                        printf("%d la so duong", number);
                    else
                        printf("%d la so am", number);
                    return 0;
                }
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,498))
    
    def test_checkprimenumber_program(self):
        """CheckPrimeNumber Program """
        input = """
                int main1() {
                    main1();
                    return 324;
                }
                void printf(string c, int d) {
                    return;
                }
                int main() { 
                    int loop, number;
                    int prime;
                    prime = 1;
                    number = 19;

                    for(loop = 2; loop < number; loop = loop + 1) {
                        if((number % loop) == 0) {
                            prime = 0;
                        }
                    }

                    if (prime == 1)
                        printf("So %d la so nguyen to.", number);
                    else
                        printf("So %d khong phai la so nguyen to.", number);
                    return 0;
                }
                """
        expect = "Unreachable Function: main1"
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_hide_function(self):
        input = """
                int foo(){return 1;}
                int main() {
                    int foo;
                    foo();
                    return 0;
                }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,500))
