class camera:
    def __init__(self, n, v, id):
        self.name = n
        self.version = v
        self.id = id

    def display(self):
        print(self.name)
        print(self.version)
        print(self.id)


a =[]
f = open("samplefile.txt")
a.append("charan")
f = open("samplefile.txt")

a =[]
x = 0
cameralist=[]
linenumber=0
while True:
    linenumber=linenumber+1
    line = f.readline()
    print("line")
    if line == '':
        print('end is here', )
        break
    else: 
        a.append(line)
        tokens = line.split()
        if len(tokens)!= 3:
            print("There is an error")
            print(" error is an ", linenumber)
            exit()
        c = camera(tokens[0], tokens[1], tokens[2])
        cameralist.append(c)
        
for c in cameralist:
    #print("this is camera name", c.name)
    if c.name.find("hall") >= 0:
        print("found camera")
        c.display()
    



