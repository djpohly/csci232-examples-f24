import collections

predict = collections.defaultdict(collections.Counter)

with open("/tmp/lw.txt") as f:
    all_text = f.read()

all_words = [w.strip("'\",;.").lower() for w in all_text.split()]
for first, second in zip(all_words, all_words[1:]):
    predict[first][second] += 1

print(predict["the"].most_common(20))
