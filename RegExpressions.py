def isPhoneNumber(text):
  if len(text) != 12:
    print('Not Phone Number')
    return False
  for i in range(0,3):
    if not text[i].isdecimal():
      print('Not Phone Number')
      return False
  if text[3] != '-':
    print('Not Phone Number')
    return False
  for i in range(4,7):
    if not text[1].isdecimal():
      print('Not Phone Number')
      return False
  if text[7] != '-':
    print('Not Phone Number')
    return False
  for i in range(8,12):
    if not text[i].isdecimal():
      print('Not Phone Number')
      return False
  print('Phone Number')
  return True

isPhoneNumber('4154555-1234')

_________________________________________________________________________________

def isPhoneNumber(text):
  if len(text) != 12:
    return False
  for i in range(0,3):
    if not text[i].isdecimal():
      return False
  if text[3] != '-':
    return False
  for i in range(4,7):
    if not text[1].isdecimal():
      return False
  if text[7] != '-':
    return False
  for i in range(8,12):
    if not text[i].isdecimal():
      return False
  return True

isPhoneNumber('4154555-1234')

message='Call me at 123-555-0156 tomorrow. 123-555-0538 is my office.'
for i in range(len(message)):
  chunk=message[i:i+12]
  if isPhoneNumber(chunk):
    print('Phone number found: ' + chunk)
print('Done.')

import re

phoneNumRegex=re.compile(r'\d{3}-\d{3}-\d{4}')

mo=phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
print(mo)

