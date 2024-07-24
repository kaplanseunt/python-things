import math
# Add any extra import statements you may need here
#A balanced array would be an array in which each element appears the same number of times.
#Given an array with n elements, return a dictionary with the key as the element and the value as the count of elements needed to balance the given array.

# Add any helper functions you may need here


def return_missing_balanced_numbers(input):
    print()
    lst = input.copy()
    lst.sort()
    print("Sıralanmış Liste:", lst)
    
    lst_dstnct = list(set(lst))
    print("Benzersiz Elemanlar:", lst_dstnct)
    
    leng = len(lst_dstnct)
    max_count = 0
    most_frequent = None
    
    element_counts = {}
    for i in range(leng):
        count = lst.count(lst_dstnct[i])
        element_counts[lst_dstnct[i]] = count
        print(f"{lst_dstnct[i]} elemani {count} kez geciyor.")
        
        if count > max_count:
            max_count = count
            most_frequent = lst_dstnct[i]
    
    print("En fazla gecen eleman:", most_frequent, "sayisi:", max_count)
    
    missing_counts = {element: max_count - count for element, 
                      count in element_counts.items() 
                      if element != most_frequent and max_count - count > 0}
    print("Mevcut durum:", element_counts)
    print("Eksik Sayılar:", missing_counts)
    return missing_counts


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
    print(expected)
    print(' Your output: ', end='')
    print(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  
  # Testcase 1 
  input_1 = ['a','b','abc','c','a']
  output_1 = return_missing_balanced_numbers(input_1)
  expected_1 = {'b':1,'abc':1,'c':1}
  check(expected_1, output_1)

  # Testcase 2 
  input_2 = [1,3,4,2,1,4,1]
  output_2 = return_missing_balanced_numbers(input_2)
  expected_2 = {2:2,3:2,4:1}
  check(expected_2, output_2) 
  
  # Testcase 3
  input_3 = [4,5,11,5,6,11]
  output_3 = return_missing_balanced_numbers(input_3)
  expected_3 = {4:1,6:1}
  check(expected_3, output_3)
  
  # Add your own test cases here
  
