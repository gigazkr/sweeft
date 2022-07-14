try:
  n = int(input("Enter the number of words (from 1 to 10^5): "))
  if not 1 <= n <= 10**5:
    raise ValueError("Incorrect number")

  word_list = []
  for word in range(n):
    word = input("Enter the word (Lowercase English letters): ")
    if word.islower() and word.isalpha():          
      word_list.append(word)
    else:
      raise ValueError("Incorrect letters")
  
  if len(''.join(word_list)) > 10**6:   
    raise ValueError("The sum of the lengths of the words is greater than 10^6")

except ValueError as e:
  print(e)
except Exception as e:
  print(e)

  
dictx = {}

for i in word_list:
  if i in dictx:
    dictx[i] += 1
  else:
    dictx[i] = 1

print(len(dictx))
for i in dictx.values():
  print(i, end=' ')


