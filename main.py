from art import logo


#создаем отдельные функции с операциями над числами:
#add
def add(num_1, num_2):
	return num_1 + num_2


#subtract
def subtract(num_1, num_2):
	return num_1 - num_2


#multiply
def multiply(num_1, num_2):
	return num_1 * num_2


#divide
def divide(num_1, num_2):
	return num_1 / num_2


# создаем словарь
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
	print(logo)
	number_1 = float(input("Please enter first number: "))
	for symbol in operations:
		print(symbol)
	continue_game = True
	while continue_game:
		operational_symbol = input("Pick an operation: ")
		number_2 = float(input("Please enter next number: "))
		calc_action = operations[operational_symbol]
		answer = calc_action(number_1, number_2)
		# print(answer)
		print(f"{number_1} {operational_symbol} {number_2} = {answer}")
		continue_calc = input(
		    f"Type 'y' to continue calculating with {answer} or type 'n' to exit: "
		)
		if continue_calc == "y":
			number_1 = answer
		else:
			continue_game = False
			calculator()


calculator()
#рекурсия вызывает сама себя
