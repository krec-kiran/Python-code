def isPrime(n):
  if n==1:
    return False
  for t in range(2,n):
    if n%t==0:
     return False
  return True

def primes(n=1):
  while n<10:
    if isPrime(n):
      yield n
    n+=1

for i in primes():
  print(i)

