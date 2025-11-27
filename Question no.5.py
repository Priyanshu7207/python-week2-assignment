words = ["This", "is", "good", "is"]

freq = {}

for w in words:
    key = w.lower()
    freq[key] = freq.get(key, 0) + 1

print(freq)
