def square(number):
  return number*number
b=int(input("Enter a length of list"))
numbers = []
for i in range(b):
  c=int(input("enter a num"))
  numbers.append(c)
print("original list", numbers)  
squared_numbers_iterator = map(square, numbers)

squared_numbers = list(squared_numbers_iterator)
print("Square list",squared_numbers)