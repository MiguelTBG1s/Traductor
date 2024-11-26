from grammarTraductorListener import grammarTraductorListener;
from grammarTraductorParser import *;

class TraducePyToJava(grammarTraductorListener):
    def __init__(self): 
        self.java_code = ""
       
    # Enter a parse tree produced by grammarTraductorParser#program.
    def enterProgram(self, ctx:grammarTraductorParser.ProgramContext):
        self.java_code +=  'public class Multiplica {\n'

    # Exit a parse tree produced by grammarTraductorParser#program.
    def exitProgram(self, ctx:grammarTraductorParser.ProgramContext):
        self.java_code += '\n}'
        
        # Especificamos el nombre del archivo y abrimos en modo de escritura
        file_name = "Multiplica.java"
        with open(file_name, "w") as file:
            file.write(self.java_code)

        print(f"El código Java ha sido guardado en el archivo '{file_name}'.")
        print(self.java_code)


    # Enter a parse tree produced by grammarTraductorParser#funcion.
    def enterFuncion(self, ctx:grammarTraductorParser.FuncionContext):
        
        self.java_code += f'\tpublic static int {ctx.VARIABLE(0).getText()}(int {ctx.parametros().VARIABLE(0).getText()}, int {ctx.parametros().VARIABLE(1).getText()})'+'{\n\n'
        
    # Exit a parse tree produced by grammarTraductorParser#funcion.
    def exitFuncion(self, ctx:grammarTraductorParser.FuncionContext):
        self.java_code += f'\n\t\treturn {ctx.VARIABLE(1)};\n'
        self.java_code += '\t}\n'
    
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
        self.java_code += f'\t\tint {ctx.VARIABLE(0).getText()} = {ctx.VARIABLE(1).getText()} {ctx.MULTIPLICACION()} {ctx.VARIABLE(2)} {ctx.RESTA()} {ctx.VARIABLE(1)};'

    # Exit a parse tree produced by grammarTraductorParser#instrucciones.
    def exitInstrucciones(self, ctx:grammarTraductorParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#main.
    def enterMain(self, ctx:grammarTraductorParser.MainContext):
        self.java_code += '\tpublic static void main(String[] args) {'
        self.java_code += f'\n\n\t\tSystem.out.println({ctx.VARIABLE()}({ctx.parametrosNum().NUMERO(0)},{ctx.parametrosNum().NUMERO(1)}));\n\n'
    # Exit a parse tree produced by grammarTraductorParser#main.
    def exitMain(self, ctx:grammarTraductorParser.MainContext):
        self.java_code += '\t}'
        