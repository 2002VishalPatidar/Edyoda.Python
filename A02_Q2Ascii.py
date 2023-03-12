n=int(input("enter range number"))
d={}
z='`'
for i in range(n):
    key=(chr(ord(z)+1))
    z=key
    value=(ord(key))
    d[key] = value
print(d)  