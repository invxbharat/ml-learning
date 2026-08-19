x = 10;
if x > 5:
    print("x is greater than 5")

if x < 5 and x > 0:
    print("x is between 0 and 5")

if x < 5 or x > 0:
    print("x is either less than 5 or greater than 0")

if x not in [1, 2, 3, 4, 5]:
    print("x is not in the list [1, 2, 3, 4, 5]")

if x!= 5:
    print("x is not equal to 5")

if x == 10:
    print("x is equal to 10")

if x >= 10:
    print("x is greater than or equal to 10")

if x <= 10:
    print("x is less than or equal to 10")

if x == 5:
    print("x is equal to 5")
else:
    print("x is not equal to 5")

if x == 6:
    print("x is equal to 6")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is neither 6 nor 5")

# loop control structures
for i in range(5):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(0, 10, 2): # step value of 2
    print(i)

for i in range(10, 0, -1): # step value of -1
    print(i)

for i in range(10): # loop control structures with break and continue
    if i == 5:
        break
    print(i)

for i in range(10):
    if i == 5:
        continue
    print(i)

while x > 0:
    print(x)
    x -= 1


# match case control structure
x = 3
match x:
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3:
        print("x is 3")
    case _:
        print("x is not 1, 2 or 3")