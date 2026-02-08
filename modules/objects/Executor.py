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
        for i in code:
            if i == "": continue #TODO esto se debe arreglar, lo deje asi por ahora
            print(Expression(i).Token().type)