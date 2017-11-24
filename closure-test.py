def transmit_to_space(message):
  "This is the enclosing function"
  def data_transmitter(msg):
      "The nested function"
      print(msg + ' ' +message)
  return data_transmitter

fun2 = transmit_to_space("Burn the Sun!")
fun2("Hello Kiran")
fun2("Hello Priya")


def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))
print(multiplywith5(10))

mlt = multiplier_of(3)
print(mlt(2))

