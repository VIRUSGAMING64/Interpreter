from modules.utils import *
from .Expression import *

class Executor:
    def __init__(self,code = ""):
        self.code = code
        self.run()

    def run(self, code = None):
        if code != None:
            self.code = code
        self.code = CleanCode(self.code)
        code = self.code.split("\n")
        print(code)
        for i in code:
            if i == "": continue #TODO esto se debe arreglar, lo deje asi por ahora
            ex = Expression(i)
            print("-" * 8)

            if ex.Token().type == FUNC:
                for j in ex.Token().opt:
                    print(j.type,j.expr)
            else:
                print(ex.Token().type,ex.Token().expr)

            print("-" * 8)
