import sys

# function for fibonacci numbers
def fib(n):
  if n <= 0:
     return []
  if n == 1:
     return [0]
  result = [0, 1]
  if n == 2:
     return result
  for i in range(2, n):
     result.append(result[i-1] + result[i-2])
  return result

list = (fib(20)) #set to 20 as the example in moodle

# print the sequence with the args from cli
print(list[int(sys.argv[1])-1:int(sys.argv[2])])

