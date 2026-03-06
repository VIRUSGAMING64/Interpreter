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
            "Errors": [],
            "result":""
        }

        code = self.code.split("\n")
        print(code)
        lines = []
        p = 0
        for line in code:
            p +=1
            if line == "": continue #TODO esto se debe arreglar, lo deje asi por ahora
            ex = Expression(line)
            print("-" * 8)
            line = ex.Token()
            for j in range(len(line.tokens)):
                if line.tokens[j].expr == "//":
                    line.tokens[j].type = COMMENT
                    line.tokens[j].tokens = line.tokens[j+1:]
                    del line.tokens[j+1:]
                    break

            for j in line.tokens:
                if j.type == INVALID:
                    output["Errors"].append(f"invalid token at line: {p}")
                print(j.type,j.expr)
                

            lines.append(ex)
        
        output["result"] = "no syntaxis error"
        return output