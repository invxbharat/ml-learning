# file handling in python

try:
    file = open("resource/example.txt", "r") # open file in read mode
    content = file.read() # read the content of the file
    print(content)
except FileNotFoundError:
    print("Error: File not found")
finally:
    file.close() # close the file

# with statement automatically closes the file after the block of code is executed
try:
    with open("resource/example.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found")


# open() opens a file.
# read(), readline(), and readlines() are used to read data.
# write() writes data to a file.
# append mode ("a") adds data without deleting existing content.
# close() closes the file.
# Using with open(...) is the preferred approach because it automatically closes the file, even if an error occurs.



try:
    with open("resource/example.txt", "r") as file:
        content = file.readline()
        print(content)
except FileNotFoundError:
    print("Error: File not found")

try:
    with open("resource/example.txt", "a") as file:
        file.write("\nHello, World!")
        file.write("\nThis is a new line.")
except FileNotFoundError:
    print("Error: File not found")

# try:
#     with open("resource/example.txt", "w") as file:
#         file.write("Hello, World!")
#         file.write("\nThis is a new line.")
# except FileNotFoundError:
#     print("Error: File not found")

try:
    with open("resource/example.txt", "r") as file:
        content = file.readlines()
        for line in content:
            print(line)
except FileNotFoundError:
    print("Error: File not found")
