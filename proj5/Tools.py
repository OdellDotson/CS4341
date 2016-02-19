__author__ = 'odell'

def removeNonAscii(s):
    return "".join(i for i in s if ord(i)<126 and ord(i)>31) #This function will clear out formatting characters from strings.