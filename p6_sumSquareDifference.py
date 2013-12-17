
def sum_squares (n):
  return sum([x*x  for x in xrange(1,n+1)])

def square_sum(n):
  return sum([x for x in xrange(1,n+1)])**2


print square_sum(100)-sum_squares(100)
