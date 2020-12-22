import sys,math
c=100
# e=int(c*math.trunc(float(sys.argv[1])*c)/c)
e=int(math.trunc(float(sys.argv[1])*c))
l=[]
a=l.append
for d in[200,c,50,20,10,5,2,1]:
 if d>e:continue
 if d==e:
  a(d/c)
  break
 f,e=divmod(e,d)
 for _ in range(f):a(d/c)
 if e==0:break
print(l)