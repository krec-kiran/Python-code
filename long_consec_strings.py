# a=["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"]
# starr=["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"]
k=2
# starr=["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"]
# starr=["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"]
# starr=["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"]
# starr=["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"]
starr=['ppddpppyyyaarr', 'qqqkkccwpsddbbzzzzz', 'pppdddazzz', 'llluujsmmmm', 'vijjqqqww', 'ccaaadduuummmnwwww', 'jjjppttaaaff', 'zzzwwffyyy', 'ooozztxx', 'wwjjrrgggqffdd', 'zzzqqggsss', 'sssfdddh', 'pppxxfffpppnnnu', 'gggpkk', 'qoreoojjjjb', 'hhrrhhhhpp', 'yyyppggglll', 'ffohhzssrjjj', 'mmmeiiirrw', 'eeepeeekkkqqqw', 'oofrxxxxpppyy', 'xwwzzk', 'tttoobbjdddttt', 'llxxxggg', 'qqnnnngttty', 'jiisood', 'xlllnnaaa', 'llpppddsssiii', 'iivvvxscccu', 'oooxxxsssyyyll', 'rrrqbbbtthhff', 'bbllyy', 'cyhhbbfff', 'qqtttchhkkzzzsx', 'gggooeeee', 'ttbbrr', 'grrrdd', 'eqvvvuuoooff', 'llgggzzz', 'tttvvbb', 'yyyiiiiiuvvv', 'ccaaavvssd', 'ddcckkkmmvvbbb', 'jwwaii', 'gggirrr', 'zzbsaaahh', 'eeovvvaaaddpp', 'iiyooxxxxxx', 'dddbbbk', 'uqpp', 'dddnjjjbbb', 'fffkkkggnb', 'aawxx', 'yqquuzzzp', 'oowwwxxxoozzzk', 'mmazan', 'mmmkkkooonnkkkoo', 'llccczzzzz', 'aajjkmccrrr', 'kkkgggeeeeeew', 'bbboreeeddd', 'ssfffbbi', 'ppre', 'rrivvv', 'xxxraaauuczznbb', 'oossxxxeeaakk', 'kkknnnh', 'xuuuccnnn', 'eeyyfffiigjjj', 'gppoooww', 'rbbbdffqfffffrrr', 'ccccxxxqqqii', 'uuuxkkkhhh', 'vpppssssrrr', 'rrrhfffhhckw', 'wwwaxxb', 'mmsssnnkkbbwww', 'bzdd', 'xxmmssii', 'xxxaaaaaa', 'csssurrriiiggg', 'tttffficccqqqfff', 'vui', 'iimmmzxxxxx', 'gggutggcc', 'hrggsssgg', 'mmyyfs', 'dppssgxxx', 'rrriigkkk', 'aiiwwgggrrr', 'ihzetttuuuaa', 'bsnnnnnnzzzn', 'uuunnnkkkmmbbc', 'tttxzmmmzznnn', 'qlllrrrllliggg', 'rrrrruzyytt', 'lllbfffppp', 'dddttmmmaawwzztt', 'ccxjcccooovv', 'ssszhh', 'eeepppiinnqq', 'plllyyy', 'gggjjmmmgggww', 'wwwblll', 'qqnnnv', 'cqqqqqqqqrrr', 'aeeejjjt', 'kkevl', 'jjyqqbbkkk', 'cfx', 'vrrrbbgzlll', 'qqqmdooouuvvvv', 'btttdffi', 'cccxxdddtlawn', 'iiikkyhhh', 'mmmooosss', 'tkeexss', 'tttssnnuggywr', 'vvnnbbtttf', 'zzjjjayyy']

def longest_consec(strarr, k):
  if k<=0 or k>len(strarr):
      return ''
  if strarr:
        long_index=strarr.index(max(strarr,key=len))
        print("Longest:",strarr[long_index])
  else:
        return ''
  long_consec_string = strarr[long_index]
  count=1
  print("Length:",len(strarr))
  print("Long index:",long_index)
  if long_index < len(strarr)-1:
    if len(strarr[long_index+1])>len(strarr[long_index-1]):
      while count < k and long_index+count <len(strarr):
        long_consec_string+=strarr[long_index+count]
        count+=1
    else:
      while k>0 and long_index>0:
        long_consec_string=strarr[long_index-1]+long_consec_string
        long_index-=1
        k-=1
  else:
      while count < k:
        long_consec_string=strarr[long_index-count]+long_consec_string
        count+=1
  return long_consec_string



print(longest_consec(starr,k))
