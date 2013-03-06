from arithmetic import *

def tokenize(user_input):
	tokens = user_input.split(" ")
	operator = tokens[0]
	num1 = int(tokens[1])
	num2 = int(tokens[2])

	if operator == "+":
		print add(num1, num2)
	elif operator == "-":
		print subtract(num1, num2)
	elif operator == "*":
		print multiply(num1, num2)
	elif operator == "/":
		print divide(num1, num2)
	elif operator == "square":
		print square(num1)
	elif operator == "cube":
		print cube(num1)
	elif operator == "power":
		print power(num1, num2)
	elif operator == "mod":
		print mod(num1, num2)
	else:
		tokenize(raw_input("Please try again using a standard operand. > ")) 

	play_again()

def play_again():	
	print "Do you want to calculate something else?"
	answer = raw_input("Type yes or no. > ").lower()
	if answer == "yes":
		tokenize(raw_input("Enter in another operand followed by two integers. > "))
	elif answer == "no":
		print "Goodbye!"
	else:
		print "Sorry, I didn't catch that."
		play_again()


print "Hi! Welcome to Em and Rosette's Calculator!",
tokenize(raw_input("To use, first enter operand then two integers. > "))
