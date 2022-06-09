seqno=5000
class student():
    
    def __init__(self,name,age,marks):
        global seqno
        self.name=name
        self.age = age
        self.marks= marks
        self.roll = seqno
        seqno=seqno+1
    
def toppereldest(x):
        i=0
        hmarks=0
        eldest = 0
        
        while i<len(x):
            if hmarks<x[i].marks:
                hmarks=x[i].marks
                h_index=i
            if eldest<x[i].age:
                eldest = x[i].age
                e_index=i
            i=i+1
        return(x[h_index],x[e_index])
                
    
        
s4=student('bob',25,99)
s1=student('charan',28,98)
s3=student('revanth',18,95)
s2=student('teja',30,89)


s=[s1,s2,s3,s4]

topper,eld=toppereldest(s)
print("The eldest is:", eld.name,eld.roll )
print("The topper is:",topper.name,topper.roll)