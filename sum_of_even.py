def sum_of_even_numbers(numbers):
    total = 0 
    for i in numbers:
      if i % 2 == 0:
        total += i
    return total

  
  
def main():
  numbers = [1,2,3,4,5,6,7,8,9,10]
  print(sum_of_even_numbers(numbers))

main()

  
