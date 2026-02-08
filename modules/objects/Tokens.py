
NUMBER      = 0B00000001 #! 1
STRING      = 0B00000010 #! 2
FUNC        = 0B00000100 #! 4
NIL         = 0B00001000 #! 8
BOLEAN      = 0B00010000 #! 16
OPERATION   = 0B00100000 #! 32
KEYWORD     = 0B01000000 #! 64
LABEL       = 0B10000000 #! 128

operators =  [
    "+","-","*","/","**","!","&","|","^","=",")","(","{","}",";",".",",","//"
]

keywords = [
    "goto","if","else","while","fun","True","False"
]



class Token:
    def __init__(self,expr, type = NIL, opt = None):
        self.expr = expr
        self.type = type
        self.opt  = opt

    def isKeyword(self):
        return self.expr in keywords
    
    def isOperator(self):
        return self.expr in operators
    
    def isLabel(self):
        return True if self.expr.endswith(":") else False
    