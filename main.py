import flask
import os
from modules import *
app     = flask.Flask("INTERPRETER")
ROOT    = os.path.realpath("./gui")
saver   = CodeSaver("src")
CODE    = saver.load()


@app.route("/run")
def run():
    global CODE
    code = flask.request.args.get("code","")
    if code != CODE:
        CODE = code
        saver.save(code)

    return response(ROOT+"/index.html")

@app.route("/save")
def save(): 
    global CODE
    code = flask.request.args.get("code", "")
    if code != CODE:
        CODE = code
        saver.save(code)
    return {"status":"ok"},200


@app.route("/getcode")
def sendCode():
    return {"status":"ok","code":CODE},200


@app.route("/")
def main():
    return response(ROOT+"/index.html")


@app.route('/gui/<path:subpath>')
def show_subpath(subpath):
    if ".." in subpath:
        return "Access denied", 403
    return response(ROOT+"/"+subpath)

app.run("0.0.0.0", 9000)