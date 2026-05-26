def strcmp(Str1, Str2):
    print(Str1, Str2)
    n = min(
        len(Str1),
        len(Str2)
    )
    for i in range(n):
        if (Str1[i] < Str2[i]):
            return -1
        elif (Str2[i] < Str1[i]):
            return 1
    if len(Str1) < len(Str2):
        return -1
    
    if len(Str2) < len(Str1):
        return 1
    
    return 0

def strcp(Str1, Str2):
    return Str1 + Str2

def newstr():
    return ""

def isS1inS2(s1, s2):
    return int(s1 in s2)
