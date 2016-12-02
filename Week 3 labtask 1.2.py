def primenum(n):
  if n < 2 or n % 2 == 0:
    return False
  if n == 2:
    return True
  for i in range(2, n):
    if n % i == 0:# if the number is divisble then it’s not a prime number.
      return False
    return True

n = int(raw_input("Enter a number: "))
print primenum(n)
