def cube_checker(volume, side):
  if side <= 0 or volume <= 0:
    return False
  if side**3 == volume:
    return True
  else:
    return False

