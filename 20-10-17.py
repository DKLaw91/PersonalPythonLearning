https://www.learnpython.org/en/Conditions
_____________________________________________
x=[1,2,3]
y=[1,2,3]
print(x==y)
print(x is y)
print(x is x)
print(y is y)
print([1,2,3] is [1,2,3])

# 'not' inverts True & False
print(not x!=y) # x is not equal to y is True (actually False)
print(not x==y) # x is equal to y is False (actually True)

print('################')

number = 20
second_number = False
first_array = [1,0,0]
second_array = [1,2]

if number > 15: # number must be greater than 15
    print("1")

if first_array: # first_array must be True (contain something)
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
______________________________________________________________
https://www.learnpython.org/en/Loops

primes=[2,3,5,7]
for prime in primes:
  print(prime)
print()

for i in primes:
  print(i)
print()
  
for x in range(5): # prints 0-4
  print(x)
print()

for x in range(1,6): # prints 1-5
  print(x)
print()

# prints 1-5
count = 1
while count<=5:
  print(count)
  count+=1 # This is the same as count = count +1
print()

count=1
while True:
  print(count)
  count+=1
  if count==6:
    break
print()

# Prints out only odd numbers
for x in range(10):
  # check if x is even
  if x % 2 == 0: # if x divides by 2 with no remainder
    continue
  print(x)
print()

count=1
while count<6:
  print(count)
  count+=1
else:
  print("Count value reached: " + str(count))
print()

for i in range(1,10):
  if (i%6==0):
    break
  print(i)
else: # Obsolete instruction 
  print("This is not printed because for loop is terminated because of break but not due to fail in condition")
print()

numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527]
for i in numbers:
  if i == 237:
    break
  elif i % 2 == 0:
    print(i)
  
  

