def calcOpcode(inputsArr):
  pos = 0
  index1 = 0
  index2 = 0
  index3 = 0

  inputs = inputsArr[:]
  while(True):
    if(inputs[pos] == 1):
      index1 = inputs[pos + 1] # add 1
      index2 = inputs[pos + 2] # add 2
      index3 = inputs[pos + 3] # add pos
      
      inputs[index3] = inputs[index1] + inputs[index2]

      pos += 4;

    elif inputs[pos] == 2:
      index1 = inputs[pos + 1]
      index2 = inputs[pos + 2]
      index3 = inputs[pos + 3]

      inputs[index3] = inputs[index1] * inputs[index2]

      pos += 4;

    elif inputs[pos] == 99:
      return inputs


def findVerbNoun(original):
  for i in range(99):
    for j in range(99):
      changed = original
      changed[1] = i
      changed[2] = j

      changed = calcOpcode(changed)
      if changed[0] == 19690720:
        return [i, j]


f = open("modules.txt", "r")

if(f.mode == "r"):
  modules = f.read()
  inputs1 = list(map(int, modules.split(',')))
  results = calcOpcode(inputs1)
  print("New opcode " + str(results) + "\n \n")

print(findVerbNoun(inputs1))
