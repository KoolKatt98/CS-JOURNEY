def guess_a_password(password): 
  # defining function with parameter
  i = 10 
  # set variable i with value 10 to give user 10 tries
  while i > 0: 
  # while loop to give user 10 tries
    if password.lower().strip() != "hello": 
      # if statement to check if password is correct while also removing spaces and making it lowercase
      print("Wrong password") 
      # print statement to tell user that password is wrong
      i -= 1 
      # subtract 1 from i to give user another try
      if i > 0: 
        # if statement to check if user has more tries left
        password = input("Try Again: ") # ask user to try again
    else: 
      # else statement to check if password is correct
      return("You are correct !") 
      # print statement to tell user that password is correct
  return("You have exhausted all your attempts, the correct answer is hello") 
  # print statement to tell user that they have exhausted all their attempts and the correct answer is hello


def main(): # defining main function
  password = input("Enter your password: ") # ask user to enter password
  answer = guess_a_password(password) # call function with argument
  print(answer) # print answer

main() # call main function





