def suml(list):
        l=[]
        sum=0
        for i in range(list):
            num=int(input("Enter a number:"))
            l.append(num)
        print("list:",l)
        for i in l:
         sum=sum+i
        print("Total of list:",sum)       
a=int(input("How many numbers:"))
suml(a)