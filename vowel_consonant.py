char=input()
if len(char)==1 and char.isalpha():
  if char.lower() in ['a','e','i','o','u']:
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
