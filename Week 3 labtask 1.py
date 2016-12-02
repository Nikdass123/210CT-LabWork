def revSente(n):
  i = n.split()# this split up the sentence 
  result = []
  for word in i:
    result.insert(0,word)#this will make the sentence reversed from position 0
  return " ".join(result)# join the words for producing required result

test =("This is awesome")
print revSente(test)
