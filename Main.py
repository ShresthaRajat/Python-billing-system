import Modules
import Check
import Bill

""" The main module which acts like a launcher and interacts with user by help of 
	imported modules"""

products = Modules.file_to_dict("Inventory.txt")

while Check.yes_customer():
    name = Check.name(input("Enter customer name: "))
    bill_dictionary = {}

    while Check.yes_product():
        item = Check.product(products)
        (price, amount) = (products[item][0], products[item][1])
        print("the product costs : %s and %s pieces available" % (price, amount))
        customer_amount = Check.amount(amount)
        products[item][1] -= customer_amount
        bill_dictionary[item] = [price, customer_amount]

    discount = Check.discount()
    Bill.bill(name, bill_dictionary, discount)

Modules.dict_to_file(products, "inventory.txt")
