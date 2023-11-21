from execution import BasicExecute
from lexer import BasicLexer
from parser1 import BasicParser


if __name__ == '__main__': 
    lexer = BasicLexer() 
    parser = BasicParser() 
    env = {} 
      
    while True: 
          
        try: 
            text = input('Rawr Compiler > ') 
          
        except EOFError: 
            break
          
        if text: 
            tree = parser.parse(lexer.tokenize(text)) 
            BasicExecute(tree, env)