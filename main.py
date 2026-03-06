import flask
import os
from modules import *

os.makedirs("codes", exist_ok=True)
cods = os.listdir("codes")
codes = {}
for name in cods:
    data = read("codes/"+name)
    if data == "":
        os.remove("codes/" + name)
        continue
    codes[name] = data

app   = flask.Flask("INTERPRETER")
ROOT  = os.path.realpath("./gui")
saver = CodeSaver("codes/")

@app.route("/run")
def run():
    code = flask.request.args.get("code", "")
    name = flask.request.args.get("name", "")
    print("running code...")
    
    if code != codes[name]:
        codes[name] = code
        saver.save(name,code)

    exe = Executor(code)
    out = exe.run()
    print(out)
    return out,200
    
    
@app.route("/save")
def save(): 
    code = flask.request.args.get("code", "")
    name = flask.request.args.get("name", "")
    if code != codes.get(name):
        codes[name] = code
        saver.save(name,code)

    return {"status":"ok"},200


@app.route("/getcode")
def sendCode():
    name = flask.request.args.get("name", "")
    return {"status":"ok","code":codes.get(name, "")},200


@app.route("/")
def main():
    return response(ROOT+"/index.html")


@app.route('/gui/<path:subpath>')
def show_subpath(subpath):
    if ".." in subpath:
        return "Access denied", 403
    return response(ROOT+"/"+subpath)

@app.route("/getcodes")
def getcodes():
    name = flask.request.args.get("name", "")
    return {
        "status":"ok",
        "code"  : codes.get(name, "")
    }

@app.route("/initcodes")
def initcodes():
    names = []
    cods = []
    for name in os.listdir("codes"):
        code = read("codes/"+name)
        if code == "":
            continue``
        
        cods.append(name)
        

    for name in cods:
        names.append(name)
    
    res = {
        "status" : "ok",
        "names": names
    }

    return res,200

@app.route("/newcode")
def newcode():
    name = flask.request.args.get("name")
    res = {
        "status":"ok",
        "code": ""        
    }
    codes[name] = ""
    return res,200

app.run("0.0.0.0", 9000)