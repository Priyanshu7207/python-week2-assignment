def to_title_case(sentence):
    words = sentence.split()
    result = []

    for w in words:
        if w:
            result.append(w[0].upper() + w[1:])
        else:
            result.append(w)

    return " ".join(result)

print(to_title_case("hello world from python"))
