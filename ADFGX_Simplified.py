# This kata is the first of the ADFGX Ciphers, the harder version can be foundhere.
# The ADFGX Cipher is a pretty well-known Cryptographic tool, and is essentially a modified Polybius Square.
#
# Rather than having numbers as coordinates on the table, it has the letters:
# A, D, F, G, X
#
# Also, because this is the first step, and to help simplify things,
# you won't have to worry about a key, or the corresponding columnar transposition. In this kata ;)
#
# All you have to do is encrypt and decrypt a string into ADFGX format.
#
# adfgx_encrypt() and adfgx_decrypt() will be passed a string, plaintext and ciphertext respectively,
# and an adfgxsquare, for which will guide the operations.
#
# Now for some examples to clear confusion:
#
# adfgx_encrypt("helloworld", "bchigklnmoqprstuvwxyzadef")
#     A D F G X
# A   b c h i g
# D   k l n m o
# F   q p r s t  -> square (PLEASE NOTE, j SHOULD BE TREATED AS i)
# G   u v w x y
# X   z a d e f
#
# "helloworld"   -> plaintext
#
# EVALUATES TO:
#
#       F
#           -> "AF"
# A     h
# --------------
#           G
#                -> "XG"
# X         e
#
# AND SO FORTH...
#
# Results in:
# adfgx_encrypt("helloworld", "bchigklnmoqprstuvwxyzadef") == "AFXGDDDDDXGFDXFFDDXF"
#
# Now decryption:
# adfgx_decrypt("FGXGADGDXGFXAXXGFGFGAADGXG", "aczlmuqngoipvstkrwfxhdbey)
#     A D F G X
# A   a c z l m
# D   u q n g o
# F   i p v s t  -> square (PLEASE NOTE, j SHOULD BE TREATED AS i)
# G   k r w f x
# X   h d b e y
#
# "FGXGADGDXGFXAXXGFGFGAADGXG"   -> ciphertext
# "FG" == "s"
# "XG" == "e"
#
# AND SO ON:
# adfgx_decrypt("FGXGADGDXGFXAXXGFGFGAADGXG", "aczlmuqngoipvstkrwfxhdbey) == "secretmessage"

def adfgx_encrypt(plaintext, square):
    key = ['A', 'D', 'F', 'G', 'X']
    ciphertext = ""
    if 'j' in plaintext and 'j' not in square:
        plaintext = plaintext.replace('j', 'i')
    if 'i' in plaintext and 'i' not in square:
        plaintext = plaintext.replace('i', 'j')
    for i in plaintext:
        a = square.index(i)
        ciphertext = ciphertext + key[int(a / 5)] + key[a % 5]
    print(ciphertext)

def adfgx_decrypt(ciphertext, square):
    key = ['A', 'D', 'F', 'G', 'X']
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a = key.index(ciphertext[i])
        b = key.index(ciphertext[i+1])
        plaintext = plaintext + square[(a * 5) + b]
    print(plaintext)

adfgx_encrypt("helloworld", "bchigklnmoqprstuvwxyzadef")
# Ans: "AFXGDDDDDXGFDXFFDDXF"
adfgx_decrypt("FGXGADGDXGFXAXXGFGFGAADGXG", "aczlmuqngoipvstkrwfxhdbey")

# adfgx_encrypt("wtsbnjoklzyfemuvqhapgcdrx", "qhgnvzocfewujptymrldskabx")

