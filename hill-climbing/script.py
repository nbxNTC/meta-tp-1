import random
import math

def hill_climbing(objective, minArray, maxArray, maxFailedAttempts):
  def generateRandomSolution():
    randomSolution = []
    for i in range(len(minArray)):
      randomSolution.append(random.uniform(minArray[i], maxArray[i]))
    return randomSolution

  def printSolution(title, solution):
    x, y = solution
    print(title)
    print('f(', x, ', ', y, ') = ', objective(solution))

  solution = generateRandomSolution()
  bestSolution = solution
  bestObjectiveValue = objective(bestSolution)

  printSolution('Initial solution', solution)

  failedAttempts = 0

  while (True):
    solution = generateRandomSolution()
    objectiveValue = objective(solution)

    if objectiveValue < bestObjectiveValue:
      bestSolution = solution
      bestObjectiveValue = objectiveValue
      failedAttempts = 0

    if objectiveValue >= bestObjectiveValue:
      failedAttempts += 1
      if failedAttempts == maxFailedAttempts:
        break

  printSolution('Best solution', bestSolution)
  print()

def objectiveOne(solution):
  x, y = solution
  return math.sin(x + y) + math.pow((x - y), 2) - (1.5 * x) + (2.5 * y) + 1

def objectiveTwo(solution):
  x, y = solution
  return ((-1 * (y + 47)) * math.sin(math.sqrt(abs((x / 2) + y + 47)))) - (x * math.sin(math.sqrt(abs(x - y - 47))))

maxFailedAttempts = 100000

minArray = [-1.5, -3]
maxArray = [4, 4]

hill_climbing(objectiveOne, minArray, maxArray, maxFailedAttempts)

minArray = [-512, -512]
maxArray = [512, 512]

hill_climbing(objectiveOne, minArray, maxArray, maxFailedAttempts)

minArray = [-1, -2]
maxArray = [0, -1]

hill_climbing(objectiveOne, minArray, maxArray, maxFailedAttempts)

minArray = [511, 404]
maxArray = [512, 405]

hill_climbing(objectiveOne, minArray, maxArray, maxFailedAttempts)
