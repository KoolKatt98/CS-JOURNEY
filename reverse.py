def reverse_sublist(numbers, start, end):
  new_list = numbers[:]
  for i in range(len(new_list)):
    if i >= start and i <= end:
      new_list[end - i + start] = numbers[i]

  
  return new_list


def main():
  my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  start = 2
  end = 6
  print(reverse_sublist(my_list, start, end))
  print(my_list)


main()
