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
