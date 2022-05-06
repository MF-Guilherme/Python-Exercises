n1 = 'Rolien'
n2 = 'Naej'
n3 = 'Elehcim'
n4 = 'Odranoel'

n = int(input())
for i in range(n) :
  k = int(input())
  for j in range(k) :
      feedback = int(input())
      if feedback == 1 :
          print(n1)
      elif feedback == 2 :
          print(n2)
      elif feedback == 3 :
          print(n3)
      else: 
          print(n4)
      j+=1
i+=1

    