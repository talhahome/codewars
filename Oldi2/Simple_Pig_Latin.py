# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.
#
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(z):
    z = z.split(' ')
    for i in z:
        if i.isalpha():
            j = i[1:] + i[0] + 'ay'
            z[z.index(i)] = j
    return ' '.join(z)

print(pig_it('Pig latin is cool'))
# igPay atinlay siay oolcay
print(pig_it('Hello world !'))
# elloHay orldway !
