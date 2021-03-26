Task 1b

Task b required the creation of a recursive loop to work out the answer to “a^b mod c”. This was attempted using the function:

		if b==1:
			return (a%c)
		elif b==0:
			return 1
		else:
			return (a**b) % c

If b is one, a to the power of b is the same as a-alone and so when b is equal to one, to work out the modular exponentiation you find the mod of a and c. If b is equal to zero, then the answer is one, this is as it is a rule that anything to the power of zero is always one. If these two conditions are not met, the full equation: a to the power of b, modulus c; will be used to find the result.

This can be faster than just using the equation: “a^b mod c”, as if the first condition is met, the function: “a%c” is faster than “a^b mod c” and so saves time. Then it could be argued that if the first condition is not met and the second is, the program going through the first two conditions and returning one as result of the second condition: “b==0”, being met, is faster than using “a^b mod c” to work out either of the first two conditions. The first would be faster to compute than the full equation by a fraction of a second, as it is part of the full equation. If neither of the conditions are met, and the so the full equation is used, it would take longer to compute, however the probability of this outcome is one third so this method is viable.
