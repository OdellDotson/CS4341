#Odell Dotson and Ethan Prihar, ocdotson@wpi.edu ebprihar@wpi.edu, Intro to AI Project 5

def removeNonAscii(s):
    return "".join(i for i in s if ord(i)<126 and ord(i)>31) #This function will clear out formatting characters from strings.

#I honestly expected to need to make more functional tools than this. I feel silly for making a file for this.