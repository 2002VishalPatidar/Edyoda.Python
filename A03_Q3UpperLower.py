def suml(list):
    u,l=0,0
    for i in list:
      if(i.isupper()):
         u+=1
      elif(i.islower()):
         l+=1
      else:
         pass     
    print("Upper case characters:",u)
    print("Lower case characters:",l)         
a=input("Enter a string")
suml(a)