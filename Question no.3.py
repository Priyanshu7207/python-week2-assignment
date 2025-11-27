words = ["apple", "banana", "apple", "orange", "banana", "banana"]

counts = {}
repeated = {}

for w in words:
    counts[w] = counts.get(w, 0) + 1

for item, freq in counts.items():
    if freq > 1:
        repeated[item] = freq

print(repeated)
