def powerOfN(n,exp):
  assert type(n)==int and type(exp)==int,"n and exp must be integer"
  assert n>0 and exp>=0,"n and exp must be +ve num"
  if exp==0:
      return 1
  else:
      value=n*powerOfN(n,exp-1)
  return value
print(powerOfN(2,-1))
