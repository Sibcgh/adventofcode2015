from collections import defaultdict
# check if contains bad string
def check_bad_string(input_text):
  for word in ["ab", "cd", "pq", "xy"] :
    if word in input_text:
      return False
  
  return True


# create function to check subarray of repeating 
def subarray_check(input_text):
  # once u find the first repeating char of len 2 return true
  for i in range(len(input_text)-1):
    if input_text[i] == input_text[i+1]:
      return True
  return False


# check if there are 3 vowels
def vowel_check(input_text):
  count = 0
  for char in input_text:
    if char in "aeiou":
      count +=1

  return True if count >= 3 else False


# just need find all instances of repeating chars of len 2
def check_repeating_chars(input_text):
  for i in range(len(input_text) - 2):
    # checks for repeating by checking curr start is in curr end 
    if input_text[i: i + 2] in input_text[i + 2:]:
      return True
  return False


# find palindrome of len 3
def check_palindrome_three(input_text):
  for i in range(len(input_text)-2):
    # simple palindrome check by checking indices 2 chars apart
    if input_text[i] == input_text[i+2]:
      return True

  return False


def question_one():
  with open("day_5.txt") as f:
      lines = f.read().split("\n")

  nice_word_count = 0

  for line in lines:
    line = line.strip()
    check1 = subarray_check(line)
    check2 = check_bad_string(line)
    check3 = vowel_check(line)

    if check1 and check2 and check3:
      nice_word_count += 1


  print((nice_word_count))


def question_two():
  with open("day_5.txt") as f:
      lines = f.read().split("\n")

  nice_word_count = 0

  for line in lines:
    line = line.strip()
    check1 = check_repeating_chars(line)
    check2 = check_palindrome_three(line)

    if check1 and check2:
      nice_word_count += 1

  print((nice_word_count))


question_one()
question_two()