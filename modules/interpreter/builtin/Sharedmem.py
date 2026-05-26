import time
from types import *

addr = {

}


def newmemory():
    key = hex(time.time_ns())
    addr[key] = {}
    return  key

def malloc(key,size,value):
    try:
        if not isinstance(key , str):
            raise Exception("Key not found")
        for i in range(size):
            addr[key][i] = value
    except Exception as e:
        raise e
    
def memset(key, idx, value):
    try:
        if(idx >= len(addr[key])):
            raise Exception("Unallocated memory address") 
        addr[key][idx] = value
    except Exception as e:
        if isinstance(e, KeyError):
            raise Exception("Key not found")
        raise e