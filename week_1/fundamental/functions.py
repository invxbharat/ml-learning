# functions and lamda expressions

# def add(x, y):
#     return x + y

def add(x, y=10):
    return x + y;

print(add(5, 11));
result = add(5);
print(result);


result = lambda x, y=10: x + y;
print(result(5, 11));
print(result(5));

mul = lambda x: x * x;
print(mul(5));


max = lambda x, y: x if x > y else y;
print(max(5, 10));

# lamda with for

test = [1, 2, 3, 4, 5];
result = list(map(lambda x: x * 2, test));
print(result);

result = list(filter(lambda x: x % 2 == 0, test));
print(result);

result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, test)));
print(result);

result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, test)));
print(result);

print( list(map(lambda x: x, test)))