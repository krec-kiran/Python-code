import re

# def domain_name():
#   str="http://www.google.com/text/images"
#   # match = re.search(r'http://www\w+',str)
#   match = re.match(r'http://www', str,re.M|re.I)
#   if match:
#     print("found",match.group(1))
#   else:
#     print('did not find')


# domain_name()

import re

# line = "Cats are smarter than dogs"

# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

line = "http://www.google.com/test"

matchObj = re.match(r'http:// (.*)',line, re.M|re.I)

if matchObj:
   print("matchObj.group()  : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
else:
   print("No match!!")
