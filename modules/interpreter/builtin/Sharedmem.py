import time
from types import *
import modules.interpreter.debug as debug


shared_memory = {

}


def newmemory():
    key = hex(time.time_ns())
    shared_memory[key] = {}
    return  key

def memget(key, idx):
    try:
        if debug.DEBUG:
            print("getting",key, idx, shared_memory[key][idx])
        return shared_memory[key][idx]
    except Exception as e:
        raise Exception("Unallocated memory address")

def malloc(key,size,value):
    try:
        if not isinstance(key , str):
            raise Exception("Key not found")
        for i in range(size):
            shared_memory[key][i] = value
    except Exception as e:
        raise e
    
def memset(key, idx, value):
    try:
        if(idx >= len(shared_memory[key])):
            raise Exception("Unallocated memory address") 
        if debug.DEBUG:
            print("Allocated in",key,idx, value)
        shared_memory[key][idx] = value
    except Exception as e:
        if isinstance(e, KeyError):
            raise Exception("Key not found")
        raise e