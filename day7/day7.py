class Directory():
    def __init__(self, name, parent):
        self.name = name
        self.subObjects = []
        self.parent = parent
    def getSize(self):
        size = 0
        for file in self.subObjects:
            if isinstance(file, File):
                size += file.size
            else:
                size += file.getSize()
        return size
    def get_sub_dirs(self):
        sub_dirs = []
        for file in self.subObjects:
            if isinstance(file, Directory):
                sub_dirs.append(file)
                sub_directories = file.get_sub_dirs()
                if sub_directories != []:
                    sub_dirs.extend(sub_directories)
        return sub_dirs

class File():
    def __init__(self, size, name):
        self.size = size
        self.name = name
    def getSize(self):
        return self.size

def parseFileDirectory(command, fileStruc):
    if command[0] == "dir":
        return Directory(command[1], fileStruc)
    else:
        return File(int(command[0]), command[1])

with open("day7.txt", "r") as file:
    command = file.readline().rstrip('\n').split(" ")
    while command != ['']:
        useEffort = True
        if command[0] == "$":
            if command[1] == "cd":
                if command[2] == "/":
                    fileStructure = Directory("/", None)
                elif command[2] == "..":
                    fileStructure = fileStructure.parent
                else:
                    fileStructure = next(x for x in fileStructure.subObjects if x.name == command[2])
            elif command[1] == "ls":
                command = file.readline().rstrip('\n').split(" ")
                while command[0] != "$":
                    if command == ['']:
                        break
                    fileStructure.subObjects.append(parseFileDirectory(command, fileStructure))
                    command = file.readline().rstrip('\n').split(" ")
                continue
        command = file.readline().rstrip('\n').split(" ")
while fileStructure.parent != None:
    fileStructure = fileStructure.parent
# DAY 1
# total = 0
# for direc in fileStructure.get_sub_dirs():
#     if direc.getSize() < 100000:
#         total += direc.getSize()
#     print(direc.name, direc.getSize())
# print(total)

# DAY 2
unused_space = 70000000 - fileStructure.getSize()
space_needed = 30000000 - unused_space

print(space_needed)
best_result = space_needed
best_dir = "/"
for direc in fileStructure.get_sub_dirs():
    if direc.getSize() > space_needed:
        diff = direc.getSize() - space_needed
        if diff < best_result:
            best_result = diff
            best_dir = direc
print(best_dir.getSize(), best_dir.name)

# DONT WORRY IT ACTUALLY WORKS ITS A BIT OF A MESS BUT IT WORKS