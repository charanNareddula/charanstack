from subprocess import list2cmdline
from turtle import st


class student:
    
    def __init__(self,name, age):
        self.name = name
        self.age = age +100

        #self.fees = 0
    def display(self):
        print(self.name)
        print(self.age)
        print("......................")
        

    
s1 = student ("charan", 28)
s2 = student(" teja", 212)
'''s1.age=56
s1.name="dsdsdds"
s1.display()'''

print(s1.name)

list = []

list.append(s1)
list.append(s2)

list.append(student( "xyz", 21))
list.append(student('amit', 90))
list.append(student('yoga', 87))

#mydic = {'charan': s1, 'teja' : s2}
mydic = {}

mydic['charan']=s1
mydic['xyz'] =s2

print(mydic)

for key,value in mydic.items():
    print(key, ' : ', value.age)
s=mydic['xyz']
print(s.age)