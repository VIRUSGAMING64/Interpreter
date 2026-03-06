class CodeSaver:
    def __init__(self,path):
        self.path = path
    
    def save(self, name, code:str):
        print(code)
        f = open(self.path + name, "wb")
        f.write(code.encode())
        f.close()
    
    def load(self,name):
        try:
            f = open(self.path + name, "r")
            data=f.read(2**30)
            f.close()
            return data
        except:
            return ""