def ordinal_suffix(n):
    assert n >= 0
    if n >= 100:
        return ordinal_suffix(n % 100)
    if n == 1:
        return "st"
    elif n == 2:
        return "nd"
    elif n == 3:
        return "rd"
    elif n < 20:
        return "th"
    else:
        return ordinal_suffix(n % 10)

def plural_word(base, n):
    assert n >= 0
    if n == 1:
        return base
    return pluralize(base)

def pluralize(s):
    if s[-1:] == "y":
        return s[:-1] + "ies"
    elif s[-1:] == "s" or s[-1:] == "x":
        return s + "es"
    return s + "s"

gift_list = [
    "fruitcake",
    "partridge in a pear tree",
    "turtle doves",
    "French hens",
    "call...ing? birds",
    "golden rings",
    "geese a-laying",
    "swans a-swimming",
    "maids a-milking",
    "ladies dancing",
    "lords a-leaping",
    "pipers piping",
    "drummers drumming"
]

for day in range(1, 13):
    print("On the " + str(day) + ordinal_suffix(day) + " day of Christmas my true love gave to me:")
    gift_day = day
    while gift_day > 0:
        print(str(gift_day) + " " + gift_list[gift_day])
        gift_day -= 1
