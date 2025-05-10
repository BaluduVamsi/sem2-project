word=input("enter a word: ")
newword=""
for i in range(len(word)):
  if i%2==0:
    newword+=word[i].lower()
  else :
    newword+= word[i].upper()
print(newword)