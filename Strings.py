Jeff='What you doing over there \t Jeff'
print(Jeff)
print('Why so low \nJoe')
print("Just ignore Jess' bullshit")
print(r'Pretend like \ he is not here')
print('Where did he \\ go')
print()
Newline=(r'''This is alright...
this multiline...
stuff!
Much easier than... 
that \t crap''')
print(Newline)
print(len(Jeff))
print(Jeff[0:14] + ' ' + Jeff[28:])
print()
for i in Jeff.upper()[0:15]:
  print(i)
for i in Jeff.upper()[28:]:
  print(i)
if 'Jeff' in Jeff:
  print('G\'won Jeff!')
if 'Steff' not in Jeff:
  print('Sod off Steff!')
print('jeff'.isalpha())
print('this will be the title'.title())
while True:
  name=input('Is your name, Jeff, Jeff?')
  if name.lower() == 'yes':
    print('Sikkent, Brah!')
    break
  else:
    print('I am disappoint.')
    break
while True:
  password=input('Choose a password?')
  if password.isalnum() and len(password) >= 6:
    print('Enter, my Man!')
    break
  else: 
    print('I am disappoint, try again.')
if Jeff.endswith('Jeff'):
  print('Das it mayne')
if not Jeff.startswith('Howdy'):
  print('Das not it mayne')
List=['My', 'name', 'is', 'Jeff!']
print(' '.join(List))
print(', '.join(List))
print(Jeff.split())
print(Newline.split('\n'))

