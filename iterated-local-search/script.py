import random
import math

def generateRandomValue():
    randomValue = 0
    while randomValue == 0 or randomValue == 1:
      randomValue = random.uniform(0, 1)
    return randomValue

def generateRandomSolution(minArray, maxArray):
  randomSolution = []
  for i in range(len(minArray)):
    randomSolution.append(((maxArray[i] - minArray[i]) * generateRandomValue()) + minArray[i])
  return randomSolution

def printSolution(title, solution, objective):
  print('Variables', title,': ', solution)
  print('Objective value: ', objective(solution))

def hill_climbing(objective, minArray, maxArray, tweakProbability, noiseSizes, maxFailedAttempts):
  def tweakSolution(solution):
    for i in range(len(solution)):
      if random.uniform(0, 1) < tweakProbability:
        operations = [-1, 1]
        multiplier = operations[random.randint(0, 1)]

        noise = abs(solution[i] * noiseSizes[i])
        newValue = solution[i] + (multiplier * noise)

        if newValue >= minArray[i] and newValue <= maxArray[i]:
          solution[i] = newValue

  solution = generateRandomSolution(minArray, maxArray)
  bestSolution = solution
  bestObjectiveValue = objective(bestSolution)

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

  return bestSolution, objective(bestSolution)

def iterated_local_search(objective, minArray, maxArray, tweakProbability, noiseSizes, maxFailedAttempts, restartsAmount):
  bestSolution, bestSolutionValue = hill_climbing(objective, minArray, maxArray, tweakProbability, noiseSizes, maxFailedAttempts)

  for i in range(restartsAmount):
    newBestSolution, newBestSolutionValue = hill_climbing(objective, minArray, maxArray, tweakProbability, noiseSizes, maxFailedAttempts)
    if newBestSolutionValue < bestSolutionValue:
      bestSolution, bestSolutionValue = newBestSolution, newBestSolutionValue

  printSolution('best solution', bestSolution, objective)
  print()
  return bestSolutionValue

def objectiveTest(solution):
  x = solution[0]
  return math.pow(x, 2)

def objectiveOne(solution):
  x, y = solution
  return math.sin(x + y) + math.pow((x - y), 2) - (1.5 * x) + (2.5 * y) + 1

def objectiveTwo(solution):
  x, y = solution
  return ((-1 * (y + 47)) * math.sin(math.sqrt(abs((x / 2) + y + 47)))) - (x * math.sin(math.sqrt(abs(x - y - 47))))

maxFailedAttempts = 10000

minArray = [0]
maxArray = [10]
tweakProbability = 1
noiseSizes = [0.3]
restartsAmount = 10

iterated_local_search(objectiveTest, minArray, maxArray, tweakProbability, noiseSizes, maxFailedAttempts, restartsAmount)

minArray = [-1.5, -3]
maxArray = [4, 4]
tweakProbability = 1
noiseSizes = [0.3, 0.3]
restartsAmount = 10

results = []
for i in range(30):
  result = iterated_local_search(objectiveOne, minArray, maxArray, tweakProbability, noiseSizes, maxFailedAttempts, restartsAmount)
  results.append(result)
print(results)

minArray = [-1, -2]
maxArray = [0, -1]
tweakProbability = 1
noiseSizes = [0.3, 0.3]
restartsAmount = 10

results = []
for i in range(30):
  result = iterated_local_search(objectiveOne, minArray, maxArray, tweakProbability, noiseSizes, maxFailedAttempts, restartsAmount)
  results.append(result)
print(results)

minArray = [-512, -512]
maxArray = [512, 512]
tweakProbability = 1
noiseSizes = [0.3, 0.3]
restartsAmount = 10

results = []
for i in range(30):
  result = iterated_local_search(objectiveTwo, minArray, maxArray, tweakProbability, noiseSizes, maxFailedAttempts, restartsAmount)
  results.append(result)
print(results)

minArray = [511, 404]
maxArray = [512, 405]
tweakProbability = 1
noiseSizes = [0.3, 0.3]

results = []
for i in range(30):
  result = iterated_local_search(objectiveTwo, minArray, maxArray, tweakProbability, noiseSizes, maxFailedAttempts, restartsAmount)
  results.append(result)
print(results)
