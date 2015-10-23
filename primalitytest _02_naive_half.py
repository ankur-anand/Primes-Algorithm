import timeit
from timeit import Timer

def isPrime_naive(number):
	'''
	// none of the numbers between n/2 and n can be a divisor of n,
    // so we can stop testing at n/2, reducing the running time by
    // roughly half.
	'''
	half = number // 2 + 1
	for x in xrange(2,half):
		if number % x == 0:
			return False

	return True


# prime = 664579
# naive = Timer("isPrime_naive(prime)","from __main__ import isPrime_naive, prime")
# print ("Naive half way of Checking Prime" , naive.repeat(3,1000), "ms")
'''
('Naive half way of Checking Prime', [0.021305670872824863, 0.024006404170921578, 0.021194316298307106], 'ms') for number = 1
('Naive half way of Checking Prime', [0.21287915719468578, 0.21271751345748255, 0.21376948063610662], 'ms') for number = 10
('Naive half way of Checking Prime', [2.1679914611054376, 2.130246878736408, 2.14648412042715], 'ms') for number = 100
('Naive half way of Checking Prime', [21.444053819667168, 21.418079980294863, 21.515459299133283], 'ms') for number = 1000
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
print ("naive_nth_prime_half - ", nthPrime , " - ", nthPrime_naive(nthPrime) ," ", naive_nth.repeat(3,1),"ms")

'''

('naive_nth_prime_half - ', 1, ' - ', 2, ' ', [2.5657736064000658e-06, 1.539464163840039e-06, 1.026309442560026e-06], 'ms')
('naive_nth_prime_half - ', 10, ' - ', 29, ' ', [2.1039343572480537e-05, 2.0526188851200523e-05, 2.0526188851200526e-05], 'ms')
('naive_nth_prime_half - ', 1000, ' - ', 7919, ' ', [0.1251456076521632, 0.12461346620619584, 0.1271268980310253], 'ms')
('naive_nth_prime_half - ', 10000, ' - ', 104729, ' ', [16.885736864522023, 16.917259959050252, 17.04759766617233], 'ms')
'''
