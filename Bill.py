import datetime as T


def bill(name, product_dictionary, discount_percent):
	"""
	Function to generate unique .txt file to store bill data

	:parameter name: The name of customer
	:parameter product_dictionary:  The dictionary of the items, price and amount
	:parameter discount_percent: Discount percent to be calculated at the total
	:return:
	"""

	file_name = name + "_" + (
		str(T.datetime.now().year)) + "_" + (
		str(T.datetime.now().month)) + "_" + (
		str(T.datetime.now().day)) + "_" + (
		str(T.datetime.now().hour)) + (
		str(T.datetime.now().minute)) + ".txt"

	file = open(file_name, "a")
	file.write(str(T.datetime.now()) + "  \n  \n name : ")
	file.write(name + "  \n \n products: \n \n")
	file.write("Product:\t\tRate:\t\t\tAmount:\t\t\t\tTotal:\n")
	total = 0

	for k, v in product_dictionary.items():
		rate = int(product_dictionary[k][0])
		amount = int(product_dictionary[k][1])
		total_of_product = rate * amount
		file.write(k + "\t\t\t%s\t\t\t%s\t\t\t\t%s\n" % (rate, amount, total_of_product))
		total += total_of_product

	discount_amount = discount_percent * total / 100
	final = total - discount_amount

	file.write("\n\n  Total price = \t \t \t%s\n\n " % total)
	file.write(" Discount percent = \t\t\t%s\n\n " % discount_percent)
	file.write(" Discount amount =\t\t\t%s\n\n " % discount_amount)
	file.write(" Final amount = \t\t\t%s \n\n " % final)
	file.close()
