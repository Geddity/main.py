def all_variants(text):
    length = len(text)

    for stop in range(1, length + 1):
        for start in range(length - stop + 1):
            yield text[start:start + stop]

a = all_variants("abc")
for i in a:
    print(i)