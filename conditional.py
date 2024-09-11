def privileges(age):
    if age >= 8:
        print("use scissors unsupervised")
    if age >= 16:
        print("Driver's license")
    if age >= 18:
        print("LOC Card")
    if age >= 21:
        print("Adopt")
    if age >= 25:
        print("Rent a car")

def best_privilege(age):
    if age >= 25:
        return "Rent a car"
    elif age >= 21:
        return "Adopt"
    elif age >= 18:
        return "LOC Card"
    elif age >= 16:
        return "Driver's license"
    elif age >= 8:
        return "use scissors unsupervised"
    else:
        return "breathe"


my_age = int(input("What age are you? "))
if my_age < 0:
    print("Looking forward to meeting you when you exist")
else:
    # str() int()
    best = best_privilege(my_age)
    print("You can " + best)
