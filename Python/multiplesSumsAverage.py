for count in range (0, 1000):
  if count % 2 != 0:
    print count
  count += count


for num in range (5, 1000000):
  if num % 5 == 0:
    print num
  num += 5



a = [1, 2, 5, 10, 255, 3]
total = 0
for item in a:
  total += item
print total

a = [1, 2, 5, 10, 255, 3]
total = 0
for item in a:
  total += item
avg = total/len(a)
print avg


