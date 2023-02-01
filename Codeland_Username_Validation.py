import re
def CodelandUsernameValidation(string):
  count = 0
  if((len(string) > 4) and (len(string) < 25)):
    count += 1  
  
  l = list(string)
  if(l[0].isalpha()):
    count += 1
  
  if((len(string)-1) != '_'):
    count += 1
  
  res = bool(re.match("^[A-Za-z0-9_-]*$",string))
  if(res == True):
    count += 1
  
  if(count == 4):
    result = True
  else:
    result = False
# code goes here
  return result

# keep this function call here 
print(CodelandUsernameValidation(input()))