import random
import math

def generateRandomValue(minValue, maxValue):
  return random.uniform(minValue, maxValue)

def generateRandomSolution(minArray, maxArray):
  return [generateRandomValue(minArray[0], maxArray[0]), generateRandomValue(minArray[1], maxArray[1])]

def calculateSolutionValue(solution):
  x = solution[0]
  y = solution[1]
  return math.sin(x + y) + math.pow((x - y), 2) - (1.5 * x) + (2.5 * y) + 1

def printSolution(title, solution):
  print(title)
  print('-----------------------')
  print('x = ', solution[0])
  print('y =', solution[1])
  print('Result =', calculateSolutionValue(solution), '\n')

min = [-1.5, -3]
max = [4, 4]

initialSolution = generateRandomSolution(min, max)
solution = initialSolution
bestSolution = solution
bestSolutionValue = calculateSolutionValue(bestSolution)

printSolution('Initial solution', solution)

failedAttempts = 0
maxFailedAttempts = 100000

while (True):
  solution = generateRandomSolution(min, max)
  solutionValue = calculateSolutionValue(solution)

  if solutionValue < bestSolutionValue:
    bestSolution = solution
    bestSolutionValue = solutionValue
    failedAttempts = 0

  if solutionValue >= bestSolutionValue:
    failedAttempts += 1
    if failedAttempts == maxFailedAttempts:
      break

printSolution('Best solution', bestSolution)
