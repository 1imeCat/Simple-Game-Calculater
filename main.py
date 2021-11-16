import crawler
import calculator

while(1):
	user_input == input(">")
	if user_input == "Exit":
		break
	elif user_input == "recipe":
		print(calculator.recipe())
	elif user_input == "price":
		print(calculator.price())
	elif user_input == "profit":
		print(calculator.profit())
	elif user_input == "update":
		crawler.update()
	else:
		print("command not found")

#parameters should added to calculator function
#crawler.update() function will return dict !!
