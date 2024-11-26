from  antlr4 import *
from grammarTraductorLexer import grammarTraductorLexer
from grammarTraductorParser import grammarTraductorParser
from grammarTraductorListener import grammarTraductorListener
from TraducePyToJava import TraducePyToJava

def main():
    in_code = input('File name> ')
    fileopen = open(in_code)
    
    lexer = grammarTraductorLexer(InputStream(fileopen.read()))
    stream = CommonTokenStream(lexer)
    parser = grammarTraductorParser(stream)
    tree = parser.program()
    
    #print(tree.toStringTree(recog=parser))
    walter = ParseTreeWalker()
    walter.walk(TraducePyToJava(),tree)
    
if __name__=='__main__':
    main()