import collections

with open("/tmp/lw.txt") as f:
    all_text = f.read()

all_text = all_text.casefold()
all_words = all_text.split()
c = collections.Counter(all_words)

print(c.most_common(50))
