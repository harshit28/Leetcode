# store powers of 2 less than 100_000
pow2 = set()
p2 = 1
while p2 < 100_000:
    p2 <<= 1
    pow2.add(p2)

# hashtable to store solutions for ns from 1 to 100,000
table = {}
# starting value for concatenated numbers
total = 0
# current length of n in bits
b = 1
for n in range(1, 100_001):
	#  if n is a power of 2 it is 1 bit longer than n-1
    if n in pow2:
        b += 1
	# make space for n
    total <<= b
	# replace first b bits with bits in n (could use XOR or addition too)
    total |= n
    total %= (10**9 + 7)
    table[n] = total

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return table[n]
