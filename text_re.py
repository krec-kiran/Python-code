import re
text = '$aa0AabbX2bZccddEd_!1jJpqlFQx_.///y4YaMbababNhii_'
#
# text = ''.join(re.findall('[A-Z0-9]', text))
#
# text = re.findall('[A-Z0-9]', text)
#
# #
# print(text)

exampleString = '''
Adam is 9 years Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97 years old, and his grandfather, Oscar, is 102.
'''
# exampleString = ''' KLadam 12 15 67
# '''
ages = re.findall(r'\d{2,3}', exampleString)
names = re.findall(r'[A-Z][a-z]*', exampleString)
kames = re.findall(r'[a-z]+', exampleString)
tames = re.findall(r'[a-z]?', exampleString)


print('ages', ages)
print('names', names)
print('kames', kames)
print('Tames', tames)

text = 'KA04MB6700G J14GUD'

val = re.findall('[A-Z]*', text)
print(val)
print(''.join(val))
