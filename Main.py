from typing import List

def selectionSort(array, size) -> List[int]:
  # Write your code he
  for i in range(size):
    j = i+1
    for j in range(size):
      if array[i]<= array[j]:
          i +=1
      else:
          a = array[j]
          array[j]=array[i]
          array[i] = a
  return array
  

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
