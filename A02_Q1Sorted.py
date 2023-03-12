n=int(input("enter range number "))
l=[]
for i in range(n):
        a=int(input("enter a number"))
        b=int(input("enter b number"))
        l.append((a,b))
l.sort(key=lambda a: a[-1])
print(l) 