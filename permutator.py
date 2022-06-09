list = []
resultList = []
counter = 0

inputNumber = int(input('Digite um Número:' ))

for i in range(inputNumber):
  list.append(i+1)

def permutateList(list, resultList):
    global counter

    if len(list) == 0:
      print(resultList)
      counter+=1
        
    for index in range(len(list)):
      initiation = [list[index]]
      leftSideList = list[:index]
      rightSideList = list[index + 1:]
      fullList = leftSideList + rightSideList
      permutateList(fullList, resultList + initiation)

permutateList(list, resultList)
print('Esse foi o número de permutações retornados:', counter)
