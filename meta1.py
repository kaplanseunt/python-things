/*
Return Mismatched Words
Given an input of two strings consisting of english letters (a-z; A-Z) and spaces, complete a function that returns a list containing all the mismatched words (case sensitive) between them.
You can assume that a word is a group of characters delimited by spaces.
A mismatched word is a word that is only in one string but not the other.
Add mismatched words from the first string before you add mismatched words from the second string in the output array.
*/


import math
# Add any extra import statements you may need here
# Add any helper functions you may need here




def return_mismatched_words(str1, str2):
  
  str1=str1.split()
  
  str2=str2.split()
  
  
  set1=set(str1)
  set2=set(str2)
  
  set3=set1-set2
  set4=set2-set1
  final_lst=list(set3)+list(set4)
  
  print(final_lst)
  return final_lst
    
    
    
    
    
# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printStringList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printStringList(expected)
    print(' Your output: ', end='')
    printStringList(output)
    print()
  test_case_number += 1
    
if __name__ == "__main__":
  # Testcase 1
  str1 = "Firstly this is the first string"
  str2 = "Next is the second string" 
  output_1 = return_mismatched_words(str1, str2)
  expected_1 = ["Firstly", "this", "first", "Next", "second"]
  check(expected_1, output_1)

  # Testcase 2
  str1 = "This is the first string"
  str2 = "This is the second string" 
  output_3 = return_mismatched_words(str1, str2)
  expected_3 = ["first", "second"]
  check(expected_3, output_3)
  
  # Testcase 3
  str1 = "This is the first string extra"
  str2 = "This is the second string" 
  output_4 = return_mismatched_words(str1, str2)
  expected_4 = ["first", "extra", "second"]
  check(expected_4, output_4)
  
  # Testcase 4
  str1 = "This is the first text"
  str2 = "This is the second string" 
  output_5 = return_mismatched_words(str1, str2)
  expected_5 = ["first", "text", "second", "string"]
  check(expected_5, output_5)
  
  
  # Add your own test cases here
