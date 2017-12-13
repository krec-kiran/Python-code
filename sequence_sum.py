# sequence_sum(2, 6, 2) # 12 (= 2 + 4 + 6)

def sequence_sum(begin,end,step):
  val=begin
  toto=0
  print("Val",val)
  print("toto",toto)
  print("end",end)

  if begin>=0:
    while(val<=end):
      # print("Val",val)
      # print("Toto",toto)
      toto+=val
      val+=step
    print(toto)
  else:
    while(val>=end):
      print("Val",val)
      print("Toto",toto)
      toto+=val
      val+=step
    print(toto)


sequence_sum(-24, -2, 22)
# Test.assert_equals(sequence_sum(-2, 4, 658), -2)


# -24+22=-2

# -24-2=-26
