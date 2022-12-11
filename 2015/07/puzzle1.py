TEST = False
TEST_SOLUTION = 0 # add solution for test input here

def ignore_exception(exception=Exception, default_val=None):
  """Returns a decorator that ignores an exception raised by the function it
  decorates.

  Using it as a decorator:

    @ignore_exception(ValueError)
    def my_function():
      pass

  Using it as a function wrapper:

    int_try_parse = ignore_exception(ValueError)(int)
  """
  def decorator(function):
    def wrapper(*args, **kwargs):
      try:
        return function(*args, **kwargs)
      except exception:
        return default_val
    return wrapper
  return decorator

wires = {}
try_parse = ignore_exception(ValueError)(int)

def resolve(wire):
    input = wires[wire]
    if(len(input) == 1):
        value = try_parse(input[0])
        if(value == None):
            value = resolve(input[0])
            wires[input[0]] = [str(value)]
            return value
        return int(value)
    if(len(input) == 2):
        value = try_parse(input[1])
        if(value == None):
            value = ~resolve(input[1])
            wires[input[1]] = [str(value)]
            return value
        return ~int(value)
    if(len(input) == 3):
        left, operand, right = input
        if(try_parse(left) == None):
            left = resolve(left)
            wires[input[0]] = [str(left)]
        else:
            left = int(left)
        if(try_parse(right) == None):
            right = resolve(right)
            wires[input[2]] = [str(right)]
        else:
            right = int(right)
        
        if(operand == 'AND'):
            return left & right
        if(operand == 'OR'):
            return left | right
        if(operand == 'LSHIFT'):
            return left << right
        if(operand == 'RSHIFT'):
            return left >> right

def puzzle(filecontent):
    result = 0
    # insert solution here

    split_lines = [x.split(' -> ') for x in filecontent]
    
    for input, output in split_lines:
        input_parts = input.split(' ')
        wires[output] = input_parts

    print(resolve('a'))

    return result

def solve(input_filename):
    file = open(input_filename, "r")
    content = file.read().splitlines()
    return puzzle(content)

if(TEST):
    testsolution = solve("test.txt")
    if(testsolution == TEST_SOLUTION):
        print("Solution for test input correct")
        regularsolution = solve("input.txt")
        print("Answer for main input", regularsolution)
    else:
        print(f"Solution for test input incorrect! (expected: {TEST_SOLUTION}; is: {testsolution})")
else:
    solve("input.txt")