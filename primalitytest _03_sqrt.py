import unittest
import timeit
from timeit import Timer

def sqrt(number):
	'''
	Function to calculate the square root
	'''
	x = number
	y = (x + (number // x)) // 2

	while y < x:
		x = y
		y = (x + (number // x)) // 2

	return x

def isPrime_naive(number):
	'''
	// Stopping at n/2 is still way too slow to find the n-th
    // prime for larger n.
    // So we start to think. If n/2 is a divisor of n, then
    // n = 2*(n/2), so 2 is a divisor too, and the testing
    // loop never reaches n/2, hence we can stop even earlier.
    // Now, the next largest possible divisor of n is n/3.
    // But if n/3 is a divisor of n, so is 3, and the loop
    // won't go further than 3. The next largest -
    //
    // Hey, wait a minute. 2 <-> n/2, 3 <-> n/3 ...
    // The divisors of n come in pairs, d and n/d.
    // Unless d = sqrt(n), one of these two, say d, is smaller
    // than the other and hence d*d < d*(n/d) = n, so d < sqrt(n).
    //
    // If n is composite, at least one of its nontrivial divisors is
    // not larger than sqrt(n).
    // That means we can stop our loop at sqrt(n). First BIG step.
    //
    // This improvement reduces the complexity of the algorithm.
    // Testing primality of n has dropped from O(n) to O(sqrt(n)),
    // so the overall complexity of finding the n-th prime has
    // dropped from O(n^2 * log n) to O(n^1.5 * sqrt(log n)) -
    // or so, I haven't done it properly and may have gotten
    // the exponent of the log factor wrong.
	'''

	limit = sqrt(number) + 1
	for x in xrange(2,limit):
		if number % x == 0:
			return False

	return True


# prime = 664579
# naive = Timer("isPrime_naive(prime)","from __main__ import isPrime_naive, prime")
# print ("Naive sqrt way of Checking Prime" , naive.repeat(3,1), "ms")
'''
('Naive sqrt way of Checking Prime', [6.517064960256167e-05, 6.157856655360157e-05, 6.157856655360157e-05], 'ms') for number = 1
('Naive sqrt way of Checking Prime', [0.0006137330466508957, 0.0006019304880614554, 0.0006014173333401755], 'ms') for number = 10
('Naive sqrt way of Checking Prime', [0.0060557388658254345, 0.006069594043299995, 0.006050607318612636], 'ms') for number = 100
('Naive sqrt way of Checking Prime', [0.12713664797072965, 0.12604875996161605, 0.1323841681505391], 'ms') for number = 1000
'''

def nthPrime_naive(number):
	'''
	Find the nth Prime
	'''
	count = 0
	candidate = 2
	while count < number:
		if isPrime_naive(candidate):
			count += 1
		candidate += 1
	
	return candidate - 1


nthPrime = 10
naive_nth = Timer("nthPrime_naive(nthPrime)", "from __main__ import nthPrime_naive, nthPrime")
print ("naive_nth_prime_sqrt - ", nthPrime , " - ", nthPrime_naive(nthPrime) ," ", naive_nth.repeat(3,1),"ms")
'''
('naive_nth_prime_sqrt - ', 10, ' - ', 29, ' ', [3.694713993216094e-05, 3.694713993216095e-05, 3.6433985210880944e-05], 'ms')

('naive_nth_prime_sqrt - ', 100, ' - ', 541, ' ', [0.0009580598646297846, 0.0009534414721382644, 0.000966783494891545], 'ms')

('naive_nth_prime_sqrt - ', 1000, ' - ', 7919, ' ',  [0.020482570699891726, 0.020224967029809155, 0.020982383398418458], 'ms')

('naive_nth_prime_sqrt - ', 10000, ' - ', 104729, ' ', [0.4140409394836638, 0.41208735945975067, 0.4136878890354231], 'ms')



'''
