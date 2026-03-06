from .Tokens import *
from modules.utils import *
from .memory import *

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
    

def CallFunc(self,func_line:list = []):
    pass
    

def eval_line(line:list[Token]):
    stack = []

    while len(stack):
        pass     
