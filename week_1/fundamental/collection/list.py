# Collections

##List -- Mutable -- duplicate -- ordered

numbers = [1,2,3,4,5]
names= ['bharat', 'ABC', 'XYZ']

print(numbers)
print(names)

### Positive Index
print(names[0])
print(names[1])
print(names[2])

### Negative index (reverse)
print(names[-1])
print(names[-2])
print(names[-3])

### length
print(len(names))

for i in range(len(names)):
    print(names[i])


### Add

#### insert at specific position
names.insert(1, "567")

print(names)

#### append at last
names.append('last')
print(names)

### Update

names[1] = "opps"

### Remove

#### Remove By value
names.remove("last")
print(names)


#### pop by position
names.pop(1)
print(names)

### contains

print("bharat" in names)

print("bharat" not in names)

## Iterate

### For Each

for name in names:
    print(name)

### with value and index

for index, value in enumerate(names):
    print(f'index: {index} value: {value}')

for index, value in enumerate(names):
    print("index:", index, "value:", value)


## Extend List (like addAll in java)

names2 = ['test', 'code']

names.extend(names2)

print(names)


## Sort

names.sort()
print(names)

names.sort(reverse=True)
print(names)


## Reverse
names.reverse()
print(names)


## Copy
copy = names.copy()
print(copy)

## count

print(copy.count('bharat'))

## clear

copy.clear()
print(copy)

## Index

print(names.index('bharat'))


## Slicing

print(names[:3])
print(names[1:3])
print(names[-2:])
print(names[:-2])

## function
numbers = [12,2,2,2,1,4,4,4,1,2,4,2,1,1,2]

print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))