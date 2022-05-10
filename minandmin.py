def maxmin(a,b,c):
    if a>b:
        max=a
    else:
        max=b
    if max<c:
        max=c     
    return max
def minmax(a,b,c):
    if a<b:
        min=a
    else:
        min=b
    if min>c:
        min=c
    return min 
x=4
y=9
z=90
mx = maxmin(x,y,z)
#mi = minmax(x,y,z)
print(" max value is ", mx)
print("the min value is ", minmax(x,y,z))
