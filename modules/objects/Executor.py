from modules.utils import *
from .Expression import *
import json




class Executor:
    def __init__(self,code = ""):
        self.code = code

    def run(self, code = None):
        if code != None:
            self.code = code
        output = {
            "SyntaxErros":None,
            "Errors": None,
            "result":""
        }

        code = self.code.split("\n")
        print(code)
        lines = []
        errors = []
        p = 0
        for i in code:
            p +=1
            if i == "": continue #TODO esto se debe arreglar, lo deje asi por ahora
            ex = Expression(i)
            print("-" * 8)
            line = ex.Token()
            for j in line.tokens:
                if j.type == INVALID:
                    errors.append(p)
                print(j.type,j.expr)
                

            lines.append(ex)
        
        output["SyntaxErros"] = errors
        output["result"] = "no syntaxis error"
        return output