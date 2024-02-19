# Permutation Number Demonstration

Demonstrates converting a permutation over `{0, 1, ..., 255}` to a
permutation number that fits in 211 bytes and back.

This is an unoptimized O(n²) implementation.  I wrote this for
simplicity, not performance.

Because log₂₅₆(256!) ≈ 210.5, and is in fact slightly less, the
upper four bits of the leading byte should actually be 0.  That gives
you a little room to pack other stuff, if you were using this in
some sort of encoder.

Smaller permutations can fit in even fewer bits.  I opted to hard-code
this for `{0, ..., 255}` to keep the code simpler.
