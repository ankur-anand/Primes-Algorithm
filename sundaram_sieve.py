import timeit
import cProfile
from math import sqrt

#@profile
def prime_sundaram_sieve(upton):
  '''
  This function gets a further improvement by 
  removing even number from the eratosthenes sieve since they are never prime except
  for 2.
  This yields up the speed by two things first we have to tick only
  few members and seconds only half of the space is required
  '''
  limit = int(sqrt(upton)) + 1
  sieve = [True] * (upton >> 1)
  sievelen = len(sieve)
  for index in range(0,limit):
    if sieve[index]:
      temp = index + index
      index_square = ( temp * (index + 3) ) + 3
      increment = temp + 3
      for inner_index in range(index_square,sievelen,increment): 
        sieve[inner_index] = False
  return sieve

if __name__ == '__main__':
  def prime_sundaram_sieve_time():
    tenk = timeit.Timer('prime_sundaram_sieve(10000)','from __main__ import prime_sundaram_sieve')
    print ("Time to build tenK prime sieve",tenk.repeat(3,1), "sec" )
    thousandk = timeit.Timer('prime_sundaram_sieve(1000000)','from __main__ import prime_sundaram_sieve')
    print ("Time to build 1000k prime sieve",thousandk.repeat(3,1), "sec" )

# prime_sundaram_sieve_time()
# Time to build tenK prime sieve [7.191699842223898e-05, 4.3590000132098794e-05, 4.2716994357760996e-05] sec
# Time to build 1000k prime sieve [0.0050111880045733415, 0.0046959000028437, 0.0027847560049849562] sec
# [Finished in 0.1s]
