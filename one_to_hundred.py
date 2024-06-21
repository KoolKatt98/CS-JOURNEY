def guess_a_password(password):
	x = 10 
	while x > 0 :
		if password.strip().lower() != "hello":
			print("You are incorrect")
			x -= 1
			if x > 0:
				password = input("Try again: ")
		else:
			return("You are correct")
	return ("You have exhausted all attempts. The correct answer was hello") 


def main():
  question = input("I am thinking of a word that starts with H. Guess it: ")
  answer = guess_a_password(question)
  print(answer)

main()
