def fillGrid(lines):
  x = 0
  y = 0
  step = 0
  coordinates = []
  for line in lines:
    if(line[0] == "R"):
      dist = int(line[1:])
      for __ in range(dist):
        x += 1
        step += 1
        coordinates.append((x, y, step))
    elif(line[0] == "L"):
      dist = int(line[1:])
      for __ in range(dist):
        x -= 1
        step += 1
        coordinates.append((x, y, step))
    elif(line[0] == "U"):
      dist = int(line[1:])
      for __ in range(dist):
        y += 1
        step += 1
        coordinates.append((x, y, step))
    elif(line[0] == "D"):
      dist = int(line[1:])
      for __ in range(dist):
        y -= 1
        step += 1
        coordinates.append((x, y, step))

  return coordinates

def findCoordsCross(coords1, coords2):
  return list(set(coords1) & set(coords2))

def findClosest(coords):
  shortest = 10000
  for i in range(len(coords)):
    x = coords[i][0]
    y = coords[i][1]

    dist = abs((0 - x)) + abs((0 - y))
    if( dist < shortest):
      shortest = dist

  return shortest

def findStepCount(crossing, coordsList, coordsList_with_stepValue):
  stepsIndex = [coordsList.index(x) for x in crossing]
  valueAtIndex = []
  for x in stepsIndex:
    valueAtIndex.append(coordsList_with_stepValue[x][2])
  return valueAtIndex

def findFastest(line1StepCount, line2StepCount):
  stepCount = 1000000000
  for a, b in zip(line1StepCount, line2StepCount):
    if a + b < stepCount:
      stepCount = a + b
  return stepCount


f = open("modules.txt", "r")

if(f.mode == "r"):
  modules = f.readlines()
  
  firstLine = list(map(str, modules[0].split(',')))
  #remove \n from last element
  firstLine[-1] = firstLine[-1].strip("\n")

  secondLine = list(map(str, modules[1].split(',')))

  coords1 = fillGrid(firstLine)
  coords2 = fillGrid(secondLine)

  line1Coords = [(x, y) for x, y, _ in coords1]
  line2Coords = [(x, y) for x, y, _ in coords2]

  crossing = findCoordsCross(line1Coords, line2Coords)

  line1StepCount = findStepCount(crossing, line1Coords, coords1)
  line2StepCount = findStepCount(crossing, line2Coords, coords2)

  print("Shortest distance: ", findClosest(crossing), "Shortest step count: ", findFastest(line1StepCount, line2StepCount))
