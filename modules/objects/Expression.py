from .Tokens import *


class Expression:
    def __init__(self, expr):
        self.expr:str = expr
        self.type     = None

    def eval(self):
        pos = 0
        act_tok = ""
        toks = []

        while pos <= len(self.expr):
            if pos < len(self.expr) and not self.expr[pos] in operators:
                act_tok += self.expr[pos]
            else:
                toks.append(Token(act_tok,NIL))
                if toks[len(toks) - 1].isKeyword():
                    toks[len(toks) - 1].type = KEYWORD
                elif toks[len(toks) - 1].isLabel():
                    toks[len(toks) - 1].type = LABEL
                
                if pos == len(self.expr):
                    break

                act_tok = ""
                toks.append(Token(self.expr[pos], OPERATION))

            pos += 1


        return toks if toks != None else None
    
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