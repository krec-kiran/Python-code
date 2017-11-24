def dollar(fn):
  def new(*args):
    return '$' + str(fn(*args))
  return new

@dollar
def price(amount,tax_rate):
  return amount + amount*tax_rate


print(price(100,0.2))

