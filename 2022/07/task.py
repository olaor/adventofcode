#!/usr/bin/env python
import sys

class file:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)
        return

class folder:
    def __init__(self, parent = None, name = "/"):
        self.parent = parent
        self.name = name
        if parent:
            self.path = ("%s/%s" % (parent.path, name)).replace("//","/")
            self.parent.addsubfolder(self)
        else:
            self.path = name

        self.subfolders = {}
        self.files = {}
        self.size = 0

        return

    def addsubfolder(self, subfolder):
        self.subfolders[subfolder.name] = subfolder
        return

    def getsubfolder(self, name):
        subfolder = self.subfolders.get(name)
        if subfolder:
            return subfolder
        else:
            return folder(self, name)
        return

    def updatesize(self, size):
        self.size += size
        if self.parent:
            self.parent.updatesize(size)
        return


    def addfile(self, filedata):
        size, name = filedata.split()
        this = self.files.get(name)
        if this:
            return
        
        this = file(name, size)
        self.files[name] = this
        self.updatesize(this.size)

        return


folders = {}

def cd(cwd, path):
    if path == "..":
        return cwd.parent
    if cwd:
        return cwd.getsubfolder(path)

    this = folder(cwd, path)
    folders[this.path] = this
    return this

cwd = None
ls = False
for line in open(sys.argv[1]).readlines():
    line = line.strip()
    args = line.split()
    first = args[0]

    if args[0] == '$':
        ls = False
        cmd = args[1]
        if cmd == "cd":
            cwd = cd(cwd,args[2])
        if cmd == "ls":
            ls = True
        continue

    if ls:
        if first == "dir":
            continue
        else:
            cwd.addfile(line)

    pass


def traverse(cwd):
    if cwd.size < 100000:
        smalls.append(cwd)

    for subfolder in cwd.subfolders.values():
        traverse(subfolder)
    

def hunterkiller(cwd):
    sizes.append(cwd)
    for subfolder in cwd.subfolders.values():
        hunterkiller(subfolder)

        
    
start = folders["/"]
smalls = []
traverse(start)
    



partone = sum([f.size for f in smalls])

space = 70000000
free = 30000000
needed = space - free
delete = start.size - needed 
sizes = []
hunterkiller(start)

ordered = sorted(sizes, key=lambda x: x.size)


parttwo = False
for f in ordered:
    if f.size >  delete:
        parttwo = f.size
        break

print("Solution part one:")
print(partone)
print("Solution part two:")
print(parttwo)



