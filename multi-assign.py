x, y = 10, 12
print(x)
print(y)

x, y = y, x
print(x)
print(y)


d = {}
d[3] = "three"
d[5] = "five"
d[8] = "twelve"
d[20] = "d&d"


for k, v in d.items():
    print("key is " + str(k) + " and value is " + str(v))

print("----")

# Dictionary literal
d = {10: "ten",  20: "twenty",  30: "thirty"}
for k, v in d.items():
    print("key is " + str(k) + " and value is " + str(v))



l = ["hello", "there", "world", "what's", "up"]
for i, s in enumerate(l):
    print("index " + str(i) + " is " + str(s))

l2 = ["for", "the", "beauty", "of", "the", "earth"]
# for a, b in zip(l, l2):
#     print(a + " / " + b)

for a, b in zip(l2, l2[1:]):
    print(a + " / " + b)

s = "hello world"
for a, b in zip(s, s[1:]):
    print(a + b)


# Comprehensions

my_set = {x * x for x in range(100)}
my_set_as_a_list = list(my_set)

list2 = [x * x for x in range(100) if x % 2 == 0]


dcomp = {n: n **2 for n in range(100) if n % 2 == 0}
