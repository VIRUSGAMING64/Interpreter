from modules.generic.utils import *
from modules.interpreter.Lexer import *
from modules.interpreter.ExprParser import *
import json
import modules.interpreter.debug as debug
import os
from .structures import *
import logging
import threading as th
from modules.interpreter.auxiliar.utils import *

mtx = th.Lock()
RunningInstances : list[InterpreterInstance]= []



class InterpreterInstance():
    def __init__(self):
        self.output = {}

    def ExecuteCode(self,code):
        if not isinstance(code, str | dict):
            return {
                "Errors": ["code is invalid"],
                "result": ""
            }

        if code == "":
            return {"Errors": [], "result":""}

        memory = Memory()

        self.output = {
            "Errors": [],
            "result": "",
            "running": True
        }

        struct = None

        if isinstance(code,dict):
            struct = dict2Token(code)

        elif isinstance(code, str):
            lines    = Lexer(code, self.output).TokenizeSource()

            if debug.DEBUG:
                for line in lines:
                    for tok in line.tokens:
                        print(tok.expr , tok.type)

            s,struct = extract(self.output, memory, 0 , lines)

        if self.output["Errors"] == []:
            if debug.DEBUG:
                for i in struct.tokens:
                    print("debug:",i.expr, i.data.get("name", None))  
                
            code, res = Evaluator(struct, None, self.output, memory).run()
        
        self.output["running"] = False
        logging.log(logging.DEBUG,memory.mem)

        return self.output

    def kill(self):
        self.output["Killed"] = True

def Kill():
    outs = []

    for ins in RunningInstances:
        ins.kill()

    for ins in RunningInstances:
        while ins.output["running"]:
            time.sleep(0.100)
        outs.append(ins.output)

    return {"stoped":True, "outputs": outs} #* No se usa en el frontend esta por si luego hace falta
                                            #* Es innecesario ya que al running coge el output del hilo cerrado  

def ExecuteCode(code):
    mtx.acquire()
    id = len(RunningInstances)
    RunningInstances.append(InterpreterInstance())
    mtx.release()
    out = RunningInstances[id].ExecuteCode(code) 
    mtx.acquire()
    RunningInstances.pop(id)
    mtx.release()   
    return out
    