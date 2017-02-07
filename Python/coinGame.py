import random


heads = 1
tails = 2
headCount = 0
tailCount = 0
count = 0
print "Starting the program..."

for count in range(1, 5000):
  toss = random.randrange(1, 3)
  if toss == 1:
    headCount += 1
    count +=1
    print "Attempt #" + str(count) + ": Throwing a coin... It's a head! ... Got " + str(headCount) + " head(s) so far and " + str(tailCount)  + " tails(s) so far"
  elif toss == 2:
    tailCount += 1
    count +=1
    print "Attempt #" + str(count) + ": Throwing a coin... It's a tails! ... Got " + str(tailCount) + " tail(s) so far and " + str(headCount) + " head(s) so far"
print "Ending program, thank you!"





  

