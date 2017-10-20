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
