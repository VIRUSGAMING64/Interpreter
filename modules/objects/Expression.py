from .Tokens import *


class Expression:
    def __init__(self, expr):
        self.expr:str = expr
        self.type     = None

    
    def eval(self):
        return 1 #todo ERREGLAR PARA EVALUAR (3 + 312 ) / 13 + 1 <=== ejemplo
        pass

    def Token(self):
      
        if self.expr.isnumeric():
            return Token(self.expr, NUMBER)
        elif self.expr.startswith("\"") and self.expr.endswith("\""):
            return Token(self.expr, STRING)
        elif self.expr.startswith("'") and self.expr.endswith("'"):
            return Token(self.expr, STRING)
        else:
            res = self.eval()
            if res == None:
                return "an error in expression" #todo aqui hay q retornar errores reales 

            return Token(self.expr, FUNC, res)