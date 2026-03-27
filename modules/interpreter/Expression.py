from modules.interpreter.Tokens import *
from modules.generic.utils import *
from modules.interpreter.memory import *
from modules.interpreter.Exceptions import *
import time
class Expression:
    def __init__(self, expr = None, memory=None):
        self.expr:str = expr
        self.type     = None
        self.memory = memory

    def Token(self):
        self.expr = cleanStr(self.expr)
        res = Tokenize(self.expr)
        return Token(self.expr, LINE, res)
    
    def __dict__(self):
        return {
            "expr":self.expr,
            "type":self.type
        }
    
    def evalstr(self):
        toks    = self.Token()
        return self.evalTokens(toks)

    def evalTokens(self, toks):
        try:
            return self._evalTokens(toks)
        except Exception as e:
            print(e)
            line = None if isinstance(toks, list) else toks.data["line"]
            raise ArithmeticException(line, str(e))


    def funcat(self, i , tokens):
        opens = 1
        args = []
        arg = []
        for j in range(i+2, len(tokens)):
            if tokens[j].expr == "(":
                opens += 1
                arg.append(tokens[j])
            
            elif tokens[j].expr == ",":
                if opens == 1:    
                    args.append(arg)
                    arg = []
                else:
                    arg.append(tokens[j])

            elif tokens[j].expr == ")":
                opens -= 1
                arg.append(tokens[j])
            
            else:
                arg.append(tokens[j])

            if opens == 0:
                arg.pop()
                args.append(arg)
                return j,args
        
        raise Exception("Not closed function call !!")

    def extract_funcs_call(self,toks):
        tokens:list = toks.tokens
        for i in range(len(tokens)):
            if i + 1 >= len(tokens):
                break
            
            if tokens[i].type == VARIABLES and tokens[i + 1].expr == "(":
                eofc,args = self.funcat(i,tokens)
                if eofc == None:
                    raise Exception("Func call not closed")
                func = Token("__func__", FUNCCALL, []) 
                func.data["args"] = []
            
                for arg in args:
                    func.data["args"].append(arg)
                del tokens[i : eofc + 1]
                tokens.insert(i, func)

    def _evalTokens(self,toks):
        if isinstance(toks, list):
            toks = Token("__sourcecode__", LINE , toks)
        
        nums    = []
        oper    = []
        unary   = True 

        self.extract_funcs_call(toks)

        for elem in toks.tokens:
            
            if elem.type == FUNCCALL:
                for arg in elem.data["args"]:
                    for ex in arg:
                        print(ex.expr, end=" ")
                print('')
                continue

            if elem.type == COMMENT:
                continue
            
            if elem.type == VARIABLES:
                elem.expr = self.memory.query(elem.data["name"])

            if elem.expr == "(":
                oper.append(elem)
                unary = True
            
            elif elem.expr == ")":
                while oper[-1].expr != "(":
                    self.process(nums, oper)
                
                oper.pop()
                unary = False

            elif is_operator(elem.expr):
                if unary and is_unary(elem.expr):
                    elem.data["neg"] = True
                
                while (len(oper)>0 and (
                        ((getPrio(oper[-1]) >= getPrio(elem)) and (elem.data.get("neg",False) >= 0)) or
                        (elem.data.get("neg",False) < 0 and ((getPrio(oper[-1])) >= getPrio(elem)))
                    )):
                    
                    self.process(nums, oper)

                unary = True
                oper.append(elem)
            else:
                unary = False
                nums.append(elem)
        
        while len(oper):
            self.process(nums,oper)

        return nums,oper

    def process(self, nums, oper):
        a = nums.pop()
        opp = oper.pop()
        if opp.data.get("neg", False):
            nums.append(
                Token(UnaryOP(a,  opp), NUMBER)
            )
            return
        b = nums.pop()        
        n = process_op(a, b, opp, self.memory)
        nums.append(Token(n, NUMBER))


def TokenizeSource(code,output):
        lines = []
        p = 0
        for line in code:
            p +=1
            if line == "": 
                continue
            
            ex = Expression(line)
            print("-" * 8)
            line = ex.Token()
            line.put("line", p)
            lines.append(line)
            for j in range(len(line.tokens)):
                if line.tokens[j].expr == "//":
                    line.tokens[j].type = COMMENT
                    line.tokens[j].tokens = line.tokens[j+1:]
                    del line.tokens[j+1:]
                    break

                if line.tokens[j].type == KEYWORD and j != 0:
                    output["Errors"].append(f"keyword not in the start of line [{p}]")
                    break

            for j in line.tokens:
                if j.type == INVALID:
                    output["Errors"].append(f"invalid token at line: {p}")
                print(j.type,j.expr)
        
        return lines
