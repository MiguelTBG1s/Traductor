# Generated from grammarTraductor.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("?\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\5\3\26\n\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\7\4!\n\4\f\4\16\4$\13\4\3\5\3\5\3\5")
        buf.write("\7\5)\n\5\f\5\16\5,\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\5\7;\n\7\3\7\3\7\3\7\2\2\b\2\4")
        buf.write("\6\b\n\f\2\2\2<\2\16\3\2\2\2\4\21\3\2\2\2\6\35\3\2\2\2")
        buf.write("\b%\3\2\2\2\n-\3\2\2\2\f\65\3\2\2\2\16\17\5\4\3\2\17\20")
        buf.write("\5\f\7\2\20\3\3\2\2\2\21\22\7\3\2\2\22\23\7\16\2\2\23")
        buf.write("\25\7\t\2\2\24\26\5\6\4\2\25\24\3\2\2\2\25\26\3\2\2\2")
        buf.write("\26\27\3\2\2\2\27\30\7\n\2\2\30\31\7\f\2\2\31\32\5\n\6")
        buf.write("\2\32\33\7\4\2\2\33\34\7\16\2\2\34\5\3\2\2\2\35\"\7\16")
        buf.write("\2\2\36\37\7\r\2\2\37!\7\16\2\2 \36\3\2\2\2!$\3\2\2\2")
        buf.write("\" \3\2\2\2\"#\3\2\2\2#\7\3\2\2\2$\"\3\2\2\2%*\7\17\2")
        buf.write("\2&\'\7\r\2\2\')\7\17\2\2(&\3\2\2\2),\3\2\2\2*(\3\2\2")
        buf.write("\2*+\3\2\2\2+\t\3\2\2\2,*\3\2\2\2-.\7\16\2\2./\7\13\2")
        buf.write("\2/\60\7\16\2\2\60\61\7\7\2\2\61\62\7\16\2\2\62\63\7\b")
        buf.write("\2\2\63\64\7\16\2\2\64\13\3\2\2\2\65\66\7\5\2\2\66\67")
        buf.write("\7\t\2\2\678\7\16\2\28:\7\t\2\29;\5\b\5\2:9\3\2\2\2:;")
        buf.write("\3\2\2\2;<\3\2\2\2<=\7\n\2\2=\r\3\2\2\2\6\25\"*:")
        return buf.getvalue()


