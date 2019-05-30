from sys import argv
script , file = argv

def printfile(f):
     print(f.read())

def rewind(f):
    f.seek(0)

def printaline(line,f):
    print(line, f.readline())

f = open(file)

printfile(f)
print("\n")
rewind(f)
line = 1
printaline(line, f)
printaline(line+1 , f)
