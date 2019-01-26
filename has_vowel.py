import sys
string=input()
vowel=['a','e','i','o','u']
for i in string:
  if i in vowel:
    print('yes')
    sys.exit(0)
print('no')
