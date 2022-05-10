class camera:
    def __init__(self, name, version, id):
        self.name = name
        self.version = version
        self.id = id

    def display(self,name,version,id):
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
while True:
        line = f.readline()
        print("line")
        if line == '':
            print('end is here', )
            break
        else: 
           a.append(line)
           tokens = line.split()
           print(tokens)
           c = camera(tokens(0), tokens(1), tokens(2))
           cameralist.append(c)
for c in cameralist:
    print("this is camera name", c.name)


