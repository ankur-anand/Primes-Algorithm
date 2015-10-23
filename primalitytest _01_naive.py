import unittest
import timeit
from timeit import Timer

def isPrime_naive(number):
	'''
	This is the naive method of 
	'''
	for x in xrange(2,number):
		if number % x == 0:
			return False

	return True


# prime = 664579
# naive = Timer("isPrime_naive(prime)","from __main__ import isPrime_naive, prime")
# print ("Naive way of Checking Prime" , naive.timeit(number=1), "ms")
'''
('Naive way of Checking Prime', 0.04427601566148209, 'ms') for number = 1
('Naive way of Checking Prime', 0.8443298969072165, 'ms') for number = 10
('Naive way of Checking Prime', 14.868997244359146, 'ms') for number = 100
('Naive way of Checking Prime', 48.910480672027425, 'ms') for number = 1000
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


nthPrime = 10000
naive_nth = Timer("nthPrime_naive(nthPrime)", "from __main__ import nthPrime_naive, nthPrime")
print ("naive_nth_prime - ", nthPrime , " - ", nthPrime_naive(nthPrime) ," ", naive_nth.repeat(3,1),"ms")
'''
('naive_nth_prime - ', 10, ' - ', 29, ' ', [2.3605117178880604e-05, 2.2065653015040567e-05, 2.2065653015040567e-05], 'ms')

('naive_nth_prime - ', 100, ' - ', 541, ' ', [0.001912527646210609, 0.0018673700307379677, 0.001869935804344368], 'ms')

('naive_nth_prime - ', 1000, ' - ', 7919, ' ', [0.24615056985831799, 0.24393630723599474, 0.24505395821894255], 'ms')

('naive_nth_prime - ', 10000, ' - ', 104729, ' ', [32.6315851862495, 33.538759089253, 34.14927465580148], 'ms')



'''

# class naivePrimetest(unittest.TestCase):
# 	'''
# 	Testing all the prime methods defined
# 	'''
# 	def test_nthPrime_naive(self):

# 		self.assertEqual(nthPrime_naive(25), 97)

# 	def test_isPrime_naive(self):

# 		self.assertEqual(isPrime_naive(664579), True)

# if __name__ == '__main__':
# 	unittest.main()



