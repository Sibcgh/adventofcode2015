from string import digits

def question_one():
  with open("day2.txt") as f:
    lines = f.read().split("\n")

  res = 0

  for line in lines:
    numbers = []

    test = line.split("x")
    for char in test:
      if char.isdigit():
        numbers.append(int(char))

    l = numbers[0]
    w = numbers[1]
    h = numbers[2]
    res += (2*l*w + 2*w*h + 2*h*l) + min(l*w, w*h, h*l)

  print(res)

def question_two():
  with open("day2.txt") as f:
    lines = f.read().split("\n")

  res = 0

  for line in lines:
    numbers = []

    test = line.split("x")
    for char in test:
      if char.isdigit():
        numbers.append(int(char))

    l = numbers[0]
    w = numbers[1]
    h = numbers[2]

    vol = l*w*h
    numbers.sort()
    numbers.pop()

    res += l*w*h + 2*(numbers[0]+numbers[1])

  print(res)
  
question_one()
question_two()