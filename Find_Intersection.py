def FindIntersection(strArr):
  list1 = strArr[0]
  list1 = list(map(int, list1.split(", ")))
  list2 = strArr[1]
  list2 = list(map(int, list2.split(", ")))

  n = len(list1)
  m = len(list2)

  res = []

  for i in range(0, n):
    for j in range(0, m):
      if(list1[i] == list2[j]):
        res.append(list1[i])

  result = ','.join([str(elem) for elem in res])
  
  return result
  # code goes here
  

# keep this function call here 
print(FindIntersection(input()))