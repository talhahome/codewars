# Write a function that will return the count of distinct case-insensitive alphabetic characters and
# numeric digits that occur more than once in the input string.
# The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
def duplicate_count(text):
    text = str(text.lower())
    a = list(text)
    seen = []
    duplicate = []
    for i in range(0, len(a)):
        if a[i] not in seen:
            seen.append(a[i])
        else:
            if a[i] not in duplicate:
                duplicate.append(a[i])
    return len(duplicate)

text = 'Indivisibilities'

print(duplicate_count(text))