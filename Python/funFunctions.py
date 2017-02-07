
#Odd/Even
def odd_even():
  for i in range (1,2001):
    if i % 2 != 0:
      print "Number is " + str(i) + "." + " This is an odd number."
    if i % 2 == 0:
      print "Number is " + str(i) + "." + " This is an even numer."
odd_even()


#Multiply
def multiply(list,b):
  newlist =[]
  for i in list:
    i = i*b
    newlist.append(i)
  return newlist

print multiply([2, 4, 10, 16],5)

#Hacker Challenge
def layered_multiples(a, b):
  new_array = []
  for i in range(0, len(a)):
    arrA = []
    for i in range(0,a[i]):
      arrA.append(1)
    new_array.append(arrA)
  return new_array

x = layered_multiples([2, 4, 5], 3)
print x