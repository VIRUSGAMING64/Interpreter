from modules.utils import *
from modules.t_statics import *

def Tokenize(code):

    pos = 0
    act_tok = ""
    toks = []

    while pos <= len(code):

        if (pos < len(code)) and (not code[pos] in operators):
            act_tok += code[pos]
        else:
            dis = -1        
            act_tok = cleanStr(act_tok)
            toks.append(Token(act_tok,NIL))

            if pos < len(code):            
                dis -= 1
            
            p = False
            if act_tok == "":
                toks.pop()
                p = True

            if dis == -2:
                toks.append(Token(code[pos], OPERATION))
                if pos + 1 != len(code) and code[pos] + code[pos + 1] in operators:
                    toks[len(toks) - 1].expr += code[pos + 1]
                    pos += 1
                
            if p: 
                pos += 1
                continue
        
            if toks[len(toks) + dis].expr.isnumeric():
                toks[len(toks) + dis].type = NUMBER
            elif toks[len(toks) + dis].expr.startswith("\"") and toks[len(toks) + dis].expr.endswith("\""):
                toks[len(toks) + dis].type = STRING
            elif toks[len(toks) + dis].expr.startswith("'") and toks[len(toks) + dis].expr.endswith("'"):
                toks[len(toks) + dis].type = STRING
            elif toks[len(toks) + dis].isKeyword():
                toks[len(toks) + dis].type = KEYWORD
            elif toks[len(toks) + dis].isLabel():
                toks[len(toks) + dis].type = LABEL
            elif toks[len(toks) + dis].expr.isalnum():
                toks[len(toks) + dis].type = VARIABLES
            
            act_tok = ""

        pos += 1


    line_tokens = []
    for i in range(len(toks)):
        line:Token = toks[i]
        if line.type == NIL:
            splited_tokens = line.getErrs()
            for t in splited_tokens:
                line_tokens.append(t[0])
        else:
            line_tokens.append(line)
    return line_tokens



class Token:
    def __init__(self,expr, type = NIL, tokens = None):
        self.expr:str = expr
        self.type = type
        self.tokens  = tokens

    def isKeyword(self):
        return self.expr in keywords
    
    def isOperator(self):
        return self.expr in operators
    
    def isLabel(self):
        return True if self.expr.endswith(":") else False
    
    def math(self, token):
        if token.expr in maths[self.expr]:
            return True
        return False
    
    def getErrs(self):
        self.expr = self.expr.split(' ')
        
        if len(self.expr) == 1:
            return [[Token(self.expr[0],INVALID)]]
        arr = []
        for x in self.expr:
            arr.append(Tokenize(x))

        return arr