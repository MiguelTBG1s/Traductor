# Generated from grammarTraductor.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .grammarTraductorParser import grammarTraductorParser
else:
    from grammarTraductorParser import grammarTraductorParser

# This class defines a complete listener for a parse tree produced by grammarTraductorParser.
class grammarTraductorListener(ParseTreeListener):

    # Enter a parse tree produced by grammarTraductorParser#program.
    def enterProgram(self, ctx:grammarTraductorParser.ProgramContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#program.
    def exitProgram(self, ctx:grammarTraductorParser.ProgramContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#funcion.
    def enterFuncion(self, ctx:grammarTraductorParser.FuncionContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#funcion.
    def exitFuncion(self, ctx:grammarTraductorParser.FuncionContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#parametros.
    def enterParametros(self, ctx:grammarTraductorParser.ParametrosContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#parametros.
    def exitParametros(self, ctx:grammarTraductorParser.ParametrosContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#parametrosNum.
    def enterParametrosNum(self, ctx:grammarTraductorParser.ParametrosNumContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#parametrosNum.
    def exitParametrosNum(self, ctx:grammarTraductorParser.ParametrosNumContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#instrucciones.
    def enterInstrucciones(self, ctx:grammarTraductorParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#instrucciones.
    def exitInstrucciones(self, ctx:grammarTraductorParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#main.
    def enterMain(self, ctx:grammarTraductorParser.MainContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#main.
    def exitMain(self, ctx:grammarTraductorParser.MainContext):
        pass


