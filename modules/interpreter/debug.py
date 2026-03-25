
from .Tokens import Token

def dst(structure:Token,prof = 0):
    print(prof * " ",end = "")
    print(structure.expr)
    assert(isinstance(structure.expr,str|int|bool))
    if structure.tokens == None:
        return
    
    print("-"*40)   

    
    for sub in structure.tokens:
        dst(sub, prof+1)

def audit_memory(mem):
    for addr in mem.mem:
        print(addr, mem.query(addr))