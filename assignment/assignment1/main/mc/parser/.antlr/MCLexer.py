# Generated from /home/kraken/ppl-course/assignment/assignment1/main/mc/parser/MC.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\62")
        buf.write("\u018f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6")
        buf.write("\3\6\5\6\u0085\n\6\3\7\3\7\5\7\u0089\n\7\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\5\f\u0097\n\f\3\f")
        buf.write("\6\f\u009a\n\f\r\f\16\f\u009b\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\5\34\u00f4\n\34\3\34\3\34\3\34\7\34\u00f9")
        buf.write("\n\34\f\34\16\34\u00fc\13\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3")
        buf.write("&\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3")
        buf.write("-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3")
        buf.write("\63\3\64\3\64\3\64\6\64\u0135\n\64\r\64\16\64\u0136\5")
        buf.write("\64\u0139\n\64\3\65\6\65\u013c\n\65\r\65\16\65\u013d\3")
        buf.write("\65\3\65\7\65\u0142\n\65\f\65\16\65\u0145\13\65\3\65\5")
        buf.write("\65\u0148\n\65\3\65\7\65\u014b\n\65\f\65\16\65\u014e\13")
        buf.write("\65\3\65\3\65\6\65\u0152\n\65\r\65\16\65\u0153\3\65\5")
        buf.write("\65\u0157\n\65\3\65\6\65\u015a\n\65\r\65\16\65\u015b\3")
        buf.write("\65\3\65\5\65\u0160\n\65\3\66\3\66\5\66\u0164\n\66\3\67")
        buf.write("\3\67\7\67\u0168\n\67\f\67\16\67\u016b\13\67\3\67\3\67")
        buf.write("\3\67\38\68\u0171\n8\r8\168\u0172\38\38\39\39\79\u0179")
        buf.write("\n9\f9\169\u017c\139\39\59\u017f\n9\39\39\3:\3:\7:\u0185")
        buf.write("\n:\f:\16:\u0188\13:\3:\3:\3:\3;\3;\3;\2\2<\3\3\5\2\7")
        buf.write("\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\4\33\5\35")
        buf.write("\6\37\7!\b#\t%\n\'\13)\f+\r-\16/\17\61\20\63\21\65\22")
        buf.write("\67\239\24;\25=\26?\27A\30C\31E\32G\33I\34K\35M\36O\37")
        buf.write("Q S!U\"W#Y$[%]&_\'a(c)e*g+i,k-m.o/q\60s\61u\62\3\2\13")
        buf.write("\3\2\62;\3\2c|\3\2C\\\6\2\n\f\16\17$$^^\t\2$$^^ddhhpp")
        buf.write("ttvv\4\2GGgg\3\2\63;\5\2\13\f\17\17\"\"\7\3\n\f\16\17")
        buf.write("$$))^^\2\u019c\2\3\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2")
        buf.write("\2\2\2s\3\2\2\2\2u\3\2\2\2\3w\3\2\2\2\5|\3\2\2\2\7~\3")
        buf.write("\2\2\2\t\u0080\3\2\2\2\13\u0084\3\2\2\2\r\u0088\3\2\2")
        buf.write("\2\17\u008a\3\2\2\2\21\u008d\3\2\2\2\23\u0090\3\2\2\2")
        buf.write("\25\u0092\3\2\2\2\27\u0094\3\2\2\2\31\u009d\3\2\2\2\33")
        buf.write("\u00a5\3\2\2\2\35\u00a9\3\2\2\2\37\u00af\3\2\2\2!\u00b6")
        buf.write("\3\2\2\2#\u00bb\3\2\2\2%\u00be\3\2\2\2\'\u00c4\3\2\2\2")
        buf.write(")\u00c8\3\2\2\2+\u00ce\3\2\2\2-\u00d7\3\2\2\2/\u00da\3")
        buf.write("\2\2\2\61\u00df\3\2\2\2\63\u00e6\3\2\2\2\65\u00eb\3\2")
        buf.write("\2\2\67\u00f3\3\2\2\29\u00fd\3\2\2\2;\u00ff\3\2\2\2=\u0101")
        buf.write("\3\2\2\2?\u0103\3\2\2\2A\u0105\3\2\2\2C\u0107\3\2\2\2")
        buf.write("E\u0109\3\2\2\2G\u010c\3\2\2\2I\u010f\3\2\2\2K\u0112\3")
        buf.write("\2\2\2M\u0115\3\2\2\2O\u0117\3\2\2\2Q\u0119\3\2\2\2S\u011c")
        buf.write("\3\2\2\2U\u011f\3\2\2\2W\u0121\3\2\2\2Y\u0123\3\2\2\2")
        buf.write("[\u0125\3\2\2\2]\u0127\3\2\2\2_\u0129\3\2\2\2a\u012b\3")
        buf.write("\2\2\2c\u012d\3\2\2\2e\u012f\3\2\2\2g\u0138\3\2\2\2i\u015f")
        buf.write("\3\2\2\2k\u0163\3\2\2\2m\u0165\3\2\2\2o\u0170\3\2\2\2")
        buf.write("q\u0176\3\2\2\2s\u0182\3\2\2\2u\u018c\3\2\2\2wx\7o\2\2")
        buf.write("xy\7c\2\2yz\7k\2\2z{\7p\2\2{\4\3\2\2\2|}\t\2\2\2}\6\3")
        buf.write("\2\2\2~\177\t\3\2\2\177\b\3\2\2\2\u0080\u0081\t\4\2\2")
        buf.write("\u0081\n\3\2\2\2\u0082\u0085\5\7\4\2\u0083\u0085\5\t\5")
        buf.write("\2\u0084\u0082\3\2\2\2\u0084\u0083\3\2\2\2\u0085\f\3\2")
        buf.write("\2\2\u0086\u0089\n\5\2\2\u0087\u0089\5\17\b\2\u0088\u0086")
        buf.write("\3\2\2\2\u0088\u0087\3\2\2\2\u0089\16\3\2\2\2\u008a\u008b")
        buf.write("\7^\2\2\u008b\u008c\t\6\2\2\u008c\20\3\2\2\2\u008d\u008e")
        buf.write("\7^\2\2\u008e\u008f\n\6\2\2\u008f\22\3\2\2\2\u0090\u0091")
        buf.write("\7\60\2\2\u0091\24\3\2\2\2\u0092\u0093\7a\2\2\u0093\26")
        buf.write("\3\2\2\2\u0094\u0096\t\7\2\2\u0095\u0097\7/\2\2\u0096")
        buf.write("\u0095\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0099\3\2\2\2")
        buf.write("\u0098\u009a\5\5\3\2\u0099\u0098\3\2\2\2\u009a\u009b\3")
        buf.write("\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\30")
        buf.write("\3\2\2\2\u009d\u009e\7d\2\2\u009e\u009f\7q\2\2\u009f\u00a0")
        buf.write("\7q\2\2\u00a0\u00a1\7n\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3")
        buf.write("\7c\2\2\u00a3\u00a4\7p\2\2\u00a4\32\3\2\2\2\u00a5\u00a6")
        buf.write("\7k\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8\7v\2\2\u00a8\34")
        buf.write("\3\2\2\2\u00a9\u00aa\7h\2\2\u00aa\u00ab\7n\2\2\u00ab\u00ac")
        buf.write("\7q\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae\7v\2\2\u00ae\36")
        buf.write("\3\2\2\2\u00af\u00b0\7u\2\2\u00b0\u00b1\7v\2\2\u00b1\u00b2")
        buf.write("\7t\2\2\u00b2\u00b3\7k\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b5")
        buf.write("\7i\2\2\u00b5 \3\2\2\2\u00b6\u00b7\7x\2\2\u00b7\u00b8")
        buf.write("\7q\2\2\u00b8\u00b9\7k\2\2\u00b9\u00ba\7f\2\2\u00ba\"")
        buf.write("\3\2\2\2\u00bb\u00bc\7f\2\2\u00bc\u00bd\7q\2\2\u00bd$")
        buf.write("\3\2\2\2\u00be\u00bf\7y\2\2\u00bf\u00c0\7j\2\2\u00c0\u00c1")
        buf.write("\7k\2\2\u00c1\u00c2\7n\2\2\u00c2\u00c3\7g\2\2\u00c3&\3")
        buf.write("\2\2\2\u00c4\u00c5\7h\2\2\u00c5\u00c6\7q\2\2\u00c6\u00c7")
        buf.write("\7t\2\2\u00c7(\3\2\2\2\u00c8\u00c9\7d\2\2\u00c9\u00ca")
        buf.write("\7t\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc\7c\2\2\u00cc\u00cd")
        buf.write("\7m\2\2\u00cd*\3\2\2\2\u00ce\u00cf\7e\2\2\u00cf\u00d0")
        buf.write("\7q\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3")
        buf.write("\7k\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5\7w\2\2\u00d5\u00d6")
        buf.write("\7g\2\2\u00d6,\3\2\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9")
        buf.write("\7h\2\2\u00d9.\3\2\2\2\u00da\u00db\7g\2\2\u00db\u00dc")
        buf.write("\7n\2\2\u00dc\u00dd\7u\2\2\u00dd\u00de\7g\2\2\u00de\60")
        buf.write("\3\2\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2")
        buf.write("\7v\2\2\u00e2\u00e3\7w\2\2\u00e3\u00e4\7t\2\2\u00e4\u00e5")
        buf.write("\7p\2\2\u00e5\62\3\2\2\2\u00e6\u00e7\7v\2\2\u00e7\u00e8")
        buf.write("\7t\2\2\u00e8\u00e9\7w\2\2\u00e9\u00ea\7g\2\2\u00ea\64")
        buf.write("\3\2\2\2\u00eb\u00ec\7h\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee")
        buf.write("\7n\2\2\u00ee\u00ef\7u\2\2\u00ef\u00f0\7g\2\2\u00f0\66")
        buf.write("\3\2\2\2\u00f1\u00f4\5\13\6\2\u00f2\u00f4\5\25\13\2\u00f3")
        buf.write("\u00f1\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4\u00fa\3\2\2\2")
        buf.write("\u00f5\u00f9\5\13\6\2\u00f6\u00f9\5\25\13\2\u00f7\u00f9")
        buf.write("\5\5\3\2\u00f8\u00f5\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8")
        buf.write("\u00f7\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2")
        buf.write("\u00fa\u00fb\3\2\2\2\u00fb8\3\2\2\2\u00fc\u00fa\3\2\2")
        buf.write("\2\u00fd\u00fe\7-\2\2\u00fe:\3\2\2\2\u00ff\u0100\7/\2")
        buf.write("\2\u0100<\3\2\2\2\u0101\u0102\7,\2\2\u0102>\3\2\2\2\u0103")
        buf.write("\u0104\7\61\2\2\u0104@\3\2\2\2\u0105\u0106\7\'\2\2\u0106")
        buf.write("B\3\2\2\2\u0107\u0108\7#\2\2\u0108D\3\2\2\2\u0109\u010a")
        buf.write("\7~\2\2\u010a\u010b\7~\2\2\u010bF\3\2\2\2\u010c\u010d")
        buf.write("\7(\2\2\u010d\u010e\7(\2\2\u010eH\3\2\2\2\u010f\u0110")
        buf.write("\7?\2\2\u0110\u0111\7?\2\2\u0111J\3\2\2\2\u0112\u0113")
        buf.write("\7#\2\2\u0113\u0114\7?\2\2\u0114L\3\2\2\2\u0115\u0116")
        buf.write("\7>\2\2\u0116N\3\2\2\2\u0117\u0118\7@\2\2\u0118P\3\2\2")
        buf.write("\2\u0119\u011a\7>\2\2\u011a\u011b\7?\2\2\u011bR\3\2\2")
        buf.write("\2\u011c\u011d\7@\2\2\u011d\u011e\7?\2\2\u011eT\3\2\2")
        buf.write("\2\u011f\u0120\7?\2\2\u0120V\3\2\2\2\u0121\u0122\7*\2")
        buf.write("\2\u0122X\3\2\2\2\u0123\u0124\7+\2\2\u0124Z\3\2\2\2\u0125")
        buf.write("\u0126\7}\2\2\u0126\\\3\2\2\2\u0127\u0128\7\177\2\2\u0128")
        buf.write("^\3\2\2\2\u0129\u012a\7]\2\2\u012a`\3\2\2\2\u012b\u012c")
        buf.write("\7_\2\2\u012cb\3\2\2\2\u012d\u012e\7.\2\2\u012ed\3\2\2")
        buf.write("\2\u012f\u0130\7=\2\2\u0130f\3\2\2\2\u0131\u0139\7\62")
        buf.write("\2\2\u0132\u0134\t\b\2\2\u0133\u0135\t\2\2\2\u0134\u0133")
        buf.write("\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0134\3\2\2\2\u0136")
        buf.write("\u0137\3\2\2\2\u0137\u0139\3\2\2\2\u0138\u0131\3\2\2\2")
        buf.write("\u0138\u0132\3\2\2\2\u0139h\3\2\2\2\u013a\u013c\5\5\3")
        buf.write("\2\u013b\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013b")
        buf.write("\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u013f\3\2\2\2\u013f")
        buf.write("\u0143\5\23\n\2\u0140\u0142\5\5\3\2\u0141\u0140\3\2\2")
        buf.write("\2\u0142\u0145\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144")
        buf.write("\3\2\2\2\u0144\u0147\3\2\2\2\u0145\u0143\3\2\2\2\u0146")
        buf.write("\u0148\5\27\f\2\u0147\u0146\3\2\2\2\u0147\u0148\3\2\2")
        buf.write("\2\u0148\u0160\3\2\2\2\u0149\u014b\5\5\3\2\u014a\u0149")
        buf.write("\3\2\2\2\u014b\u014e\3\2\2\2\u014c\u014a\3\2\2\2\u014c")
        buf.write("\u014d\3\2\2\2\u014d\u014f\3\2\2\2\u014e\u014c\3\2\2\2")
        buf.write("\u014f\u0151\5\23\n\2\u0150\u0152\5\5\3\2\u0151\u0150")
        buf.write("\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0151\3\2\2\2\u0153")
        buf.write("\u0154\3\2\2\2\u0154\u0156\3\2\2\2\u0155\u0157\5\27\f")
        buf.write("\2\u0156\u0155\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0160")
        buf.write("\3\2\2\2\u0158\u015a\5\5\3\2\u0159\u0158\3\2\2\2\u015a")
        buf.write("\u015b\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2")
        buf.write("\u015c\u015d\3\2\2\2\u015d\u015e\5\27\f\2\u015e\u0160")
        buf.write("\3\2\2\2\u015f\u013b\3\2\2\2\u015f\u014c\3\2\2\2\u015f")
        buf.write("\u0159\3\2\2\2\u0160j\3\2\2\2\u0161\u0164\5\63\32\2\u0162")
        buf.write("\u0164\5\65\33\2\u0163\u0161\3\2\2\2\u0163\u0162\3\2\2")
        buf.write("\2\u0164l\3\2\2\2\u0165\u0169\7$\2\2\u0166\u0168\5\r\7")
        buf.write("\2\u0167\u0166\3\2\2\2\u0168\u016b\3\2\2\2\u0169\u0167")
        buf.write("\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016c\3\2\2\2\u016b")
        buf.write("\u0169\3\2\2\2\u016c\u016d\7$\2\2\u016d\u016e\b\67\2\2")
        buf.write("\u016en\3\2\2\2\u016f\u0171\t\t\2\2\u0170\u016f\3\2\2")
        buf.write("\2\u0171\u0172\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173")
        buf.write("\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175\b8\3\2\u0175")
        buf.write("p\3\2\2\2\u0176\u017a\7$\2\2\u0177\u0179\5\r\7\2\u0178")
        buf.write("\u0177\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2")
        buf.write("\u017a\u017b\3\2\2\2\u017b\u017e\3\2\2\2\u017c\u017a\3")
        buf.write("\2\2\2\u017d\u017f\t\n\2\2\u017e\u017d\3\2\2\2\u017f\u0180")
        buf.write("\3\2\2\2\u0180\u0181\b9\4\2\u0181r\3\2\2\2\u0182\u0186")
        buf.write("\7$\2\2\u0183\u0185\5\r\7\2\u0184\u0183\3\2\2\2\u0185")
        buf.write("\u0188\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2")
        buf.write("\u0187\u0189\3\2\2\2\u0188\u0186\3\2\2\2\u0189\u018a\5")
        buf.write("\21\t\2\u018a\u018b\b:\5\2\u018bt\3\2\2\2\u018c\u018d")
        buf.write("\13\2\2\2\u018d\u018e\b;\6\2\u018ev\3\2\2\2\32\2\u0084")
        buf.write("\u0088\u0096\u009b\u00f3\u00f8\u00fa\u0136\u0138\u013d")
        buf.write("\u0143\u0147\u014c\u0153\u0156\u015b\u015f\u0163\u0169")
        buf.write("\u0172\u017a\u017e\u0186\7\3\67\2\b\2\2\39\3\3:\4\3;\5")
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
    WS = 45
    UNCLOSE_STRING = 46
    ILLEGAL_ESCAPE = 47
    ERROR_CHAR = 48

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
            "FLOATLIT", "BOOLEANLIT", "STRINGLIT", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "Digit", "Lowcase", "Uppercase", "Letter", "Character", 
                  "Escape", "IllegalEscape", "Dot", "Underscore", "Exponent", 
                  "BOOLEANTYPE", "INTTYPE", "FLOATTYPE", "STRINGTYPE", "VOIDTYPE", 
                  "DO", "WHILE", "FOR", "BREAK", "CONTINUE", "IF", "ELSE", 
                  "RETURN", "TRUE", "FALSE", "ID", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "NOT", "OR", "AND", "EQUAL", "NOT_EQUAL", 
                  "LT", "GT", "LE", "GE", "ASSIGN", "LB", "RB", "LP", "RP", 
                  "LSB", "RSB", "COMA", "SEMI", "INTLIT", "FLOATLIT", "BOOLEANLIT", 
                  "STRINGLIT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
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
            actions[53] = self.STRINGLIT_action 
            actions[55] = self.UNCLOSE_STRING_action 
            actions[56] = self.ILLEGAL_ESCAPE_action 
            actions[57] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                temp = str(self.test)
                self.test = temp[1:-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                esc = ['\b', '\t', '\n', '\f', '\r', '"', '\\']
                temp = str(self.test)

                if temp[-1] in esc:
                    raise UncloseString(temp[1:-1])
                else :
                    raise UncloseString(temp[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                temp = str(self.test)
                raise IllegallEscape(temp[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise ErrorToken(self.text)

     


