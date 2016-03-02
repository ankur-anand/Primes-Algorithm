import timeit
from timeit import Timer

def isPrime_sqrt_wheel(number):
  '''
  This function uses the fact that apart from the odd we can skip the multiple 
  of 3 too. So we need to try every third number. This leaves us with only 6*k (+-) 1
  number to check. This improves the factor by another 1.5
  '''
  if not number & 1:
    return number == 2
  if not number % 3:
    return number == 3

  limit = int(sqrt(number)) + 1
  step = 2
  for divisor in range(5,limit,step):
    step = 6 - step
    # print (step , divisor)
    # print (number % divisor)
    if not number % divisor:
      # print (divisor)
      return False
  return True


if __name__ == '__main__':
  def isPrime_sqrt_Wheel_time():
    isPrime_naive0000t = timeit.Timer('isPrime_sqrt_wheel(n1000)','from __main__ import isPrime_sqrt_wheel, n1000')
    print ("Time to check 1000th prime", isPrime_sqrt_wheel(n1000),isPrime_naive0000t.repeat(3,10), "sec" )
    isPrime_naive00000t = timeit.Timer('isPrime_sqrt_wheel(n10000)','from __main__ import isPrime_sqrt_wheel, n10000')
    print ("Time to check 1000th prime", isPrime_sqrt_wheel(n10000),isPrime_naive00000t.repeat(3,10), "sec" )
# isPrime_sqrt_Wheel_time()
# Time to check 1000th prime True [4.2592060429410074e-05, 4.1052588365696454e-05, 4.1052588365696454e-05] sec
# Time to check 1000th prime True [0.00013855248573422558, 0.0001416314298616528, 0.0001375261710250831] sec
