from .Tokens import *
from modules.utils import *

class Expression:
    def __init__(self, expr):
        self.expr:str = expr
        self.type     = None

    def Token(self):
        self.expr = cleanStr(self.expr)
        res = Tokenize(self.expr)
        return Token(self.expr, LINE, res)
    
    def __dict__(self):
        return {
            "expr":self.expr,
            "type":self.type
        }
    

def eval_line(line:list[Token]):
    stack = []

    while len(stack):
        pass335        
