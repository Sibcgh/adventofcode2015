# starting coordinates in a tuple
# have a hashmap storing the directions of each symbol
# iterate through the input text char by char, 
# move the chars based on input symbols from map
# check if new coords are in visited, if not add to visit
# return visited count

# stores in x,y coord form
directions_dict = {
      "^": (0,1),
      "v": (0,-1),
      ">": (1,0),
      "<": (-1,0),
  }


def question_one():
  visited = set()
  with open("day3.txt") as f:
      lines = f.read().split("\n")

  curr_coord = (0,0)
  visited.add(curr_coord)  

  for line in lines:
    for char in line:
      if directions_dict[char]:
        curr_x = curr_coord[0] + directions_dict[char][0]
        curr_y = curr_coord[1] + directions_dict[char][1]
        curr_coord = (curr_x, curr_y)

        if curr_coord not in visited:
          visited.add(curr_coord)


  print(len(visited))

# keep the same visited list but this time split all even indexed characters into 
# 1 string and all odd indexed characters into another string
def question_two():
  # search function for question 2
  def search(line, curr_coord_santa):
    for char in line:
      if directions_dict[char]:
        curr_x = curr_coord_santa[0] + directions_dict[char][0]
        curr_y = curr_coord_santa[1] + directions_dict[char][1]
        curr_coord_santa = (curr_x, curr_y)

        if curr_coord_santa not in visited:
          visited.add(curr_coord_santa)

  visited = set()
  with open("day3.txt") as f:
      lines = f.read().split("\n")

  start__coord = (0,0)
  visited.add(start__coord)  

  for line in lines:
    # split into 2 strings
    santa = line[::2]
    robo_santa = line[1::2]
    search(santa, start__coord)
    search(robo_santa, start__coord)

  print(len(visited))



question_one()
question_two()