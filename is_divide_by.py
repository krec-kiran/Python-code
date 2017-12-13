number=-12
div1=2
div2=-6

def is_divide_by(number,div1,div2):
  if number%div1==0 and number%div2==0:
    return True
  else:
    return False


print(is_divide_by(-12,2,-6))
