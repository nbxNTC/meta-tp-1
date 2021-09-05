import random
import math

def hill_climbing(objective, minArray, maxArray, tweakProbability, noiseSizes, maxFailedAttempts):
  def generateRandomValue():
    randomValue = 0
    while randomValue == 0 or randomValue == 1:
      randomValue = random.uniform(0, 1)
    return randomValue

  def generateRandomSolution():
    randomSolution = []
    for i in range(len(minArray)):
      randomSolution.append(((maxArray[i] - minArray[i]) * generateRandomValue()) + minArray[i])
    return randomSolution

  def tweakSolution(solution):
    for i in range(len(solution)):
      if random.uniform(0, 1) < tweakProbability:
        operations = [-1, 1]
        multiplier = operations[random.randint(0, 1)]

        noise = abs(solution[i] * noiseSizes[i])
        newValue = solution[i] + (multiplier * noise)

        if newValue >= minArray[i] and newValue <= maxArray[i]:
          solution[i] = newValue

  def printSolution(title, solution):
    print('Variables', title,': ', solution)
    print('Objective value: ', objective(solution))

  solution = generateRandomSolution()
  bestSolution = solution
  bestObjectiveValue = objective(bestSolution)

  printSolution('initial solution', solution)

  failedAttempts = 0

  while (True):
    tweakSolution(solution)
    objectiveValue = objective(solution)

    if objectiveValue < bestObjectiveValue:
      bestSolution = solution
      bestObjectiveValue = objectiveValue
      failedAttempts = 0

    if objectiveValue >= bestObjectiveValue:
      failedAttempts += 1
      if failedAttempts == maxFailedAttempts:
        break

  printSolution('best solution', bestSolution)
  print()

def objectiveTest(solution):
  x = solution[0]
  return math.pow(x, 2)

def objectiveOne(solution):
  x, y = solution
  return math.sin(x + y) + math.pow((x - y), 2) - (1.5 * x) + (2.5 * y) + 1

def objectiveTwo(solution):
  x, y = solution
  return ((-1 * (y + 47)) * math.sin(math.sqrt(abs((x / 2) + y + 47)))) - (x * math.sin(math.sqrt(abs(x - y - 47))))

maxFailedAttempts = 10000000

minArray = [0]
maxArray = [10]
tweakProbability = 1
noiseSizes = [0.3]

hill_climbing(objectiveTest, minArray, maxArray, tweakProbability, noiseSizes, maxFailedAttempts)

minArray = [-1.5, -3]
maxArray = [4, 4]
tweakProbability = 1
noiseSizes = [0.3, 0.3]

hill_climbing(objectiveOne, minArray, maxArray, tweakProbability, noiseSizes, maxFailedAttempts)

minArray = [-512, -512]
maxArray = [512, 512]
tweakProbability = 1
noiseSizes = [0.3, 0.3]

hill_climbing(objectiveOne, minArray, maxArray, tweakProbability, noiseSizes, maxFailedAttempts)

minArray = [-1, -2]
maxArray = [0, -1]
tweakProbability = 1
noiseSizes = [0.3, 0.3]

hill_climbing(objectiveOne, minArray, maxArray, tweakProbability, noiseSizes, maxFailedAttempts)

minArray = [511, 404]
maxArray = [512, 405]
tweakProbability = 1
noiseSizes = [0.3, 0.3]

hill_climbing(objectiveOne, minArray, maxArray, tweakProbability, noiseSizes, maxFailedAttempts)
