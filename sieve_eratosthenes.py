from math import sqrt
import timeit
import time

n10000 = 104729
nnrime = 664579
n1000 = 7919


def primeSieve_01(upton):
  '''
  Returns a list of prime numbers calculated using the Sieve of Eratosthenes algrotithm
  '''
  sieve = [True] * upton
  sieve[0] = False #Zero and one are not prime number
  sieve[1] = False
  # checking the divisibilty till Square root of it
  limit = int(sqrt(upton)) + 1
  for index in range(2,limit):
    if sieve[index]:
      pointer = index * index
      for inner_index in range(pointer,upton,index):#for inner loop increase the step size by outer index 
        # print (sieve[inner_index], inner_index)
        sieve[inner_index] = False
        # print (sieve[inner_index])

  return sieve


def isPrime_01(number):
  upton = number + 1
  # start = time.clock()
  checked = primeSieve_01(upton)
  # print (time.clock() - start)
  if checked[number]:
    return True
  return False



if __name__ == '__main__':
  def isPrime_naive_time():
    isPrime_naive0000t = timeit.Timer('isPrime_01(n10000)','from __main__ import isPrime_01, n10000')
    print ("Time to check 1000th prime", isPrime_01(n10000),isPrime_naive0000t.repeat(3,10), "sec" )
    isPrime_naive00000t = timeit.Timer('isPrime_01(nnrime)','from __main__ import isPrime_01, nnrime')
    print ("Time to check 10000th prime", isPrime_01(nnrime),isPrime_naive00000t.repeat(3,10), "sec" )

# isPrime_naive_time()
# Time to check 1000th prime True [0.15272743133954594, 0.15201311630198286, 0.14999640789851804] sec
# Time to check 10000th prime True [1.0718004638942484, 1.0670989162116673, 1.060605423046923] sec
# [Finished in 4.0s]
