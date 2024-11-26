grammar grammarTraductor;

// Reglas de palabras reservadas
DEF: 'def' ;
RETURN: 'return' ;
PRINT: 'print' ;

// Reglas de operadores
SUMA: '+' ;
MULTIPLICACION: '*' ;
RESTA: '-' ;
PARENTESISABRE: '(' ;
PARENTESISCIERRA: ')' ;
IGUAL: '=' ;

// Reglas de signos de puntuación
DOBLEPUNTO: ':' ;
COMA: ',' ;

// Reglas de variables
VARIABLE: [a-zA-Z_][a-zA-Z_0-9]* ; 

// reglas de numeros
NUMERO: [0-9]+ ;

WS : [ \t\r\n]+ -> skip ;

//programa inicial
program: funcion main;

//funcion
funcion:  DEF VARIABLE PARENTESISABRE parametros? PARENTESISCIERRA DOBLEPUNTO  instrucciones RETURN VARIABLE;

parametros: VARIABLE (COMA VARIABLE)*;

parametrosNum: NUMERO (COMA NUMERO)*;

instrucciones: VARIABLE IGUAL VARIABLE MULTIPLICACION VARIABLE RESTA VARIABLE;

main: PRINT PARENTESISABRE VARIABLE PARENTESISABRE parametrosNum? PARENTESISCIERRA;