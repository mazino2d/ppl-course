# Generated from /home/kraken/ppl-course/assignment/assignment1/main/mc/parser/MC.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u01a7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\5\6\u0089\n\6\3\7\3\7\5\7\u008d\n\7\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\5\f\u009b")
        buf.write("\n\f\3\f\6\f\u009e\n\f\r\f\16\f\u009f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\5\34\u00f8\n\34\3\34\3\34\3")
        buf.write("\34\7\34\u00fd\n\34\f\34\16\34\u0100\13\34\3\35\3\35\3")
        buf.write("\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$")
        buf.write("\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*")
        buf.write("\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\64\6\64\u0137\n\64\r\64\16\64\u0138")
        buf.write("\3\65\6\65\u013c\n\65\r\65\16\65\u013d\3\65\3\65\7\65")
        buf.write("\u0142\n\65\f\65\16\65\u0145\13\65\3\65\5\65\u0148\n\65")
        buf.write("\3\65\7\65\u014b\n\65\f\65\16\65\u014e\13\65\3\65\3\65")
        buf.write("\6\65\u0152\n\65\r\65\16\65\u0153\3\65\5\65\u0157\n\65")
        buf.write("\3\65\6\65\u015a\n\65\r\65\16\65\u015b\3\65\3\65\5\65")
        buf.write("\u0160\n\65\3\66\3\66\5\66\u0164\n\66\3\67\3\67\7\67\u0168")
        buf.write("\n\67\f\67\16\67\u016b\13\67\3\67\3\67\3\67\38\38\38\3")
        buf.write("8\78\u0174\n8\f8\168\u0177\138\38\38\39\39\39\79\u017e")
        buf.write("\n9\f9\169\u0181\139\39\39\39\39\39\3:\6:\u0189\n:\r:")
        buf.write("\16:\u018a\3:\3:\3;\3;\7;\u0191\n;\f;\16;\u0194\13;\3")
        buf.write(";\5;\u0197\n;\3;\3;\3<\3<\7<\u019d\n<\f<\16<\u01a0\13")
        buf.write("<\3<\3<\3<\3=\3=\3=\3\u017f\2>\3\3\5\2\7\2\t\2\13\2\r")
        buf.write("\2\17\2\21\2\23\2\25\2\27\2\31\4\33\5\35\6\37\7!\b#\t")
        buf.write("%\n\'\13)\f+\r-\16/\17\61\20\63\21\65\22\67\239\24;\25")
        buf.write("=\26?\27A\30C\31E\32G\33I\34K\35M\36O\37Q S!U\"W#Y$[%")
        buf.write("]&_\'a(c)e*g+i,k-m.o/q\60s\61u\62w\63y\64\3\2\13\3\2\62")
        buf.write(";\3\2c|\3\2C\\\6\2\n\f\16\17$$^^\t\2$$^^ddhhppttvv\4\2")
        buf.write("GGgg\4\2\f\f\17\17\5\2\13\f\17\17\"\"\7\3\n\f\16\17$$")
        buf.write("))^^\2\u01b5\2\3\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\3{\3\2\2")
        buf.write("\2\5\u0080\3\2\2\2\7\u0082\3\2\2\2\t\u0084\3\2\2\2\13")
        buf.write("\u0088\3\2\2\2\r\u008c\3\2\2\2\17\u008e\3\2\2\2\21\u0091")
        buf.write("\3\2\2\2\23\u0094\3\2\2\2\25\u0096\3\2\2\2\27\u0098\3")
        buf.write("\2\2\2\31\u00a1\3\2\2\2\33\u00a9\3\2\2\2\35\u00ad\3\2")
        buf.write("\2\2\37\u00b3\3\2\2\2!\u00ba\3\2\2\2#\u00bf\3\2\2\2%\u00c2")
        buf.write("\3\2\2\2\'\u00c8\3\2\2\2)\u00cc\3\2\2\2+\u00d2\3\2\2\2")
        buf.write("-\u00db\3\2\2\2/\u00de\3\2\2\2\61\u00e3\3\2\2\2\63\u00ea")
        buf.write("\3\2\2\2\65\u00ef\3\2\2\2\67\u00f7\3\2\2\29\u0101\3\2")
        buf.write("\2\2;\u0103\3\2\2\2=\u0105\3\2\2\2?\u0107\3\2\2\2A\u0109")
        buf.write("\3\2\2\2C\u010b\3\2\2\2E\u010d\3\2\2\2G\u0110\3\2\2\2")
        buf.write("I\u0113\3\2\2\2K\u0116\3\2\2\2M\u0119\3\2\2\2O\u011b\3")
        buf.write("\2\2\2Q\u011d\3\2\2\2S\u0120\3\2\2\2U\u0123\3\2\2\2W\u0125")
        buf.write("\3\2\2\2Y\u0127\3\2\2\2[\u0129\3\2\2\2]\u012b\3\2\2\2")
        buf.write("_\u012d\3\2\2\2a\u012f\3\2\2\2c\u0131\3\2\2\2e\u0133\3")
        buf.write("\2\2\2g\u0136\3\2\2\2i\u015f\3\2\2\2k\u0163\3\2\2\2m\u0165")
        buf.write("\3\2\2\2o\u016f\3\2\2\2q\u017a\3\2\2\2s\u0188\3\2\2\2")
        buf.write("u\u018e\3\2\2\2w\u019a\3\2\2\2y\u01a4\3\2\2\2{|\7o\2\2")
        buf.write("|}\7c\2\2}~\7k\2\2~\177\7p\2\2\177\4\3\2\2\2\u0080\u0081")
        buf.write("\t\2\2\2\u0081\6\3\2\2\2\u0082\u0083\t\3\2\2\u0083\b\3")
        buf.write("\2\2\2\u0084\u0085\t\4\2\2\u0085\n\3\2\2\2\u0086\u0089")
        buf.write("\5\7\4\2\u0087\u0089\5\t\5\2\u0088\u0086\3\2\2\2\u0088")
        buf.write("\u0087\3\2\2\2\u0089\f\3\2\2\2\u008a\u008d\n\5\2\2\u008b")
        buf.write("\u008d\5\17\b\2\u008c\u008a\3\2\2\2\u008c\u008b\3\2\2")
        buf.write("\2\u008d\16\3\2\2\2\u008e\u008f\7^\2\2\u008f\u0090\t\6")
        buf.write("\2\2\u0090\20\3\2\2\2\u0091\u0092\7^\2\2\u0092\u0093\n")
        buf.write("\6\2\2\u0093\22\3\2\2\2\u0094\u0095\7\60\2\2\u0095\24")
        buf.write("\3\2\2\2\u0096\u0097\7a\2\2\u0097\26\3\2\2\2\u0098\u009a")
        buf.write("\t\7\2\2\u0099\u009b\7/\2\2\u009a\u0099\3\2\2\2\u009a")
        buf.write("\u009b\3\2\2\2\u009b\u009d\3\2\2\2\u009c\u009e\5\5\3\2")
        buf.write("\u009d\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u009d\3")
        buf.write("\2\2\2\u009f\u00a0\3\2\2\2\u00a0\30\3\2\2\2\u00a1\u00a2")
        buf.write("\7d\2\2\u00a2\u00a3\7q\2\2\u00a3\u00a4\7q\2\2\u00a4\u00a5")
        buf.write("\7n\2\2\u00a5\u00a6\7g\2\2\u00a6\u00a7\7c\2\2\u00a7\u00a8")
        buf.write("\7p\2\2\u00a8\32\3\2\2\2\u00a9\u00aa\7k\2\2\u00aa\u00ab")
        buf.write("\7p\2\2\u00ab\u00ac\7v\2\2\u00ac\34\3\2\2\2\u00ad\u00ae")
        buf.write("\7h\2\2\u00ae\u00af\7n\2\2\u00af\u00b0\7q\2\2\u00b0\u00b1")
        buf.write("\7c\2\2\u00b1\u00b2\7v\2\2\u00b2\36\3\2\2\2\u00b3\u00b4")
        buf.write("\7u\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6\7t\2\2\u00b6\u00b7")
        buf.write("\7k\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9\7i\2\2\u00b9 \3")
        buf.write("\2\2\2\u00ba\u00bb\7x\2\2\u00bb\u00bc\7q\2\2\u00bc\u00bd")
        buf.write("\7k\2\2\u00bd\u00be\7f\2\2\u00be\"\3\2\2\2\u00bf\u00c0")
        buf.write("\7f\2\2\u00c0\u00c1\7q\2\2\u00c1$\3\2\2\2\u00c2\u00c3")
        buf.write("\7y\2\2\u00c3\u00c4\7j\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6")
        buf.write("\7n\2\2\u00c6\u00c7\7g\2\2\u00c7&\3\2\2\2\u00c8\u00c9")
        buf.write("\7h\2\2\u00c9\u00ca\7q\2\2\u00ca\u00cb\7t\2\2\u00cb(\3")
        buf.write("\2\2\2\u00cc\u00cd\7d\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf")
        buf.write("\7g\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1\7m\2\2\u00d1*\3")
        buf.write("\2\2\2\u00d2\u00d3\7e\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5")
        buf.write("\7p\2\2\u00d5\u00d6\7v\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8")
        buf.write("\7p\2\2\u00d8\u00d9\7w\2\2\u00d9\u00da\7g\2\2\u00da,\3")
        buf.write("\2\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd\7h\2\2\u00dd.\3")
        buf.write("\2\2\2\u00de\u00df\7g\2\2\u00df\u00e0\7n\2\2\u00e0\u00e1")
        buf.write("\7u\2\2\u00e1\u00e2\7g\2\2\u00e2\60\3\2\2\2\u00e3\u00e4")
        buf.write("\7t\2\2\u00e4\u00e5\7g\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7")
        buf.write("\7w\2\2\u00e7\u00e8\7t\2\2\u00e8\u00e9\7p\2\2\u00e9\62")
        buf.write("\3\2\2\2\u00ea\u00eb\7v\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed")
        buf.write("\7w\2\2\u00ed\u00ee\7g\2\2\u00ee\64\3\2\2\2\u00ef\u00f0")
        buf.write("\7h\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2\7n\2\2\u00f2\u00f3")
        buf.write("\7u\2\2\u00f3\u00f4\7g\2\2\u00f4\66\3\2\2\2\u00f5\u00f8")
        buf.write("\5\13\6\2\u00f6\u00f8\5\25\13\2\u00f7\u00f5\3\2\2\2\u00f7")
        buf.write("\u00f6\3\2\2\2\u00f8\u00fe\3\2\2\2\u00f9\u00fd\5\13\6")
        buf.write("\2\u00fa\u00fd\5\25\13\2\u00fb\u00fd\5\5\3\2\u00fc\u00f9")
        buf.write("\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fb\3\2\2\2\u00fd")
        buf.write("\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2")
        buf.write("\u00ff8\3\2\2\2\u0100\u00fe\3\2\2\2\u0101\u0102\7-\2\2")
        buf.write("\u0102:\3\2\2\2\u0103\u0104\7/\2\2\u0104<\3\2\2\2\u0105")
        buf.write("\u0106\7,\2\2\u0106>\3\2\2\2\u0107\u0108\7\61\2\2\u0108")
        buf.write("@\3\2\2\2\u0109\u010a\7\'\2\2\u010aB\3\2\2\2\u010b\u010c")
        buf.write("\7#\2\2\u010cD\3\2\2\2\u010d\u010e\7~\2\2\u010e\u010f")
        buf.write("\7~\2\2\u010fF\3\2\2\2\u0110\u0111\7(\2\2\u0111\u0112")
        buf.write("\7(\2\2\u0112H\3\2\2\2\u0113\u0114\7?\2\2\u0114\u0115")
        buf.write("\7?\2\2\u0115J\3\2\2\2\u0116\u0117\7#\2\2\u0117\u0118")
        buf.write("\7?\2\2\u0118L\3\2\2\2\u0119\u011a\7>\2\2\u011aN\3\2\2")
        buf.write("\2\u011b\u011c\7@\2\2\u011cP\3\2\2\2\u011d\u011e\7>\2")
        buf.write("\2\u011e\u011f\7?\2\2\u011fR\3\2\2\2\u0120\u0121\7@\2")
        buf.write("\2\u0121\u0122\7?\2\2\u0122T\3\2\2\2\u0123\u0124\7?\2")
        buf.write("\2\u0124V\3\2\2\2\u0125\u0126\7*\2\2\u0126X\3\2\2\2\u0127")
        buf.write("\u0128\7+\2\2\u0128Z\3\2\2\2\u0129\u012a\7}\2\2\u012a")
        buf.write("\\\3\2\2\2\u012b\u012c\7\177\2\2\u012c^\3\2\2\2\u012d")
        buf.write("\u012e\7]\2\2\u012e`\3\2\2\2\u012f\u0130\7_\2\2\u0130")
        buf.write("b\3\2\2\2\u0131\u0132\7.\2\2\u0132d\3\2\2\2\u0133\u0134")
        buf.write("\7=\2\2\u0134f\3\2\2\2\u0135\u0137\t\2\2\2\u0136\u0135")
        buf.write("\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u0136\3\2\2\2\u0138")
        buf.write("\u0139\3\2\2\2\u0139h\3\2\2\2\u013a\u013c\5\5\3\2\u013b")
        buf.write("\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013b\3\2\2\2")
        buf.write("\u013d\u013e\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0143\5")
        buf.write("\23\n\2\u0140\u0142\5\5\3\2\u0141\u0140\3\2\2\2\u0142")
        buf.write("\u0145\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2")
        buf.write("\u0144\u0147\3\2\2\2\u0145\u0143\3\2\2\2\u0146\u0148\5")
        buf.write("\27\f\2\u0147\u0146\3\2\2\2\u0147\u0148\3\2\2\2\u0148")
        buf.write("\u0160\3\2\2\2\u0149\u014b\5\5\3\2\u014a\u0149\3\2\2\2")
        buf.write("\u014b\u014e\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d\3")
        buf.write("\2\2\2\u014d\u014f\3\2\2\2\u014e\u014c\3\2\2\2\u014f\u0151")
        buf.write("\5\23\n\2\u0150\u0152\5\5\3\2\u0151\u0150\3\2\2\2\u0152")
        buf.write("\u0153\3\2\2\2\u0153\u0151\3\2\2\2\u0153\u0154\3\2\2\2")
        buf.write("\u0154\u0156\3\2\2\2\u0155\u0157\5\27\f\2\u0156\u0155")
        buf.write("\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0160\3\2\2\2\u0158")
        buf.write("\u015a\5\5\3\2\u0159\u0158\3\2\2\2\u015a\u015b\3\2\2\2")
        buf.write("\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015d\3")
        buf.write("\2\2\2\u015d\u015e\5\27\f\2\u015e\u0160\3\2\2\2\u015f")
        buf.write("\u013b\3\2\2\2\u015f\u014c\3\2\2\2\u015f\u0159\3\2\2\2")
        buf.write("\u0160j\3\2\2\2\u0161\u0164\5\63\32\2\u0162\u0164\5\65")
        buf.write("\33\2\u0163\u0161\3\2\2\2\u0163\u0162\3\2\2\2\u0164l\3")
        buf.write("\2\2\2\u0165\u0169\7$\2\2\u0166\u0168\5\r\7\2\u0167\u0166")
        buf.write("\3\2\2\2\u0168\u016b\3\2\2\2\u0169\u0167\3\2\2\2\u0169")
        buf.write("\u016a\3\2\2\2\u016a\u016c\3\2\2\2\u016b\u0169\3\2\2\2")
        buf.write("\u016c\u016d\7$\2\2\u016d\u016e\b\67\2\2\u016en\3\2\2")
        buf.write("\2\u016f\u0170\7\61\2\2\u0170\u0171\7\61\2\2\u0171\u0175")
        buf.write("\3\2\2\2\u0172\u0174\n\b\2\2\u0173\u0172\3\2\2\2\u0174")
        buf.write("\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176\u0178\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u0179\b")
        buf.write("8\3\2\u0179p\3\2\2\2\u017a\u017b\7\61\2\2\u017b\u017f")
        buf.write("\7,\2\2\u017c\u017e\13\2\2\2\u017d\u017c\3\2\2\2\u017e")
        buf.write("\u0181\3\2\2\2\u017f\u0180\3\2\2\2\u017f\u017d\3\2\2\2")
        buf.write("\u0180\u0182\3\2\2\2\u0181\u017f\3\2\2\2\u0182\u0183\7")
        buf.write(",\2\2\u0183\u0184\7\61\2\2\u0184\u0185\3\2\2\2\u0185\u0186")
        buf.write("\b9\3\2\u0186r\3\2\2\2\u0187\u0189\t\t\2\2\u0188\u0187")
        buf.write("\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u0188\3\2\2\2\u018a")
        buf.write("\u018b\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018d\b:\3\2")
        buf.write("\u018dt\3\2\2\2\u018e\u0192\7$\2\2\u018f\u0191\5\r\7\2")
        buf.write("\u0190\u018f\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190\3")
        buf.write("\2\2\2\u0192\u0193\3\2\2\2\u0193\u0196\3\2\2\2\u0194\u0192")
        buf.write("\3\2\2\2\u0195\u0197\t\n\2\2\u0196\u0195\3\2\2\2\u0197")
        buf.write("\u0198\3\2\2\2\u0198\u0199\b;\4\2\u0199v\3\2\2\2\u019a")
        buf.write("\u019e\7$\2\2\u019b\u019d\5\r\7\2\u019c\u019b\3\2\2\2")
        buf.write("\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3")
        buf.write("\2\2\2\u019f\u01a1\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1\u01a2")
        buf.write("\5\21\t\2\u01a2\u01a3\b<\5\2\u01a3x\3\2\2\2\u01a4\u01a5")
        buf.write("\13\2\2\2\u01a5\u01a6\b=\6\2\u01a6z\3\2\2\2\33\2\u0088")
        buf.write("\u008c\u009a\u009f\u00f7\u00fc\u00fe\u0138\u013d\u0143")
        buf.write("\u0147\u014c\u0153\u0156\u015b\u015f\u0163\u0169\u0175")
        buf.write("\u017f\u018a\u0192\u0196\u019e\7\3\67\2\b\2\2\3;\3\3<")
        buf.write("\4\3=\5")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    BOOLEANTYPE = 2
    INTTYPE = 3
    FLOATTYPE = 4
    STRINGTYPE = 5
    VOIDTYPE = 6
    DO = 7
    WHILE = 8
    FOR = 9
    BREAK = 10
    CONTINUE = 11
    IF = 12
    ELSE = 13
    RETURN = 14
    TRUE = 15
    FALSE = 16
    ID = 17
    ADD = 18
    SUB = 19
    MUL = 20
    DIV = 21
    MOD = 22
    NOT = 23
    OR = 24
    AND = 25
    EQUAL = 26
    NOT_EQUAL = 27
    LT = 28
    GT = 29
    LE = 30
    GE = 31
    ASSIGN = 32
    LB = 33
    RB = 34
    LP = 35
    RP = 36
    LSB = 37
    RSB = 38
    COMA = 39
    SEMI = 40
    INTLIT = 41
    FLOATLIT = 42
    BOOLEANLIT = 43
    STRINGLIT = 44
    CMTLINE = 45
    CMTBLOCK = 46
    WS = 47
    UNCLOSE_STRING = 48
    ILLEGAL_ESCAPE = 49
    ERROR_CHAR = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'boolean'", "'int'", "'float'", "'string'", "'void'", 
            "'do'", "'while'", "'for'", "'break'", "'continue'", "'if'", 
            "'else'", "'return'", "'true'", "'false'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'!'", "'||'", "'&&'", "'=='", "'!='", "'<'", 
            "'>'", "'<='", "'>='", "'='", "'('", "')'", "'{'", "'}'", "'['", 
            "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLEANTYPE", "INTTYPE", "FLOATTYPE", "STRINGTYPE", "VOIDTYPE", 
            "DO", "WHILE", "FOR", "BREAK", "CONTINUE", "IF", "ELSE", "RETURN", 
            "TRUE", "FALSE", "ID", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
            "OR", "AND", "EQUAL", "NOT_EQUAL", "LT", "GT", "LE", "GE", "ASSIGN", 
            "LB", "RB", "LP", "RP", "LSB", "RSB", "COMA", "SEMI", "INTLIT", 
            "FLOATLIT", "BOOLEANLIT", "STRINGLIT", "CMTLINE", "CMTBLOCK", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "Digit", "Lowcase", "Uppercase", "Letter", "Character", 
                  "Escape", "IllegalEscape", "Dot", "Underscore", "Exponent", 
                  "BOOLEANTYPE", "INTTYPE", "FLOATTYPE", "STRINGTYPE", "VOIDTYPE", 
                  "DO", "WHILE", "FOR", "BREAK", "CONTINUE", "IF", "ELSE", 
                  "RETURN", "TRUE", "FALSE", "ID", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "NOT", "OR", "AND", "EQUAL", "NOT_EQUAL", 
                  "LT", "GT", "LE", "GE", "ASSIGN", "LB", "RB", "LP", "RP", 
                  "LSB", "RSB", "COMA", "SEMI", "INTLIT", "FLOATLIT", "BOOLEANLIT", 
                  "STRINGLIT", "CMTLINE", "CMTBLOCK", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[53] = self.STRINGLIT_action 
            actions[57] = self.UNCLOSE_STRING_action 
            actions[58] = self.ILLEGAL_ESCAPE_action 
            actions[59] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                temp = str(self.text)
                self.text = temp[1:-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                esc = ['\b', '\t', '\n', '\f', '\r', '"', '\\']
                temp = str(self.text)

                if temp[-1] in esc:
                    raise UncloseString(temp[1:-1])
                else :
                    raise UncloseString(temp[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                temp = str(self.text)
                raise IllegalEscape(temp[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise ErrorToken(self.text)

     


