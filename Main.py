from typing import List

def selectionSort(array, size) -> List[int]:
  # Write your code he
  for i in range(size):
    temp = i
    for j in range(i + 1, size):
      if array[j] < array[temp]:
        temp = j
    array[temp],array[i] = array[i], array[temp]
    
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
