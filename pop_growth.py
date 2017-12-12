def nb_year(p0, percent, aug, p):
  current=p0
  n=0
  while(current<p):
    current=current+current*(percent*0.01)+aug
    n+=1
  print(n)



