gift_list = [
    "fruitcake",
    "partridge in a pear tree",
    "turtle doves",
    "french hens",
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

i = 0
while i < len(gift_list) - 1:
    smallest_j = i
    j = i + 1
    while j < len(gift_list):
        if gift_list[j] < gift_list[smallest_j]:
            smallest_j = j
        j += 1
    temp = gift_list[smallest_j]
    gift_list[smallest_j] = gift_list[i]
    gift_list[i] = temp
    i += 1

print(gift_list)
