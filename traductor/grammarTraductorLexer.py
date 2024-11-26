# Generated from grammarTraductor.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("S\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\7\r")
        buf.write("C\n\r\f\r\16\rF\13\r\3\16\6\16I\n\16\r\16\16\16J\3\17")
        buf.write("\6\17N\n\17\r\17\16\17O\3\17\3\17\2\2\20\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\3\2\6\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\5\2\13\f\17\17")
        buf.write("\"\"\2U\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5#\3\2\2\2\7*\3")
        buf.write("\2\2\2\t\60\3\2\2\2\13\62\3\2\2\2\r\64\3\2\2\2\17\66\3")
        buf.write("\2\2\2\218\3\2\2\2\23:\3\2\2\2\25<\3\2\2\2\27>\3\2\2\2")
        buf.write("\31@\3\2\2\2\33H\3\2\2\2\35M\3\2\2\2\37 \7f\2\2 !\7g\2")
        buf.write("\2!\"\7h\2\2\"\4\3\2\2\2#$\7t\2\2$%\7g\2\2%&\7v\2\2&\'")
        buf.write("\7w\2\2\'(\7t\2\2()\7p\2\2)\6\3\2\2\2*+\7r\2\2+,\7t\2")
        buf.write("\2,-\7k\2\2-.\7p\2\2./\7v\2\2/\b\3\2\2\2\60\61\7-\2\2")
        buf.write("\61\n\3\2\2\2\62\63\7,\2\2\63\f\3\2\2\2\64\65\7/\2\2\65")
        buf.write("\16\3\2\2\2\66\67\7*\2\2\67\20\3\2\2\289\7+\2\29\22\3")
        buf.write("\2\2\2:;\7?\2\2;\24\3\2\2\2<=\7<\2\2=\26\3\2\2\2>?\7.")
        buf.write("\2\2?\30\3\2\2\2@D\t\2\2\2AC\t\3\2\2BA\3\2\2\2CF\3\2\2")
        buf.write("\2DB\3\2\2\2DE\3\2\2\2E\32\3\2\2\2FD\3\2\2\2GI\t\4\2\2")
        buf.write("HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2\2\2K\34\3\2\2\2L")
        buf.write("N\t\5\2\2ML\3\2\2\2NO\3\2\2\2OM\3\2\2\2OP\3\2\2\2PQ\3")
        buf.write("\2\2\2QR\b\17\2\2R\36\3\2\2\2\6\2DJO\3\b\2\2")
        return buf.getvalue()


class grammarTraductorLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DEF = 1
    RETURN = 2
    PRINT = 3
    SUMA = 4
    MULTIPLICACION = 5
    RESTA = 6
    PARENTESISABRE = 7
    PARENTESISCIERRA = 8
    IGUAL = 9
    DOBLEPUNTO = 10
    COMA = 11
    VARIABLE = 12
    NUMERO = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'def'", "'return'", "'print'", "'+'", "'*'", "'-'", "'('", 
            "')'", "'='", "':'", "','" ]

    symbolicNames = [ "<INVALID>",
            "DEF", "RETURN", "PRINT", "SUMA", "MULTIPLICACION", "RESTA", 
            "PARENTESISABRE", "PARENTESISCIERRA", "IGUAL", "DOBLEPUNTO", 
            "COMA", "VARIABLE", "NUMERO", "WS" ]

    ruleNames = [ "DEF", "RETURN", "PRINT", "SUMA", "MULTIPLICACION", "RESTA", 
                  "PARENTESISABRE", "PARENTESISCIERRA", "IGUAL", "DOBLEPUNTO", 
                  "COMA", "VARIABLE", "NUMERO", "WS" ]

    grammarFileName = "grammarTraductor.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


