# Generated from /home/kraken/ppl-course/assignment/assignment1/main/mc/parser/MC.g4 by ANTLR 4.7.1
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
        buf.write("\n\13\r\13\16\13\u0098\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\5\33\u00f1\n\33\3\33\3\33\3\33\7\33\u00f6\n\33\f")
        buf.write("\33\16\33\u00f9\13\33\3\34\3\34\3\35\3\35\3\36\3\36\3")
        buf.write("\37\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%")
        buf.write("\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3,")
        buf.write("\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3")
        buf.write("\63\6\63\u0130\n\63\r\63\16\63\u0131\3\64\6\64\u0135\n")
        buf.write("\64\r\64\16\64\u0136\3\64\3\64\7\64\u013b\n\64\f\64\16")
        buf.write("\64\u013e\13\64\3\64\5\64\u0141\n\64\3\64\7\64\u0144\n")
        buf.write("\64\f\64\16\64\u0147\13\64\3\64\3\64\6\64\u014b\n\64\r")
        buf.write("\64\16\64\u014c\3\64\5\64\u0150\n\64\3\64\6\64\u0153\n")
        buf.write("\64\r\64\16\64\u0154\3\64\3\64\5\64\u0159\n\64\3\65\3")
        buf.write("\65\5\65\u015d\n\65\3\66\3\66\7\66\u0161\n\66\f\66\16")
        buf.write("\66\u0164\13\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\7\67")
        buf.write("\u016d\n\67\f\67\16\67\u0170\13\67\3\67\3\67\38\38\38")
        buf.write("\78\u0177\n8\f8\168\u017a\138\38\38\38\38\38\39\69\u0182")
        buf.write("\n9\r9\169\u0183\39\39\3:\3:\7:\u018a\n:\f:\16:\u018d")
        buf.write("\13:\3:\5:\u0190\n:\3:\3:\3;\3;\7;\u0196\n;\f;\16;\u0199")
        buf.write("\13;\3;\3;\3;\3<\3<\3<\3\u0178\2=\3\2\5\2\7\2\t\2\13\2")
        buf.write("\r\2\17\2\21\2\23\2\25\2\27\3\31\4\33\5\35\6\37\7!\b#")
        buf.write("\t%\n\'\13)\f+\r-\16/\17\61\20\63\21\65\22\67\239\24;")
        buf.write("\25=\26?\27A\30C\31E\32G\33I\34K\35M\36O\37Q S!U\"W#Y")
        buf.write("$[%]&_\'a(c)e*g+i,k-m.o/q\60s\61u\62w\63\3\2\13\3\2\62")
        buf.write(";\3\2c|\3\2C\\\6\2\n\f\16\17$$^^\t\2$$^^ddhhppttvv\4\2")
        buf.write("GGgg\4\2\f\f\16\17\5\2\13\f\17\17\"\"\6\3\n\f\16\17$$")
        buf.write("^^\2\u01ae\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\3y\3\2\2\2\5{\3\2\2")
        buf.write("\2\7}\3\2\2\2\t\u0081\3\2\2\2\13\u0085\3\2\2\2\r\u0087")
        buf.write("\3\2\2\2\17\u008a\3\2\2\2\21\u008d\3\2\2\2\23\u008f\3")
        buf.write("\2\2\2\25\u0091\3\2\2\2\27\u009a\3\2\2\2\31\u00a2\3\2")
        buf.write("\2\2\33\u00a6\3\2\2\2\35\u00ac\3\2\2\2\37\u00b3\3\2\2")
        buf.write("\2!\u00b8\3\2\2\2#\u00bb\3\2\2\2%\u00c1\3\2\2\2\'\u00c5")
        buf.write("\3\2\2\2)\u00cb\3\2\2\2+\u00d4\3\2\2\2-\u00d7\3\2\2\2")
        buf.write("/\u00dc\3\2\2\2\61\u00e3\3\2\2\2\63\u00e8\3\2\2\2\65\u00f0")
        buf.write("\3\2\2\2\67\u00fa\3\2\2\29\u00fc\3\2\2\2;\u00fe\3\2\2")
        buf.write("\2=\u0100\3\2\2\2?\u0102\3\2\2\2A\u0104\3\2\2\2C\u0106")
        buf.write("\3\2\2\2E\u0109\3\2\2\2G\u010c\3\2\2\2I\u010f\3\2\2\2")
        buf.write("K\u0112\3\2\2\2M\u0114\3\2\2\2O\u0116\3\2\2\2Q\u0119\3")
        buf.write("\2\2\2S\u011c\3\2\2\2U\u011e\3\2\2\2W\u0120\3\2\2\2Y\u0122")
        buf.write("\3\2\2\2[\u0124\3\2\2\2]\u0126\3\2\2\2_\u0128\3\2\2\2")
        buf.write("a\u012a\3\2\2\2c\u012c\3\2\2\2e\u012f\3\2\2\2g\u0158\3")
        buf.write("\2\2\2i\u015c\3\2\2\2k\u015e\3\2\2\2m\u0168\3\2\2\2o\u0173")
        buf.write("\3\2\2\2q\u0181\3\2\2\2s\u0187\3\2\2\2u\u0193\3\2\2\2")
        buf.write("w\u019d\3\2\2\2yz\t\2\2\2z\4\3\2\2\2{|\t\3\2\2|\6\3\2")
        buf.write("\2\2}~\t\4\2\2~\b\3\2\2\2\177\u0082\5\5\3\2\u0080\u0082")
        buf.write("\5\7\4\2\u0081\177\3\2\2\2\u0081\u0080\3\2\2\2\u0082\n")
        buf.write("\3\2\2\2\u0083\u0086\n\5\2\2\u0084\u0086\5\r\7\2\u0085")
        buf.write("\u0083\3\2\2\2\u0085\u0084\3\2\2\2\u0086\f\3\2\2\2\u0087")
        buf.write("\u0088\7^\2\2\u0088\u0089\t\6\2\2\u0089\16\3\2\2\2\u008a")
        buf.write("\u008b\7^\2\2\u008b\u008c\n\6\2\2\u008c\20\3\2\2\2\u008d")
        buf.write("\u008e\7\60\2\2\u008e\22\3\2\2\2\u008f\u0090\7a\2\2\u0090")
        buf.write("\24\3\2\2\2\u0091\u0093\t\7\2\2\u0092\u0094\7/\2\2\u0093")
        buf.write("\u0092\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0096\3\2\2\2")
        buf.write("\u0095\u0097\5\3\2\2\u0096\u0095\3\2\2\2\u0097\u0098\3")
        buf.write("\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\26")
        buf.write("\3\2\2\2\u009a\u009b\7d\2\2\u009b\u009c\7q\2\2\u009c\u009d")
        buf.write("\7q\2\2\u009d\u009e\7n\2\2\u009e\u009f\7g\2\2\u009f\u00a0")
        buf.write("\7c\2\2\u00a0\u00a1\7p\2\2\u00a1\30\3\2\2\2\u00a2\u00a3")
        buf.write("\7k\2\2\u00a3\u00a4\7p\2\2\u00a4\u00a5\7v\2\2\u00a5\32")
        buf.write("\3\2\2\2\u00a6\u00a7\7h\2\2\u00a7\u00a8\7n\2\2\u00a8\u00a9")
        buf.write("\7q\2\2\u00a9\u00aa\7c\2\2\u00aa\u00ab\7v\2\2\u00ab\34")
        buf.write("\3\2\2\2\u00ac\u00ad\7u\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af")
        buf.write("\7t\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2")
        buf.write("\7i\2\2\u00b2\36\3\2\2\2\u00b3\u00b4\7x\2\2\u00b4\u00b5")
        buf.write("\7q\2\2\u00b5\u00b6\7k\2\2\u00b6\u00b7\7f\2\2\u00b7 \3")
        buf.write("\2\2\2\u00b8\u00b9\7f\2\2\u00b9\u00ba\7q\2\2\u00ba\"\3")
        buf.write("\2\2\2\u00bb\u00bc\7y\2\2\u00bc\u00bd\7j\2\2\u00bd\u00be")
        buf.write("\7k\2\2\u00be\u00bf\7n\2\2\u00bf\u00c0\7g\2\2\u00c0$\3")
        buf.write("\2\2\2\u00c1\u00c2\7h\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4")
        buf.write("\7t\2\2\u00c4&\3\2\2\2\u00c5\u00c6\7d\2\2\u00c6\u00c7")
        buf.write("\7t\2\2\u00c7\u00c8\7g\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca")
        buf.write("\7m\2\2\u00ca(\3\2\2\2\u00cb\u00cc\7e\2\2\u00cc\u00cd")
        buf.write("\7q\2\2\u00cd\u00ce\7p\2\2\u00ce\u00cf\7v\2\2\u00cf\u00d0")
        buf.write("\7k\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2\7w\2\2\u00d2\u00d3")
        buf.write("\7g\2\2\u00d3*\3\2\2\2\u00d4\u00d5\7k\2\2\u00d5\u00d6")
        buf.write("\7h\2\2\u00d6,\3\2\2\2\u00d7\u00d8\7g\2\2\u00d8\u00d9")
        buf.write("\7n\2\2\u00d9\u00da\7u\2\2\u00da\u00db\7g\2\2\u00db.\3")
        buf.write("\2\2\2\u00dc\u00dd\7t\2\2\u00dd\u00de\7g\2\2\u00de\u00df")
        buf.write("\7v\2\2\u00df\u00e0\7w\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2")
        buf.write("\7p\2\2\u00e2\60\3\2\2\2\u00e3\u00e4\7v\2\2\u00e4\u00e5")
        buf.write("\7t\2\2\u00e5\u00e6\7w\2\2\u00e6\u00e7\7g\2\2\u00e7\62")
        buf.write("\3\2\2\2\u00e8\u00e9\7h\2\2\u00e9\u00ea\7c\2\2\u00ea\u00eb")
        buf.write("\7n\2\2\u00eb\u00ec\7u\2\2\u00ec\u00ed\7g\2\2\u00ed\64")
        buf.write("\3\2\2\2\u00ee\u00f1\5\t\5\2\u00ef\u00f1\5\23\n\2\u00f0")
        buf.write("\u00ee\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1\u00f7\3\2\2\2")
        buf.write("\u00f2\u00f6\5\t\5\2\u00f3\u00f6\5\23\n\2\u00f4\u00f6")
        buf.write("\5\3\2\2\u00f5\u00f2\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5")
        buf.write("\u00f4\3\2\2\2\u00f6\u00f9\3\2\2\2\u00f7\u00f5\3\2\2\2")
        buf.write("\u00f7\u00f8\3\2\2\2\u00f8\66\3\2\2\2\u00f9\u00f7\3\2")
        buf.write("\2\2\u00fa\u00fb\7-\2\2\u00fb8\3\2\2\2\u00fc\u00fd\7/")
        buf.write("\2\2\u00fd:\3\2\2\2\u00fe\u00ff\7,\2\2\u00ff<\3\2\2\2")
        buf.write("\u0100\u0101\7\61\2\2\u0101>\3\2\2\2\u0102\u0103\7\'\2")
        buf.write("\2\u0103@\3\2\2\2\u0104\u0105\7#\2\2\u0105B\3\2\2\2\u0106")
        buf.write("\u0107\7~\2\2\u0107\u0108\7~\2\2\u0108D\3\2\2\2\u0109")
        buf.write("\u010a\7(\2\2\u010a\u010b\7(\2\2\u010bF\3\2\2\2\u010c")
        buf.write("\u010d\7?\2\2\u010d\u010e\7?\2\2\u010eH\3\2\2\2\u010f")
        buf.write("\u0110\7#\2\2\u0110\u0111\7?\2\2\u0111J\3\2\2\2\u0112")
        buf.write("\u0113\7>\2\2\u0113L\3\2\2\2\u0114\u0115\7@\2\2\u0115")
        buf.write("N\3\2\2\2\u0116\u0117\7>\2\2\u0117\u0118\7?\2\2\u0118")
        buf.write("P\3\2\2\2\u0119\u011a\7@\2\2\u011a\u011b\7?\2\2\u011b")
        buf.write("R\3\2\2\2\u011c\u011d\7?\2\2\u011dT\3\2\2\2\u011e\u011f")
        buf.write("\7*\2\2\u011fV\3\2\2\2\u0120\u0121\7+\2\2\u0121X\3\2\2")
        buf.write("\2\u0122\u0123\7}\2\2\u0123Z\3\2\2\2\u0124\u0125\7\177")
        buf.write("\2\2\u0125\\\3\2\2\2\u0126\u0127\7]\2\2\u0127^\3\2\2\2")
        buf.write("\u0128\u0129\7_\2\2\u0129`\3\2\2\2\u012a\u012b\7.\2\2")
        buf.write("\u012bb\3\2\2\2\u012c\u012d\7=\2\2\u012dd\3\2\2\2\u012e")
        buf.write("\u0130\5\3\2\2\u012f\u012e\3\2\2\2\u0130\u0131\3\2\2\2")
        buf.write("\u0131\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132f\3\2\2")
        buf.write("\2\u0133\u0135\5\3\2\2\u0134\u0133\3\2\2\2\u0135\u0136")
        buf.write("\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137")
        buf.write("\u0138\3\2\2\2\u0138\u013c\5\21\t\2\u0139\u013b\5\3\2")
        buf.write("\2\u013a\u0139\3\2\2\2\u013b\u013e\3\2\2\2\u013c\u013a")
        buf.write("\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u0140\3\2\2\2\u013e")
        buf.write("\u013c\3\2\2\2\u013f\u0141\5\25\13\2\u0140\u013f\3\2\2")
        buf.write("\2\u0140\u0141\3\2\2\2\u0141\u0159\3\2\2\2\u0142\u0144")
        buf.write("\5\3\2\2\u0143\u0142\3\2\2\2\u0144\u0147\3\2\2\2\u0145")
        buf.write("\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0148\3\2\2\2")
        buf.write("\u0147\u0145\3\2\2\2\u0148\u014a\5\21\t\2\u0149\u014b")
        buf.write("\5\3\2\2\u014a\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c")
        buf.write("\u014a\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014f\3\2\2\2")
        buf.write("\u014e\u0150\5\25\13\2\u014f\u014e\3\2\2\2\u014f\u0150")
        buf.write("\3\2\2\2\u0150\u0159\3\2\2\2\u0151\u0153\5\3\2\2\u0152")
        buf.write("\u0151\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0152\3\2\2\2")
        buf.write("\u0154\u0155\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0157\5")
        buf.write("\25\13\2\u0157\u0159\3\2\2\2\u0158\u0134\3\2\2\2\u0158")
        buf.write("\u0145\3\2\2\2\u0158\u0152\3\2\2\2\u0159h\3\2\2\2\u015a")
        buf.write("\u015d\5\61\31\2\u015b\u015d\5\63\32\2\u015c\u015a\3\2")
        buf.write("\2\2\u015c\u015b\3\2\2\2\u015dj\3\2\2\2\u015e\u0162\7")
        buf.write("$\2\2\u015f\u0161\5\13\6\2\u0160\u015f\3\2\2\2\u0161\u0164")
        buf.write("\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163")
        buf.write("\u0165\3\2\2\2\u0164\u0162\3\2\2\2\u0165\u0166\7$\2\2")
        buf.write("\u0166\u0167\b\66\2\2\u0167l\3\2\2\2\u0168\u0169\7\61")
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
        buf.write("\u0093\u0098\u00f0\u00f5\u00f7\u0131\u0136\u013c\u0140")
        buf.write("\u0145\u014c\u014f\u0154\u0158\u015c\u0162\u016e\u0178")
        buf.write("\u0183\u018b\u018f\u0197\7\3\66\2\b\2\2\3:\3\3;\4\3<\5")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLEANTYPE = 1
    INTTYPE = 2
    FLOATTYPE = 3
    STRINGTYPE = 4
    VOIDTYPE = 5
    DO = 6
    WHILE = 7
    FOR = 8
    BREAK = 9
    CONTINUE = 10
    IF = 11
    ELSE = 12
    RETURN = 13
    TRUE = 14
    FALSE = 15
    ID = 16
    ADD = 17
    SUB = 18
    MUL = 19
    DIV = 20
    MOD = 21
    NOT = 22
    OR = 23
    AND = 24
    EQ = 25
    NE = 26
    LT = 27
    GT = 28
    LE = 29
    GE = 30
    ASSIGN = 31
    LB = 32
    RB = 33
    LP = 34
    RP = 35
    LSB = 36
    RSB = 37
    COMA = 38
    SEMI = 39
    INTLIT = 40
    FLOATLIT = 41
    BOOLEANLIT = 42
    STRINGLIT = 43
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
            "BOOLEANTYPE", "INTTYPE", "FLOATTYPE", "STRINGTYPE", "VOIDTYPE", 
            "DO", "WHILE", "FOR", "BREAK", "CONTINUE", "IF", "ELSE", "RETURN", 
            "TRUE", "FALSE", "ID", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
            "OR", "AND", "EQ", "NE", "LT", "GT", "LE", "GE", "ASSIGN", "LB", 
            "RB", "LP", "RP", "LSB", "RSB", "COMA", "SEMI", "INTLIT", "FLOATLIT", 
            "BOOLEANLIT", "STRINGLIT", "CMTLINE", "CMTBLOCK", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "Digit", "Lowcase", "Uppercase", "Letter", "Character", 
                  "Escape", "IllegalEscape", "Dot", "Underscore", "Exponent", 
                  "BOOLEANTYPE", "INTTYPE", "FLOATTYPE", "STRINGTYPE", "VOIDTYPE", 
                  "DO", "WHILE", "FOR", "BREAK", "CONTINUE", "IF", "ELSE", 
                  "RETURN", "TRUE", "FALSE", "ID", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "NOT", "OR", "AND", "EQ", "NE", "LT", "GT", 
                  "LE", "GE", "ASSIGN", "LB", "RB", "LP", "RP", "LSB", "RSB", 
                  "COMA", "SEMI", "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", 
                  "CMTLINE", "CMTBLOCK", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

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
            actions[52] = self.STRINGLIT_action 
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

     


