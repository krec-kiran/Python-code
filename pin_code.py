def validate_pin(pin):
    if len(pin)!= 4 and len(pin)!=6:
      return False
    elif not pin.isdigit():
      return False

    return True


# print(validate_pin('12345'))
# print(validate_pin('123a'))
# print(validate_pin('1234'))
