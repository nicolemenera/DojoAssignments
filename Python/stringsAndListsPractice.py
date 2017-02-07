str = "If monkeys like bananas, then I must be a monkey!"
print str.replace("monkey", "alligator")

x = [2, 54, -2, 7, 12, 98]
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[7]
message = x[0] + " " + x[7]
print 

oldList = [19,2,54,-2,7,12,98,32,10,-3,6]
oldList.sort()

def remNegatives(arr):
  newList = []
  index = len(arr) - 1
  while index >= 0:
    if arr[index] < 0:
      newList.append(arr.pop(index))
    index = index - 1
  arr.insert(0,newList)
  print newList
remNegatives(oldList)

print "hello world"
print oldList