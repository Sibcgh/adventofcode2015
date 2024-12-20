def question_one(input_vals):
    floor = 0 
    for para in input_vals:
        if para == "(":
            floor += 1
        elif para == ")":
            floor -= 1

    print("Santa is at floor: {}".format(floor))

def question_two(input_vals):
    floor = 0

    for indx, para in enumerate(input_vals):
        if floor == -1:
            print("Santa made it to the basement on index {}".format(indx))
            break
        if para == "(":
            floor += 1
        elif para == ")":
            floor -= 1


with open("day1.txt") as f:
    line = f.read().split("\n").pop()

question_one(line)
question_two(line)