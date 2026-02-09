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