def reverse_sublist(numbers, start, end):
  new_list = numbers [:]
  new_list_1 = new_list[start,end+1]
  new_list_2 = new_list_1[::-1]
  return new_list_2
  
  


def main():
  my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  start = 2
  end = 6
  print(reverse_sublist(my_list, start, end))
  print(my_list)

main()
