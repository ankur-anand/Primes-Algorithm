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
	// While we're at it, let's think about further improvements.
    // All primes except 2 are odd, and odd numbers cannot have
    // even divisors, so let's skip these in the test.
    // This reduces the running time by another factor of about 2.
	'''

	limit = sqrt(number) + 1
	for x in xrange(3,limit, 2):
		if number % x == 0:
			return False

	return True


# prime = 664579
# naive = Timer("isPrime_naive(prime)","from __main__ import isPrime_naive, prime")
# print ("Naive sqrt odd way of Checking Prime" , naive.repeat(3,1000), "ms")
'''
('Naive sqrt odd way of Checking Prime', [3.694713993216094e-05, 3.386821160448087e-05, 3.2328747440640826e-05], 'ms') for number = 1
('Naive sqrt odd way of Checking Prime', [0.0003232874744064083, 0.0003196953913574482, 0.0003186690819148881], 'ms') for number = 10
('Naive sqrt odd way of Checking Prime', [0.0032328747440640826, 0.0031959276041319223, 0.0032051643891149615], 'ms') for number = 100
('Naive sqrt way of Checking Prime', [0.032270760957136185, 0.03332118867159637, 0.03337199098900309], 'ms') for number = 1000
'''

def nthPrime_naive(number):
	'''
	Find the nth Prime
	'''
	count = 1
	candidate = 3
	while count < number:
		if isPrime_naive(candidate):
			count += 1
		candidate += 2
	
	return candidate - 2


nthPrime = 10
naive_nth = Timer("nthPrime_naive(nthPrime)", "from __main__ import nthPrime_naive, nthPrime")
print ("naive_nth_prime_sqrt_odd - ", nthPrime , " - ", nthPrime_naive(nthPrime) ," ", naive_nth.repeat(3,1),"ms")
'''
('naive_nth_prime_sqrt_odd - ', 10, ' - ', 29, ' ', [1.8473569966080474e-05, 1.7960415244800463e-05, 1.7960415244800456e-05], 'ms')

('naive_nth_prime_sqrt_odd - ', 100, ' - ', 541, ' ', [0.0004767207360691322, 0.00047518127190529215, 0.0004726154982988922], 'ms')

('naive_nth_prime_sqrt_odd - ', 1000, ' - ', 7919, ' ', [0.009950583200340736, 0.010067582476792578, 0.009959819985323772], 'ms')

('naive_nth_prime_sqrt_odd - ', 10000, ' - ', 104729, ' ', [0.21696694770440236, 0.21740312921749036, 0.2132229708579434], 'ms')



'''
