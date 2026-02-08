class CodeSaver:
    def __init__(self,path):
        self.path = path
    
    def save(self, code:str):
        print(code)
        f = open(self.path, "wb")
        f.write(code.encode())
        f.close()
    
    def load(self):
        f = open(self.path, "r")
        data=f.read(2**30)
        f.close()
        return data