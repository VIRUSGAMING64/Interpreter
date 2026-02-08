import mimetypes
import flask

def read(path, mode = "r"):
    file = open(path,mode)
    data = file.read(2**30)
    file.close()
    return data

def getmimetype(path):
    return mimetypes.guess_type(path)[0]

def response(file):
    return flask.Response(read(file), mimetype=getmimetype(file))

def CleanCode(code):
    b = True
    ncode = ""
    for c in code:
        if c == " " and b:
            continue
        if c == "\"" or c == "\'":
            b = not b
        ncode += c
    return ncode