def square(number):
  return number *3
b=int(input("Enter a length of list"))
numbers = []
for i in range(b):
  c=int(input("enter a num"))
  numbers.append(c)
print("original List", numbers)  
squared_numbers_iterator = map(square, numbers)

squared_numbers = list(squared_numbers_iterator)
print("Triple List",squared_numbers)