
NUMBER = 0B00001 #! 1
STRING = 0B00010 #! 2
FUNC   = 0B00100 #! 4
NIL    = 0B01000 #! 8
BOLEAN = 0B10000 #! 16

operators =  [
    "+","-","*","/","**",
]

class Token:
    def __init__(self,expr, type = NIL, opt = None):
        self.expr = expr
        self.type = type
        self.opt  = opt