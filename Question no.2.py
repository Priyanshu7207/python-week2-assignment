sentence = input("Enter a sentence: ").strip()
words = sentence.split()

updated = []
for index, word in enumerate(words):
    if index % 2 == 1:
        updated.append(word[::-1])
    else:
        updated.append(word)

result = " ".join(updated)
print(result)
