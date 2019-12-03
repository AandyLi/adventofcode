def calcFuel(modules):
  fuel = 0
  if type(modules) == list:
    for module in modules:
      #print("= " + module)
      currentModuleFuel = (int(module) // 3) - 2
      fuel += currentModuleFuel
      while(currentModuleFuel > 0):
        currentModuleFuel = calcFuel(currentModuleFuel)
        fuel += currentModuleFuel

  elif type(modules) == int:
    fuel += (modules // 3) - 2
  else:
    return 0
  return max(0, fuel)



f = open("modules.txt", "r")

if(f.mode == "r"):
  modules = f.readlines()
  results = calcFuel(modules)
  print("total fuel required " + str(results))

  fuelfuel = calcFuel(results)
  results += fuelfuel
  while(fuelfuel > 0):
    fuelfuel = calcFuel(fuelfuel)
    #print(fuelfuel)
    results += fuelfuel
  print("Total fuel, incl fuel fuel is " + str(results))
