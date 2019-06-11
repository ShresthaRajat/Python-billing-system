# Ths module contains functions which loops until a valid value is entered


def yes_customer():
	"""function to return Boolen value if y,yes,n and no is given as input """
	print("Add new customer?")
	while True:
		input_yes_no = input("Enter yes to add new customer or no to exit program (y/n):")
		if input_yes_no == "yes" or input_yes_no == "y":
			return True

		elif input_yes_no == "no" or input_yes_no == "n":
			return False

		else:
			print("Oops! Try again")


def yes_product():
	"""function to return True or False: if y,yes,n and no is given as input """
	print("Add new product to customer's bill?")
	while True:
		input_yes_no = input("Enter  yes or no (y/n):")
		if input_yes_no == "yes" or input_yes_no == "y":
			return True

		elif input_yes_no == "no" or input_yes_no == "n":
			return False

		else:
			print("Oops! Try again")


def name(customer_name):
	"""a function which returns valid name only (must contain 3 characters without space) """
	while True:
		if len(customer_name.strip()) > 2:
			return customer_name
		else:
			print("Invalid name. must contain at least 3 character")
			customer_name = input("Customer name : ")


def product(dictionary):
	""" function with exception handelling feature to display, take input and verify the product"""
	available_products = []
	for k, v in dictionary.items():
		if dictionary[k][1] > 0:
			available_products.append(k)
	while True:
		print("The available products are: ", available_products)
		try:
			x = input("Chose from above list :")
			if x in available_products:
				return x
			else:
				print("Oops! Try again")
		except TypeError:
			print("Oops! Try again")


def amount(available_amount):
	"""Function with exception handeling feature to return valid amount of buyable product"""
	while True:
		try:
			x = int(input("Enter desired amount: "))
			if x <= available_amount:
				if x > 0:
					return x
				else:
					print("Oops! invalid amount. Try again")
			else:
				print("Oops! invalid amount. Try again")

		except ValueError:
			print("Oops! invalid amount. Try again")


def discount():
	"""Function with exception handelling feature to return valid discount percent"""
	while True:
		try:
			x = int(input("Enter discount percentage: "))
			if x < 101:
				if x >= 0:
					return x

				else:
					print("Oops! invalid discount value. Try again")
			else:
				print("Oops! invalid discount value. Try again")

		except ValueError:
			print("Oops! invalid discount value. Try again")
