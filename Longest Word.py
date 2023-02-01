import re
def LongestWord(sen):
  res = re.sub(r'[^\w\s]','',sen)
  
  l = list(res.split())
  n = len(l)

  for i in range(0, n):
    for j in range(i + 1, n):
      if(len(l[i]) == len(l[j])):
        lw = l[i]
      elif(len(l[i]) < len(l[j])):
        lw = l[j]
      else:
        lw = l[i]
  
  # code goes here
  return lw

# keep this function call here 
print(LongestWord(input()))