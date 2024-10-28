# Strings are "strings" of characters to form text

a = "hello"
b = " world"
c = a + b

print(c)
print(len(c))
print(a * 5)

print(c[0])
print(c[7])
print(c[6:])
print(c[:8])
print(c[3:8])

name = input("What's your name? ")
number = input("Pick a number! ")
i = 0
while i < int(number):
    print("Hello, " + name)
    i = i + 1

