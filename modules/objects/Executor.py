from modules.utils import *
from .Expression import *


class Executor:
    def __init__(self,code = ""):
        self.code = code

    def run(self, code = None):
        if code != None:
            self.code = code

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
    
        if len(errors) != 0:
            print(errors)
            raise "errors sintaxis"