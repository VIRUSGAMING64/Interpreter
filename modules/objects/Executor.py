from modules.utils import *
from .Expression import *
import json
import modules.objects.debug as debug

import os
from .structures import *
mem = Memory()

class Executor:
    def __init__(self,code = ""):
        self.code = code

    def func(self,start, lines):
        eofun,code = self.extract(start + 1, lines)
        try:
            fun = None
            fun = FUNCS(start,lines)
            fun.code = code
        except Exception as e:
            self.output["Errors"].append(str(e))
            print(e)
        
        return fun,eofun


    def control(self, start,lines):
        print(lines[start].expr)
        eoif,code = self.extract(start+1,lines)
        cond = None
        try:
            cond = IF(start,lines[start],code)
        except Exception as e:
            self.output["Errors"].append(str(e))
            
        print(start, eoif)
        assert eoif >= start
        return  cond,eoif


    def extract(self,start,lines):
        i = start
        structure = Token("__source_code__")
        structure.tokens = []

        while i < len(lines):
            line = lines[i]

            if line.tokens[0].expr == "if":
                cond,i = self.control(i,lines)
                if cond != None:
                    structure.tokens.append(cond.Token())
            
            elif line.tokens[0].expr == "while":
                pass

            elif line.tokens[0].expr == "func":
                func,i = self.func(i,lines)
                if func != None:
                    mem.alloc_func(func.name, func.novars, func.code)
                    structure.tokens.append(func.Token())
            else:
                print("added",line.expr)
                structure.tokens.append(line)
            
            if line.tokens[0].expr == "end":
                return i,structure
                        
            i   += 1 

        if start != 0:
            self.output["Errors"].append("Not closed structure")
        
        return i,structure 



    def run(self, code = None):
        global mem
        
        if code != None:
            self.code = code

        self.output = {
            "Errors": [],
            "result":""
        }
        print(self.code)
        self.code = self.code.replace("\t","  ")
        print(self.code)

        code = self.code.split("\n")


        lines = TokenizeSource(code,self.output)

        s,structure = self.extract(0,lines)
        
        self.output["result"] = "no syntaxis error"
        
        debug.dst(structure)


        return self.output