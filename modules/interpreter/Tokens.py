from modules.generic.utils import *
from modules.interpreter.statics_values import *
import functools

class Token:
    def __init__(self,expr, type = NIL, tokens = None, data = None):
        self.expr:str     = expr
        self.type         = type
        self.tokens       = [] if tokens is None else tokens
        self.data         = {} if data is None else dict(data)
        self.data["name"] = self.expr

    def __dict__(self):
        di         = {}
        di["expr"] = self.expr
        di["data"] = self.data
        di["type"] = self.type
        tok = self.tokens
        if isinstance(self.tokens, list):
            tok = []
            for target in self.tokens:
                target = target.__dict__()
                tok.append(target)
        di["tokens"] = tok
        return di

    def copy(self):
        tok = self.tokens
        if isinstance(self.tokens, list):
            tok = []
            for target in self.tokens:
                if isinstance(target, Token):
                    tok.append(target.copy())
                else:
                    tok.append(target)
        return Token(self.expr, self.type, tok, self.data.copy())

    def get(self,key,default):
        return self.data.get(key,default)
    
    def put(self, key ,data):
        self.data[key] = data

    def isKeyword(self):
        return KEYWORD if self.expr in keywords else 0
    
    def isOperator(self):
        return OPERATION if self.expr in operators else 0
    
    def VarName(self):
        alphas = ""
        for i in self.expr:
            if i.isalnum():
                alphas+=i
            elif i != "_":
                return INVALID
        
        if(alphas[0].isnumeric()):
            return INVALID

        if len(alphas) >= 1:
            return VARIABLES
        
        print(alphas)
        return INVALID
    
    def IsNumeric(self):
        if self.expr.isnumeric():
            self.expr = int(self.expr)
            return NUMBER
        return INVALID
    
    def IsString(self,sep = None) -> int:
        if(sep == None):
            return self.IsString("'") | self.IsString('"')
        if self.expr.startswith(sep) and self.expr.endswith(sep) and len(self.expr) > 1:
            self.expr = self.expr.removeprefix(sep).removesuffix(sep)
            return STRING
        return INVALID
    
    def isLabel(self):
        return LABEL if self.expr.endswith(":") else 0
    
    def math(self, token):
        if token.expr in maths[self.expr]:
            return True
        return False
    

def dict2Token(di:dict):
    typ = di.get("type", None)
    expr = di.get("expr", None)
    tokens = di.get("tokens")
    data = di.get("data", None)

    if None in [typ, expr] or (tokens != None and not isinstance(tokens, list)):
        raise Exception("Invalid dict")
    
    if isinstance(tokens, list):
        toks = []
        for tok in tokens:
            tok = dict2Token(tok)
            toks.append(tok)
        tokens = toks
    n_tok = Token(expr , typ, tokens)
    n_tok.data = data
    return n_tok