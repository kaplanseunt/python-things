import math
import string

def character_frequency(s, c):
  if not c:
    return 0
  
  print()
  print(s)
  word=list(s).copy()
  print(word)
  
  lowercase_letters = list(string.ascii_lowercase)
  uppercase_letters = list(string.ascii_uppercase)
  all_letters = lowercase_letters + uppercase_letters
  print("Küçük harfler:", lowercase_letters)
  print("Büyük harfler:", uppercase_letters)
  print("Tüm harfler:", all_letters)
  frequency = 0
  
  #count ile daha basit yapılsa da burda istenmiyor, döngüye sokuyoruz
  for char in word:
    if char == c:
      frequency += 1
  #letter_count=len(lowercase_letters)
  #for i in range(letter_count):
  #  print(lowercase_letters[i])
  
  print(f"'{c}' karakteri {frequency} kez geçiyor.")
  return frequency
  

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":

  # Testcase 1
  s1 = "Mississippi"
  c1 = "s"
  expected_1 = 4
  output_1 = character_frequency(s1, c1)
  check(expected_1, output_1)

  # Testcase 2
  s2 = "Rainbow"
  c2 = "j"
  expected_2 = 0
  output_2 = character_frequency(s2, c2)
  check(expected_2, output_2)
  
  # Testcase 3
  s3 = "Mirror"
  c3 = "m"
  expected_3 = 0
  output_3 = character_frequency(s3, c3)
  check(expected_3, output_3)
  
  # Testcase 4
  s4 = ""
  c4 = "c"
  expected_4 = 0
  output_4 = character_frequency(s4, c4)
  check(expected_4, output_4)

  # Testcase 5
  s5 = "hello"
  c5 = ""
  expected_5 = 0
  output_5 = character_frequency(s5, c5)
  check(expected_5, output_5)

  # Add your own test cases here
  
