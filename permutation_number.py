#!/usr/bin/env python3

from random import shuffle

# Hard coded for permutations of 0..255.  Non-optimized O(n²) implementation.
#
# This program demonstrates that a permutation of {0, 1, .., 255} can be
# encoded in a 211 byte string and then decoded, producing the original
# permutation.
#
# The encode function genrates the permutation number for the permutation
# and converts it to an array of bytes.  The decode function takes the
# array of bytes, converts it back to a permutation number, and then
# recreates the permutation.

x256 = [x for x in range(256)]

def encode_permutation(perm):
    perm = perm.copy()
    enco = x256.copy()
    for i in range(256):
        element = perm[i]
        perm[i] = enco[element]
        for j in range(element, 256):
            enco[j] -= 1

    perm_num = 0
    for i in range(255):
        perm_num += perm[i]
        perm_num *= (255 - i)

    return perm_num.to_bytes(211)

def decode_permutation(encoded):
    perm_num = int.from_bytes(encoded)
    perm = []
    for i in range(1,257):
        perm.append(perm_num % i)
        perm_num //= i
    perm.reverse()

    deco = x256.copy()
    for i in range(256):
        element = perm[i]
        perm[i] = deco[element]
        del deco[element]

    return perm


## Straightforward test:  Generate a large number of permutations and verify
## that they can round-trip through encode and decode.  The code also verifies
## that the encoded data is 211 bytes.

fail = False

for x in range(100000):
    orig_perm = [x for x in range(256)]
    shuffle(orig_perm)
    encoded   = encode_permutation(orig_perm)
    deco_perm = decode_permutation(encoded)

    if len(encoded) != 211 or orig_perm != deco_perm:
        fail = True
        break

if fail:
    print(orig_perm)
    print(encoded)
    print(deco_perm)

    for i in range(256):
        if orig_perm[i] != deco_perm[i]:
            print(f"{i:3} {orig_perm[i]:3} {deco_perm[i]:3}")

    print("FAIL")
else:
    print("PASS")
