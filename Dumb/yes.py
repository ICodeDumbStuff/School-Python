import decimal
def compute_pi(n):
  """
  This function calculates the value of pi to 'n' number of decimal places
  Args:
  n:   precision(Decimal places)
  Returns:
  pi:   the value of pi to n-decimal places
  """

  decimal.getcontext().prec = n + 3
  decimal.getcontext().Emax = 999999999

  C = 426880 * decimal.Decimal(10005).sqrt()
  K = decimal.Decimal(6)
  M = decimal.Decimal(1)
  X = decimal.Decimal(1)
  L = decimal.Decimal(13591409)
  S = L

  # For better precision, we calculate to n+3 and truncate the last two digits
  for i in range(1, n+3):
    M = decimal.Decimal(M* ((1728*i*i*i)-(2592*i*i)+(1104*i)-120)/(i*i*i))
    L = decimal.Decimal(545140134+L)
    X = decimal.Decimal(-262537412640768000*X)
    S += decimal.Decimal((M*L) / X)

  return str(C/S)[:-2] # Pi is C/S
print(compute_pi(10000))