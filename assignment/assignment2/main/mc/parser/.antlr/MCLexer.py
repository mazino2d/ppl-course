# Generated from /home/kraken/ppl-course/assignment/assignment2/main/mc/parser/MC.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u01a0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\5\5\u0082")
        buf.write("\n\5\3\6\3\6\5\6\u0086\n\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\3\13\3\13\5\13\u0094\n\13\3\13\6\13\u0097")
        buf.write("\n\13\r\13\16\13\u0098\3\f\6\f\u009c\n\f\r\f\16\f\u009d")
        buf.write("\3\r\6\r\u00a1\n\r\r\r\16\r\u00a2\3\r\3\r\7\r\u00a7\n")
        buf.write("\r\f\r\16\r\u00aa\13\r\3\r\5\r\u00ad\n\r\3\r\7\r\u00b0")
        buf.write("\n\r\f\r\16\r\u00b3\13\r\3\r\3\r\6\r\u00b7\n\r\r\r\16")
        buf.write("\r\u00b8\3\r\5\r\u00bc\n\r\3\r\6\r\u00bf\n\r\r\r\16\r")
        buf.write("\u00c0\3\r\3\r\5\r\u00c5\n\r\3\16\3\16\5\16\u00c9\n\16")
        buf.write("\3\17\3\17\7\17\u00cd\n\17\f\17\16\17\u00d0\13\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\5\37\u012b\n\37\3\37\3\37\3\37\7\37\u0130\n\37\f\37\16")
        buf.write("\37\u0133\13\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%")
        buf.write("\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3")
        buf.write(",\3,\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\7\67\u016d\n\67\f\67\16\67\u0170\13\67\3\67")
        buf.write("\3\67\38\38\38\78\u0177\n8\f8\168\u017a\138\38\38\38\3")
        buf.write("8\38\39\69\u0182\n9\r9\169\u0183\39\39\3:\3:\7:\u018a")
        buf.write("\n:\f:\16:\u018d\13:\3:\5:\u0190\n:\3:\3:\3;\3;\7;\u0196")
        buf.write("\n;\f;\16;\u0199\13;\3;\3;\3;\3<\3<\3<\3\u0178\2=\3\2")
        buf.write("\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\3\31\4\33")
        buf.write("\5\35\6\37\7!\b#\t%\n\'\13)\f+\r-\16/\17\61\20\63\21\65")
        buf.write("\22\67\239\24;\25=\26?\27A\30C\31E\32G\33I\34K\35M\36")
        buf.write("O\37Q S!U\"W#Y$[%]&_\'a(c)e*g+i,k-m.o/q\60s\61u\62w\63")
        buf.write("\3\2\13\3\2\62;\3\2c|\3\2C\\\6\2\n\f\16\17$$^^\t\2$$^")
        buf.write("^ddhhppttvv\4\2GGgg\4\2\f\f\16\17\5\2\13\f\16\17\"\"\5")
        buf.write("\3\n\f\16\17^^\2\u01ae\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2")
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\3y\3\2")
        buf.write("\2\2\5{\3\2\2\2\7}\3\2\2\2\t\u0081\3\2\2\2\13\u0085\3")
        buf.write("\2\2\2\r\u0087\3\2\2\2\17\u008a\3\2\2\2\21\u008d\3\2\2")
        buf.write("\2\23\u008f\3\2\2\2\25\u0091\3\2\2\2\27\u009b\3\2\2\2")
        buf.write("\31\u00c4\3\2\2\2\33\u00c8\3\2\2\2\35\u00ca\3\2\2\2\37")
        buf.write("\u00d4\3\2\2\2!\u00dc\3\2\2\2#\u00e0\3\2\2\2%\u00e6\3")
        buf.write("\2\2\2\'\u00ed\3\2\2\2)\u00f2\3\2\2\2+\u00f5\3\2\2\2-")
        buf.write("\u00fb\3\2\2\2/\u00ff\3\2\2\2\61\u0105\3\2\2\2\63\u010e")
        buf.write("\3\2\2\2\65\u0111\3\2\2\2\67\u0116\3\2\2\29\u011d\3\2")
        buf.write("\2\2;\u0122\3\2\2\2=\u012a\3\2\2\2?\u0134\3\2\2\2A\u0136")
        buf.write("\3\2\2\2C\u0138\3\2\2\2E\u013a\3\2\2\2G\u013c\3\2\2\2")
        buf.write("I\u013e\3\2\2\2K\u0140\3\2\2\2M\u0143\3\2\2\2O\u0146\3")
        buf.write("\2\2\2Q\u0149\3\2\2\2S\u014c\3\2\2\2U\u014e\3\2\2\2W\u0150")
        buf.write("\3\2\2\2Y\u0153\3\2\2\2[\u0156\3\2\2\2]\u0158\3\2\2\2")
        buf.write("_\u015a\3\2\2\2a\u015c\3\2\2\2c\u015e\3\2\2\2e\u0160\3")
        buf.write("\2\2\2g\u0162\3\2\2\2i\u0164\3\2\2\2k\u0166\3\2\2\2m\u0168")
        buf.write("\3\2\2\2o\u0173\3\2\2\2q\u0181\3\2\2\2s\u0187\3\2\2\2")
        buf.write("u\u0193\3\2\2\2w\u019d\3\2\2\2yz\t\2\2\2z\4\3\2\2\2{|")
        buf.write("\t\3\2\2|\6\3\2\2\2}~\t\4\2\2~\b\3\2\2\2\177\u0082\5\5")
        buf.write("\3\2\u0080\u0082\5\7\4\2\u0081\177\3\2\2\2\u0081\u0080")
        buf.write("\3\2\2\2\u0082\n\3\2\2\2\u0083\u0086\n\5\2\2\u0084\u0086")
        buf.write("\5\r\7\2\u0085\u0083\3\2\2\2\u0085\u0084\3\2\2\2\u0086")
        buf.write("\f\3\2\2\2\u0087\u0088\7^\2\2\u0088\u0089\t\6\2\2\u0089")
        buf.write("\16\3\2\2\2\u008a\u008b\7^\2\2\u008b\u008c\n\6\2\2\u008c")
        buf.write("\20\3\2\2\2\u008d\u008e\7\60\2\2\u008e\22\3\2\2\2\u008f")
        buf.write("\u0090\7a\2\2\u0090\24\3\2\2\2\u0091\u0093\t\7\2\2\u0092")
        buf.write("\u0094\7/\2\2\u0093\u0092\3\2\2\2\u0093\u0094\3\2\2\2")
        buf.write("\u0094\u0096\3\2\2\2\u0095\u0097\5\3\2\2\u0096\u0095\3")
        buf.write("\2\2\2\u0097\u0098\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099")
        buf.write("\3\2\2\2\u0099\26\3\2\2\2\u009a\u009c\5\3\2\2\u009b\u009a")
        buf.write("\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009b\3\2\2\2\u009d")
        buf.write("\u009e\3\2\2\2\u009e\30\3\2\2\2\u009f\u00a1\5\3\2\2\u00a0")
        buf.write("\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a0\3\2\2\2")
        buf.write("\u00a2\u00a3\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a8\5")
        buf.write("\21\t\2\u00a5\u00a7\5\3\2\2\u00a6\u00a5\3\2\2\2\u00a7")
        buf.write("\u00aa\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2")
        buf.write("\u00a9\u00ac\3\2\2\2\u00aa\u00a8\3\2\2\2\u00ab\u00ad\5")
        buf.write("\25\13\2\u00ac\u00ab\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad")
        buf.write("\u00c5\3\2\2\2\u00ae\u00b0\5\3\2\2\u00af\u00ae\3\2\2\2")
        buf.write("\u00b0\u00b3\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3")
        buf.write("\2\2\2\u00b2\u00b4\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b6")
        buf.write("\5\21\t\2\u00b5\u00b7\5\3\2\2\u00b6\u00b5\3\2\2\2\u00b7")
        buf.write("\u00b8\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2")
        buf.write("\u00b9\u00bb\3\2\2\2\u00ba\u00bc\5\25\13\2\u00bb\u00ba")
        buf.write("\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00c5\3\2\2\2\u00bd")
        buf.write("\u00bf\5\3\2\2\u00be\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2")
        buf.write("\u00c0\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c2\3")
        buf.write("\2\2\2\u00c2\u00c3\5\25\13\2\u00c3\u00c5\3\2\2\2\u00c4")
        buf.write("\u00a0\3\2\2\2\u00c4\u00b1\3\2\2\2\u00c4\u00be\3\2\2\2")
        buf.write("\u00c5\32\3\2\2\2\u00c6\u00c9\59\35\2\u00c7\u00c9\5;\36")
        buf.write("\2\u00c8\u00c6\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9\34\3")
        buf.write("\2\2\2\u00ca\u00ce\7$\2\2\u00cb\u00cd\5\13\6\2\u00cc\u00cb")
        buf.write("\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce")
        buf.write("\u00cf\3\2\2\2\u00cf\u00d1\3\2\2\2\u00d0\u00ce\3\2\2\2")
        buf.write("\u00d1\u00d2\7$\2\2\u00d2\u00d3\b\17\2\2\u00d3\36\3\2")
        buf.write("\2\2\u00d4\u00d5\7d\2\2\u00d5\u00d6\7q\2\2\u00d6\u00d7")
        buf.write("\7q\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da")
        buf.write("\7c\2\2\u00da\u00db\7p\2\2\u00db \3\2\2\2\u00dc\u00dd")
        buf.write("\7k\2\2\u00dd\u00de\7p\2\2\u00de\u00df\7v\2\2\u00df\"")
        buf.write("\3\2\2\2\u00e0\u00e1\7h\2\2\u00e1\u00e2\7n\2\2\u00e2\u00e3")
        buf.write("\7q\2\2\u00e3\u00e4\7c\2\2\u00e4\u00e5\7v\2\2\u00e5$\3")
        buf.write("\2\2\2\u00e6\u00e7\7u\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9")
        buf.write("\7t\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec")
        buf.write("\7i\2\2\u00ec&\3\2\2\2\u00ed\u00ee\7x\2\2\u00ee\u00ef")
        buf.write("\7q\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1\7f\2\2\u00f1(\3")
        buf.write("\2\2\2\u00f2\u00f3\7f\2\2\u00f3\u00f4\7q\2\2\u00f4*\3")
        buf.write("\2\2\2\u00f5\u00f6\7y\2\2\u00f6\u00f7\7j\2\2\u00f7\u00f8")
        buf.write("\7k\2\2\u00f8\u00f9\7n\2\2\u00f9\u00fa\7g\2\2\u00fa,\3")
        buf.write("\2\2\2\u00fb\u00fc\7h\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe")
        buf.write("\7t\2\2\u00fe.\3\2\2\2\u00ff\u0100\7d\2\2\u0100\u0101")
        buf.write("\7t\2\2\u0101\u0102\7g\2\2\u0102\u0103\7c\2\2\u0103\u0104")
        buf.write("\7m\2\2\u0104\60\3\2\2\2\u0105\u0106\7e\2\2\u0106\u0107")
        buf.write("\7q\2\2\u0107\u0108\7p\2\2\u0108\u0109\7v\2\2\u0109\u010a")
        buf.write("\7k\2\2\u010a\u010b\7p\2\2\u010b\u010c\7w\2\2\u010c\u010d")
        buf.write("\7g\2\2\u010d\62\3\2\2\2\u010e\u010f\7k\2\2\u010f\u0110")
        buf.write("\7h\2\2\u0110\64\3\2\2\2\u0111\u0112\7g\2\2\u0112\u0113")
        buf.write("\7n\2\2\u0113\u0114\7u\2\2\u0114\u0115\7g\2\2\u0115\66")
        buf.write("\3\2\2\2\u0116\u0117\7t\2\2\u0117\u0118\7g\2\2\u0118\u0119")
        buf.write("\7v\2\2\u0119\u011a\7w\2\2\u011a\u011b\7t\2\2\u011b\u011c")
        buf.write("\7p\2\2\u011c8\3\2\2\2\u011d\u011e\7v\2\2\u011e\u011f")
        buf.write("\7t\2\2\u011f\u0120\7w\2\2\u0120\u0121\7g\2\2\u0121:\3")
        buf.write("\2\2\2\u0122\u0123\7h\2\2\u0123\u0124\7c\2\2\u0124\u0125")
        buf.write("\7n\2\2\u0125\u0126\7u\2\2\u0126\u0127\7g\2\2\u0127<\3")
        buf.write("\2\2\2\u0128\u012b\5\t\5\2\u0129\u012b\5\23\n\2\u012a")
        buf.write("\u0128\3\2\2\2\u012a\u0129\3\2\2\2\u012b\u0131\3\2\2\2")
        buf.write("\u012c\u0130\5\t\5\2\u012d\u0130\5\23\n\2\u012e\u0130")
        buf.write("\5\3\2\2\u012f\u012c\3\2\2\2\u012f\u012d\3\2\2\2\u012f")
        buf.write("\u012e\3\2\2\2\u0130\u0133\3\2\2\2\u0131\u012f\3\2\2\2")
        buf.write("\u0131\u0132\3\2\2\2\u0132>\3\2\2\2\u0133\u0131\3\2\2")
        buf.write("\2\u0134\u0135\7-\2\2\u0135@\3\2\2\2\u0136\u0137\7/\2")
        buf.write("\2\u0137B\3\2\2\2\u0138\u0139\7,\2\2\u0139D\3\2\2\2\u013a")
        buf.write("\u013b\7\61\2\2\u013bF\3\2\2\2\u013c\u013d\7\'\2\2\u013d")
        buf.write("H\3\2\2\2\u013e\u013f\7#\2\2\u013fJ\3\2\2\2\u0140\u0141")
        buf.write("\7~\2\2\u0141\u0142\7~\2\2\u0142L\3\2\2\2\u0143\u0144")
        buf.write("\7(\2\2\u0144\u0145\7(\2\2\u0145N\3\2\2\2\u0146\u0147")
        buf.write("\7?\2\2\u0147\u0148\7?\2\2\u0148P\3\2\2\2\u0149\u014a")
        buf.write("\7#\2\2\u014a\u014b\7?\2\2\u014bR\3\2\2\2\u014c\u014d")
        buf.write("\7>\2\2\u014dT\3\2\2\2\u014e\u014f\7@\2\2\u014fV\3\2\2")
        buf.write("\2\u0150\u0151\7>\2\2\u0151\u0152\7?\2\2\u0152X\3\2\2")
        buf.write("\2\u0153\u0154\7@\2\2\u0154\u0155\7?\2\2\u0155Z\3\2\2")
        buf.write("\2\u0156\u0157\7?\2\2\u0157\\\3\2\2\2\u0158\u0159\7*\2")
        buf.write("\2\u0159^\3\2\2\2\u015a\u015b\7+\2\2\u015b`\3\2\2\2\u015c")
        buf.write("\u015d\7}\2\2\u015db\3\2\2\2\u015e\u015f\7\177\2\2\u015f")
        buf.write("d\3\2\2\2\u0160\u0161\7]\2\2\u0161f\3\2\2\2\u0162\u0163")
        buf.write("\7_\2\2\u0163h\3\2\2\2\u0164\u0165\7.\2\2\u0165j\3\2\2")
        buf.write("\2\u0166\u0167\7=\2\2\u0167l\3\2\2\2\u0168\u0169\7\61")
        buf.write("\2\2\u0169\u016a\7\61\2\2\u016a\u016e\3\2\2\2\u016b\u016d")
        buf.write("\n\b\2\2\u016c\u016b\3\2\2\2\u016d\u0170\3\2\2\2\u016e")
        buf.write("\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0171\3\2\2\2")
        buf.write("\u0170\u016e\3\2\2\2\u0171\u0172\b\67\3\2\u0172n\3\2\2")
        buf.write("\2\u0173\u0174\7\61\2\2\u0174\u0178\7,\2\2\u0175\u0177")
        buf.write("\13\2\2\2\u0176\u0175\3\2\2\2\u0177\u017a\3\2\2\2\u0178")
        buf.write("\u0179\3\2\2\2\u0178\u0176\3\2\2\2\u0179\u017b\3\2\2\2")
        buf.write("\u017a\u0178\3\2\2\2\u017b\u017c\7,\2\2\u017c\u017d\7")
        buf.write("\61\2\2\u017d\u017e\3\2\2\2\u017e\u017f\b8\3\2\u017fp")
        buf.write("\3\2\2\2\u0180\u0182\t\t\2\2\u0181\u0180\3\2\2\2\u0182")
        buf.write("\u0183\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2")
        buf.write("\u0184\u0185\3\2\2\2\u0185\u0186\b9\3\2\u0186r\3\2\2\2")
        buf.write("\u0187\u018b\7$\2\2\u0188\u018a\5\13\6\2\u0189\u0188\3")
        buf.write("\2\2\2\u018a\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c")
        buf.write("\3\2\2\2\u018c\u018f\3\2\2\2\u018d\u018b\3\2\2\2\u018e")
        buf.write("\u0190\t\n\2\2\u018f\u018e\3\2\2\2\u0190\u0191\3\2\2\2")
        buf.write("\u0191\u0192\b:\4\2\u0192t\3\2\2\2\u0193\u0197\7$\2\2")
        buf.write("\u0194\u0196\5\13\6\2\u0195\u0194\3\2\2\2\u0196\u0199")
        buf.write("\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198")
        buf.write("\u019a\3\2\2\2\u0199\u0197\3\2\2\2\u019a\u019b\5\17\b")
        buf.write("\2\u019b\u019c\b;\5\2\u019cv\3\2\2\2\u019d\u019e\13\2")
        buf.write("\2\2\u019e\u019f\b<\6\2\u019fx\3\2\2\2\33\2\u0081\u0085")
        buf.write("\u0093\u0098\u009d\u00a2\u00a8\u00ac\u00b1\u00b8\u00bb")
        buf.write("\u00c0\u00c4\u00c8\u00ce\u012a\u012f\u0131\u016e\u0178")
        buf.write("\u0183\u018b\u018f\u0197\7\3\17\2\b\2\2\3:\3\3;\4\3<\5")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTLIT = 1
    FLOATLIT = 2
    BOOLEANLIT = 3
    STRINGLIT = 4
    BOOLEANTYPE = 5
    INTTYPE = 6
    FLOATTYPE = 7
    STRINGTYPE = 8
    VOIDTYPE = 9
    DO = 10
    WHILE = 11
    FOR = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    RETURN = 17
    TRUE = 18
    FALSE = 19
    ID = 20
    ADD = 21
    SUB = 22
    MUL = 23
    DIV = 24
    MOD = 25
    NOT = 26
    OR = 27
    AND = 28
    EQ = 29
    NE = 30
    LT = 31
    GT = 32
    LE = 33
    GE = 34
    ASSIGN = 35
    LB = 36
    RB = 37
    LP = 38
    RP = 39
    LSB = 40
    RSB = 41
    COMA = 42
    SEMI = 43
    CMTLINE = 44
    CMTBLOCK = 45
    WS = 46
    UNCLOSE_STRING = 47
    ILLEGAL_ESCAPE = 48
    ERROR_CHAR = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'int'", "'float'", "'string'", "'void'", "'do'", 
            "'while'", "'for'", "'break'", "'continue'", "'if'", "'else'", 
            "'return'", "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'||'", "'&&'", "'=='", "'!='", "'<'", "'>'", 
            "'<='", "'>='", "'='", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", "BOOLEANTYPE", 
            "INTTYPE", "FLOATTYPE", "STRINGTYPE", "VOIDTYPE", "DO", "WHILE", 
            "FOR", "BREAK", "CONTINUE", "IF", "ELSE", "RETURN", "TRUE", 
            "FALSE", "ID", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "OR", 
            "AND", "EQ", "NE", "LT", "GT", "LE", "GE", "ASSIGN", "LB", "RB", 
            "LP", "RP", "LSB", "RSB", "COMA", "SEMI", "CMTLINE", "CMTBLOCK", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "Digit", "Lowcase", "Uppercase", "Letter", "Character", 
                  "Escape", "IllegalEscape", "Dot", "Underscore", "Exponent", 
                  "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", "BOOLEANTYPE", 
                  "INTTYPE", "FLOATTYPE", "STRINGTYPE", "VOIDTYPE", "DO", 
                  "WHILE", "FOR", "BREAK", "CONTINUE", "IF", "ELSE", "RETURN", 
                  "TRUE", "FALSE", "ID", "ADD", "SUB", "MUL", "DIV", "MOD", 
                  "NOT", "OR", "AND", "EQ", "NE", "LT", "GT", "LE", "GE", 
                  "ASSIGN", "LB", "RB", "LP", "RP", "LSB", "RSB", "COMA", 
                  "SEMI", "CMTLINE", "CMTBLOCK", "WS", "UNCLOSE_STRING", 
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
            actions[13] = self.STRINGLIT_action 
            actions[56] = self.UNCLOSE_STRING_action 
            actions[57] = self.ILLEGAL_ESCAPE_action 
            actions[58] = self.ERROR_CHAR_action 
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

                esc = ['\b', '\t', '\n', '\f', '\r', '\\']
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

     


