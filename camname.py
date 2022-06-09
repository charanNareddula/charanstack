
class camera:
    def __init__(self, n, v, id):
        self.name = n
        self.version = v
        self.id = int(id)

    def display(self):
        print(self.name)
        print(self.version)
        print(self.id)
def mymax(a):
    i=0
    max=0
    while i<len(a):
        max = a[i].id
        i= i+1
    return(max)


a =[]
f = open("samplefile.txt")
a.append("charan")
f = open("samplefile.txt")

a =[]
x = 0
cameralist=[]
linenumber=0
mydic={} 

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
        mydic[c.name] = c
 
'''for c in cameralist:
    #print("this is camera name", c.name)
    if c.name.find("hall") >= 0:
        print("found camera")
        c.display()'''
c = mydic.get('livingroom')
if c == None:
    print(" cam not found")
else :
    print(c.id)
#Finding highest camera id using while and for loops
maxcam= mymax(cameralist)
print(" the max cam id is ",maxcam)