class grammarTraductorParser ( Parser ):

    grammarFileName = "grammarTraductor.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'return'", "'print'", "'+'", 
                     "'*'", "'-'", "'('", "')'", "'='", "':'", "','" ]

    symbolicNames = [ "<INVALID>", "DEF", "RETURN", "PRINT", "SUMA", "MULTIPLICACION", 
                      "RESTA", "PARENTESISABRE", "PARENTESISCIERRA", "IGUAL", 
                      "DOBLEPUNTO", "COMA", "VARIABLE", "NUMERO", "WS" ]

    RULE_program = 0
    RULE_funcion = 1
    RULE_parametros = 2
    RULE_parametrosNum = 3
    RULE_instrucciones = 4
    RULE_main = 5

    ruleNames =  [ "program", "funcion", "parametros", "parametrosNum", 
                   "instrucciones", "main" ]

    EOF = Token.EOF
    DEF=1
    RETURN=2
    PRINT=3
    SUMA=4
    MULTIPLICACION=5
    RESTA=6
    PARENTESISABRE=7
    PARENTESISCIERRA=8
    IGUAL=9
    DOBLEPUNTO=10
    COMA=11
    VARIABLE=12
    NUMERO=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcion(self):
            return self.getTypedRuleContext(grammarTraductorParser.FuncionContext,0)


        def main(self):
            return self.getTypedRuleContext(grammarTraductorParser.MainContext,0)


        def getRuleIndex(self):
            return grammarTraductorParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = grammarTraductorParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.funcion()
            self.state = 13
            self.main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(grammarTraductorParser.DEF, 0)

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(grammarTraductorParser.VARIABLE)
            else:
                return self.getToken(grammarTraductorParser.VARIABLE, i)

        def PARENTESISABRE(self):
            return self.getToken(grammarTraductorParser.PARENTESISABRE, 0)

        def PARENTESISCIERRA(self):
            return self.getToken(grammarTraductorParser.PARENTESISCIERRA, 0)

        def DOBLEPUNTO(self):
            return self.getToken(grammarTraductorParser.DOBLEPUNTO, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(grammarTraductorParser.InstruccionesContext,0)


        def RETURN(self):
            return self.getToken(grammarTraductorParser.RETURN, 0)

        def parametros(self):
            return self.getTypedRuleContext(grammarTraductorParser.ParametrosContext,0)


        def getRuleIndex(self):
            return grammarTraductorParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)




    def funcion(self):

        localctx = grammarTraductorParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(grammarTraductorParser.DEF)
            self.state = 16
            self.match(grammarTraductorParser.VARIABLE)
            self.state = 17
            self.match(grammarTraductorParser.PARENTESISABRE)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==grammarTraductorParser.VARIABLE:
                self.state = 18
                self.parametros()


            self.state = 21
            self.match(grammarTraductorParser.PARENTESISCIERRA)
            self.state = 22
            self.match(grammarTraductorParser.DOBLEPUNTO)
            self.state = 23
            self.instrucciones()
            self.state = 24
            self.match(grammarTraductorParser.RETURN)
            self.state = 25
            self.match(grammarTraductorParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParametrosContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(grammarTraductorParser.VARIABLE)
            else:
                return self.getToken(grammarTraductorParser.VARIABLE, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(grammarTraductorParser.COMA)
            else:
                return self.getToken(grammarTraductorParser.COMA, i)

        def getRuleIndex(self):
            return grammarTraductorParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)




    def parametros(self):

        localctx = grammarTraductorParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(grammarTraductorParser.VARIABLE)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==grammarTraductorParser.COMA:
                self.state = 28
                self.match(grammarTraductorParser.COMA)
                self.state = 29
                self.match(grammarTraductorParser.VARIABLE)
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParametrosNumContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self, i:int=None):
            if i is None:
                return self.getTokens(grammarTraductorParser.NUMERO)
            else:
                return self.getToken(grammarTraductorParser.NUMERO, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(grammarTraductorParser.COMA)
            else:
                return self.getToken(grammarTraductorParser.COMA, i)

        def getRuleIndex(self):
            return grammarTraductorParser.RULE_parametrosNum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametrosNum" ):
                listener.enterParametrosNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametrosNum" ):
                listener.exitParametrosNum(self)




    def parametrosNum(self):

        localctx = grammarTraductorParser.ParametrosNumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parametrosNum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(grammarTraductorParser.NUMERO)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==grammarTraductorParser.COMA:
                self.state = 36
                self.match(grammarTraductorParser.COMA)
                self.state = 37
                self.match(grammarTraductorParser.NUMERO)
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InstruccionesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(grammarTraductorParser.VARIABLE)
            else:
                return self.getToken(grammarTraductorParser.VARIABLE, i)

        def IGUAL(self):
            return self.getToken(grammarTraductorParser.IGUAL, 0)

        def MULTIPLICACION(self):
            return self.getToken(grammarTraductorParser.MULTIPLICACION, 0)

        def RESTA(self):
            return self.getToken(grammarTraductorParser.RESTA, 0)

        def getRuleIndex(self):
            return grammarTraductorParser.RULE_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucciones" ):
                listener.enterInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucciones" ):
                listener.exitInstrucciones(self)




    def instrucciones(self):

        localctx = grammarTraductorParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_instrucciones)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(grammarTraductorParser.VARIABLE)
            self.state = 44
            self.match(grammarTraductorParser.IGUAL)
            self.state = 45
            self.match(grammarTraductorParser.VARIABLE)
            self.state = 46
            self.match(grammarTraductorParser.MULTIPLICACION)
            self.state = 47
            self.match(grammarTraductorParser.VARIABLE)
            self.state = 48
            self.match(grammarTraductorParser.RESTA)
            self.state = 49
            self.match(grammarTraductorParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(grammarTraductorParser.PRINT, 0)

        def PARENTESISABRE(self, i:int=None):
            if i is None:
                return self.getTokens(grammarTraductorParser.PARENTESISABRE)
            else:
                return self.getToken(grammarTraductorParser.PARENTESISABRE, i)

        def VARIABLE(self):
            return self.getToken(grammarTraductorParser.VARIABLE, 0)

        def PARENTESISCIERRA(self):
            return self.getToken(grammarTraductorParser.PARENTESISCIERRA, 0)

        def parametrosNum(self):
            return self.getTypedRuleContext(grammarTraductorParser.ParametrosNumContext,0)


        def getRuleIndex(self):
            return grammarTraductorParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = grammarTraductorParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(grammarTraductorParser.PRINT)
            self.state = 52
            self.match(grammarTraductorParser.PARENTESISABRE)
            self.state = 53
            self.match(grammarTraductorParser.VARIABLE)
            self.state = 54
            self.match(grammarTraductorParser.PARENTESISABRE)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==grammarTraductorParser.NUMERO:
                self.state = 55
                self.parametrosNum()


            self.state = 58
            self.match(grammarTraductorParser.PARENTESISCIERRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





