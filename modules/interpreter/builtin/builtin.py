import os
from math import *
import time as pytime
import random
from .Sharedmem import *
from .strings import *
"""
source of __builtin__ functions
"""

def _time():
    return pytime.time_ns()

def _sleep(ms):
    return pytime.sleep(ms / 1000) 

def _getcwd():
    return os.getcwd()

def _random(a, b):
    return random.randint(a, b)

def dbg(a):
    print(a)

__builtins_funcs__ = [
    [
        "_time", []
    ],
    [
        "_sleep", ["ms"]
    ],
    [
        "_getcwd", []
    ],
    [
        "malloc", ["key" , "addr", "value"]
    ],
    [
        "memset", ["key", "addr", "value"]
    ],
    [
        "newmemory", []
    ],
    [
        "memget", ["key" , "addr"]
    ],
    [
        "newstr", []
    ],
    [
        "strcp", ["Str1","Str2"]
    ],
    [
        "strcmp", ["Str1","Str2"]
    ],
    [
        "_random", ["a", "b"]
    ],
    [
        "dbg", ["a"]
    ],
    [
        "dumpshared", []
    ],
    [
        "free",["key"]
    ]
]

__builtins_calls__ = {
    "_time"     : _time,
    "_getcwd"   : _getcwd,
    "_sleep"    : _sleep,
    "_random"   : _random,
    "strcmp"    : strcmp,
    "newstr"    : newstr,
    "strcp"     : strcp,
    "isS1inS2"  : isS1inS2,
    "malloc"    : malloc,
    "newmemory" : newmemory,
    "memset"    : memset,
    "memget"    : memget,
    "dumpshared": dumpshared,
    "free"      : free
}