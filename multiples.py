def main():
  bs = int(input("Enter the base: "))
  bound = int(input("Enter the upper bound:"))
  result=sum_of_multiples(bs,bound)
  print(f"Sum of multiples of {bs} below {bound} is eqaul to {result}")

def sum_of_multiples(base, below):
  sum = 0
  for i in range(below):
    if i % base == 0:
      sum += i

  return sum 
    
    
    
main()
