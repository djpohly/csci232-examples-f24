def factor_dict1(n):
    result = {}
    for factorme in range(1, n + 1):
        factorlist = []

        for candidate in range(1, factorme + 1):
            if factorme % candidate == 0:
                factorlist.append(candidate)

        result[factorme] = factorlist
    return result

def factor_dict2(n):
    return {
        factorme: [
            candidate
            for candidate in range(1, factorme + 1)
            if factorme % candidate == 0
        ]
        for factorme in range(1, n + 1)
    }


jokes = {}
#with open("tomswifties.txt", "r") as f:
with open("tomswifties.txt") as f:
    for line in f:
        line = line.strip()
        # words = line.split()
        # key = words[-1][:-1]

        setup, adverb = line.split("he said")
        setup = setup.strip('",. ')
        adverb = adverb.strip('",. ')
        jokes[adverb] = setup

with open("taylorswifties.txt", "w") as out:
    for k, v in jokes.items():
        print('"' + v + '," she said, ' + k + '.', file=out)

# f = open("tomswifties.txt")
# print(f)
# f.close()
