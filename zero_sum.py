def largest_sum(s):
  s=s.split('0')
  s=[x for x in s if x]
  result=[]
  totals=[]
  for x in s:
      result=list(x)
      res=list(map(int,result))
      totals.append(sum(res))
  if totals:
      return(max(totals))
  return 0
