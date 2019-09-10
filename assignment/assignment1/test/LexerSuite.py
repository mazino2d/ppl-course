import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
    def test_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            '//Hello\n/*Hi\nYay*///?!@#$%^//',
            '<EOF>',101))
    def test_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "_ _1 x X aA1_",
            "_,_1,x,X,aA1_,<EOF>",102))
    def test_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            'break continue else for if return do while',
            'break,continue,else,for,if,return,do,while,<EOF>',103))
    def test_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            '+ - * / % ! || && != == < > <= >= =',
            '+,-,*,/,%,!,||,&&,!=,==,<,>,<=,>=,=,<EOF>',104))
    def test_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            '[ ] { } ( ) ; ,',
            '[,],{,},(,),;,,,<EOF>',105))
    def test_6(self):
        self.assertTrue(TestLexer.checkLexeme(
            '1 2 3 4 5 6 7 8 9 0 01 10 000',
            '1,2,3,4,5,6,7,8,9,0,01,10,000,<EOF>',106))
    def test_7(self):
        self.assertTrue(TestLexer.checkLexeme(
            '1. .1 1.e1 1E-2 1.0e1 3.14',
            '1.,.1,1.e1,1E-2,1.0e1,3.14,<EOF>',107))
    def test_8(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' "Compiler" "Escape\n" "\f\r\n\t\"\\" ''',
            r'''Compiler,Escape\n,\f\r\n\t\"\\,<EOF>''',108))
    def test_9(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' "abc ''',
            r'''Unclosed String: abc ''',109))
    def test_10(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' "Hi, this is illegall escape \i" ''',
            r'''Illegal Escape In String: Hi, this is illegall escape \i''' ,110))
    def test_11(self):
        self.assertTrue(TestLexer.checkLexeme(
            '1>2?3',
            '1,>,2,Error Token ?',111))
    def test_12(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''int a = (int) 12.6;''',
            'int,a,=,(,int,),12.6,;,<EOF>',112))
    def test_13(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' printf("Hello World"); ''',
            r'''printf,(,Hello World,),;,<EOF>''',113))
    def test_14(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' if(m % 2 == 0) return true;''',
            r'''if,(,m,%,2,==,0,),return,true,;,<EOF>''',114))
    def test_15(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' for(int i = 0; i < n; i = i +1) {printf("");} ''',
            r'''for,(,int,i,=,0,;,i,<,n,;,i,=,i,+,1,),{,printf,(,,),;,},<EOF>''',115))
    def test_16(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' float a; while(a < 10) {a = a - 1;} ''',
            r'''float,a,;,while,(,a,<,10,),{,a,=,a,-,1,;,},<EOF>''',116))
    def test_17(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' /* /*  */ */ ''',
            r'''*,/,<EOF>''',117))
    def test_18(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' while(1<2<3>4>5) {ok();} ''',
            r'''while,(,1,<,2,<,3,>,4,>,5,),{,ok,(,),;,},<EOF>''',118))
    def test_19(self):
        self.assertTrue(TestLexer.checkLexeme(
            '{{{{{{{{{int a= 10;}}}}}}}}}',
            '{,{,{,{,{,{,{,{,{,int,a,=,10,;,},},},},},},},},},<EOF>',119))
    def test_20(self):
        self.assertTrue(TestLexer.checkLexeme(
            '#include <stdio.h>',
            'Error Token #',120))
    def test_21(self):
        self.assertTrue(TestLexer.checkLexeme('','',121))
    def test_22(self):
        self.assertTrue(TestLexer.checkLexeme('','',122))
    def test_23(self):
        self.assertTrue(TestLexer.checkLexeme('','',123))
    def test_24(self):
        self.assertTrue(TestLexer.checkLexeme('','',124))
    def test_25(self):
        self.assertTrue(TestLexer.checkLexeme('','',125))
    def test_26(self):
        self.assertTrue(TestLexer.checkLexeme('','',126))
    def test_27(self):
        self.assertTrue(TestLexer.checkLexeme('','',127))
    def test_28(self):
        self.assertTrue(TestLexer.checkLexeme('','',128))
    def test_29(self):
        self.assertTrue(TestLexer.checkLexeme('','',129))
    def test_30(self):
        self.assertTrue(TestLexer.checkLexeme('','',130))
    def test_31(self):
        self.assertTrue(TestLexer.checkLexeme('','',131))
    def test_32(self):
        self.assertTrue(TestLexer.checkLexeme('','',132))
    def test_33(self):
        self.assertTrue(TestLexer.checkLexeme('','',133))
    def test_34(self):
        self.assertTrue(TestLexer.checkLexeme('','',134))
    def test_35(self):
        self.assertTrue(TestLexer.checkLexeme('','',135))
    def test_36(self):
        self.assertTrue(TestLexer.checkLexeme('','',136))
    def test_37(self):
        self.assertTrue(TestLexer.checkLexeme('','',137))
    def test_38(self):
        self.assertTrue(TestLexer.checkLexeme('','',138))
    def test_39(self):
        self.assertTrue(TestLexer.checkLexeme('','',139))
    def test_40(self):
        self.assertTrue(TestLexer.checkLexeme('','',140))
    def test_41(self):
        self.assertTrue(TestLexer.checkLexeme('','',141))
    def test_42(self):
        self.assertTrue(TestLexer.checkLexeme('','',142))
    def test_43(self):
        self.assertTrue(TestLexer.checkLexeme('','',143))
    def test_44(self):
        self.assertTrue(TestLexer.checkLexeme('','',144))
    def test_45(self):
        self.assertTrue(TestLexer.checkLexeme('','',145))
    def test_46(self):
        self.assertTrue(TestLexer.checkLexeme('','',146))
    def test_47(self):
        self.assertTrue(TestLexer.checkLexeme('','',147))
    def test_48(self):
        self.assertTrue(TestLexer.checkLexeme('','',148))
    def test_49(self):
        self.assertTrue(TestLexer.checkLexeme('','',149))
    def test_50(self):
        self.assertTrue(TestLexer.checkLexeme('','',150))
    def test_51(self):
        self.assertTrue(TestLexer.checkLexeme('','',151))
    def test_52(self):
        self.assertTrue(TestLexer.checkLexeme('','',152))
    def test_53(self):
        self.assertTrue(TestLexer.checkLexeme('','',153))
    def test_54(self):
        self.assertTrue(TestLexer.checkLexeme('','',154))
    def test_55(self):
        self.assertTrue(TestLexer.checkLexeme('','',155))
    def test_56(self):
        self.assertTrue(TestLexer.checkLexeme('','',156))
    def test_57(self):
        self.assertTrue(TestLexer.checkLexeme('','',157))
    def test_58(self):
        self.assertTrue(TestLexer.checkLexeme('','',158))
    def test_59(self):
        self.assertTrue(TestLexer.checkLexeme('','',159))
    def test_60(self):
        self.assertTrue(TestLexer.checkLexeme('','',160))
    def test_61(self):
        self.assertTrue(TestLexer.checkLexeme('','',161))
    def test_62(self):
        self.assertTrue(TestLexer.checkLexeme('','',162))
    def test_63(self):
        self.assertTrue(TestLexer.checkLexeme('','',163))
    def test_64(self):
        self.assertTrue(TestLexer.checkLexeme('','',164))
    def test_65(self):
        self.assertTrue(TestLexer.checkLexeme('','',165))
    def test_66(self):
        self.assertTrue(TestLexer.checkLexeme('','',166))
    def test_67(self):
        self.assertTrue(TestLexer.checkLexeme('','',167))
    def test_68(self):
        self.assertTrue(TestLexer.checkLexeme('','',168))
    def test_69(self):
        self.assertTrue(TestLexer.checkLexeme('','',169))
    def test_70(self):
        self.assertTrue(TestLexer.checkLexeme('','',170))
    def test_71(self):
        self.assertTrue(TestLexer.checkLexeme('','',171))
    def test_72(self):
        self.assertTrue(TestLexer.checkLexeme('','',172))
    def test_73(self):
        self.assertTrue(TestLexer.checkLexeme('','',173))
    def test_74(self):
        self.assertTrue(TestLexer.checkLexeme('','',174))
    def test_75(self):
        self.assertTrue(TestLexer.checkLexeme('','',175))
    def test_76(self):
        self.assertTrue(TestLexer.checkLexeme('','',176))
    def test_77(self):
        self.assertTrue(TestLexer.checkLexeme('','',177))
    def test_78(self):
        self.assertTrue(TestLexer.checkLexeme('','',178))
    def test_79(self):
        self.assertTrue(TestLexer.checkLexeme('','',179))
    def test_80(self):
        self.assertTrue(TestLexer.checkLexeme('','',180))
    def test_81(self):
        self.assertTrue(TestLexer.checkLexeme('','',181))
    def test_82(self):
        self.assertTrue(TestLexer.checkLexeme('','',182))
    def test_83(self):
        self.assertTrue(TestLexer.checkLexeme('','',183))
    def test_84(self):
        self.assertTrue(TestLexer.checkLexeme('','',184))
    def test_85(self):
        self.assertTrue(TestLexer.checkLexeme('','',185))
    def test_86(self):
        self.assertTrue(TestLexer.checkLexeme('','',186))
    def test_87(self):
        self.assertTrue(TestLexer.checkLexeme('','',187))
    def test_88(self):
        self.assertTrue(TestLexer.checkLexeme('','',188))
    def test_89(self):
        self.assertTrue(TestLexer.checkLexeme('','',189))
    def test_90(self):
        self.assertTrue(TestLexer.checkLexeme('','',190))
    def test_91(self):
        self.assertTrue(TestLexer.checkLexeme('','',191))
    def test_92(self):
        self.assertTrue(TestLexer.checkLexeme('','',192))
    def test_93(self):
        self.assertTrue(TestLexer.checkLexeme('','',193))
    def test_94(self):
        self.assertTrue(TestLexer.checkLexeme('','',194))
    def test_95(self):
        self.assertTrue(TestLexer.checkLexeme('','',195))
    def test_96(self):
        self.assertTrue(TestLexer.checkLexeme('','',196))
    def test_97(self):
        self.assertTrue(TestLexer.checkLexeme('','',197))
    def test_98(self):
        self.assertTrue(TestLexer.checkLexeme('','',198))
    def test_99(self):
        self.assertTrue(TestLexer.checkLexeme('','',199))
    def test_100(self):
        self.assertTrue(TestLexer.checkLexeme('','',200))
