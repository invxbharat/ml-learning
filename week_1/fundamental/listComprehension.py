# execute imedetaly , indexing, filtering, mapping, and more
# syntax: [expression for item in iterable if condition]

square = [x*x for x in range(10)]
print(square)

even = [x for x in range(10) if x % 2 == 0]
print(even)



# genrator expression 
# sybtex: (expression for item in iterable if condition)
square_gen = (x*x for x in range(10))
for s in square_gen:
    print(s)

