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
	Next Improvement, After Skipping even numbers, we also
	skip multiples of 3, so we need to try only every third 
	number. i.e 5,7 , 11, 13, 17, 19
	which is of form 6*k +- 1
	with alternative increments of 2 and 4
	
	This idea can be taken further 
	
	'''
	if number & 1 == 0:
		return False
	if number % 3 == 0:
		return False
	step = 4 
	limit = sqrt(number) + 1
	i = 5
	while i < limit:
		step = 6 - step
		if number % i == 0:
			return False
		i += step  
	#for x in xrange(3,limit, 2):
	#	if number % x == 0:
	#		return False

	return True


#prime = 664579
#naive = Timer("isPrime_naive(prime)","from __main__ import isPrime_naive, prime")
#print ("Naive sqrt odd_ Wheel way of Checking Prime" , naive.repeat(3,1), "ms")
'''
('Naive sqrt odd way of Checking Prime', [3.694713993216094e-05, 3.386821160448087e-05, 3.2328747440640826e-05], 'ms') for number = 1
('Naive sqrt odd_ Wheel way of Checking Prime', [3.314018249511719e-05, 2.6226043701171875e-05, 2.5987625122070312e-05], 'ms')
('Naive sqrt odd way of Checking Prime', [0.0003232874744064083, 0.0003196953913574482, 0.0003186690819148881], 'ms') for number = 10
('Naive sqrt odd_ Wheel way of Checking Prime', [0.00026297569274902344, 0.0002560615539550781, 0.0002560615539550781], 'ms')

('Naive sqrt odd_ Wheel way of Checking Prime', [0.002607107162475586, 0.002592802047729492, 0.0025560855865478516], 'ms') for number = 100
('Naive sqrt odd_ Wheel way of Checking Prime', [0.026278018951416016, 0.02553391456604004, 0.02548694610595703], 'ms') for number = 1000
'''

def nthPrime_naive(number):
	'''
	Find the nth Prime
	'''
	if number < 2:
		return 2
	if number == 2:
		return 3
	count = 2
	candidate = 5
	step = 4
	while count < number:
		step = 6 - step
		if isPrime_naive(candidate):
			count += 1
		candidate += step
	
	return candidate - 2


nthPrime = 10
naive_nth = Timer("nthPrime_naive(nthPrime)", "from __main__ import nthPrime_naive, nthPrime")
print ("naive_nth_prime_sqrt_odd_2_3_Wheel - ", nthPrime , " - ", nthPrime_naive(nthPrime) ," ", naive_nth.repeat(3,1),"ms")
'''
('naive_nth_prime_sqrt_odd - ', 10, ' - ', 29, ' ', [1.8473569966080474e-05, 1.7960415244800463e-05, 1.7960415244800456e-05], 'ms')
('naive_nth_prime_sqrt_odd_2_3_Wheel - ', 10, ' - ', 29, ' ', [8.106231689453125e-06, 7.152557373046875e-06, 6.9141387939453125e-06], 'ms')
('naive_nth_prime_sqrt_odd - ', 100, ' - ', 541, ' ', [0.0004767207360691322, 0.00047518127190529215, 0.0004726154982988922], 'ms')
('naive_nth_prime_sqrt_odd_2_3_Wheel - ', 100, ' - ', 543, ' ', [0.00020503997802734375, 0.00020313262939453125, 0.00020313262939453125], 'ms')
('naive_nth_prime_sqrt_odd - ', 1000, ' - ', 7919, ' ', [0.009950583200340736, 0.010067582476792578, 0.009959819985323772], 'ms')
('naive_nth_prime_sqrt_odd_2_3_Wheel - ', 1000, ' - ', 7919, ' ', [0.004971981048583984, 0.005506038665771484, 0.005105018615722656], 'ms')
('naive_nth_prime_sqrt_odd - ', 10000, ' - ', 104729, ' ', [0.21696694770440236, 0.21740312921749036, 0.2132229708579434], 'ms')
('naive_nth_prime_sqrt_odd_2_3_Wheel - ', 10000, ' - ', 104729, ' ', [0.12161612510681152, 0.12157487869262695, 0.12128591537475586], 'ms')
'''
