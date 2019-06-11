def file_to_dict(filename):
	"""
    function to convert text in a .txt file to dictionary

    :parameter: file: opens the specified filename should be specified in (*.txt) format
    :return: Dictionary: returns the values stored in the file in form of dictionary

    """
	dictionary = {}
	File1 = open(filename, "r")
	print("The items available are : ")
	for i in (File1.read()).split("\n"):
		if len(i) > 2:
			temp_lis = i.split(", ")
			print(temp_lis[2], temp_lis[0], " costing : ", temp_lis[1])
			dictionary[temp_lis[0]] = ([int(temp_lis[1]), int(temp_lis[2])])
	File1.close()
	return dictionary


def dict_to_file(dictionary, filename):
	"""
	the function to overwrite updated data from the dictionary to a file

    :parameter: dictionary:the dictionary file with updated data
    :parameter: filename: the filename to store data

    """
	file3 = open(filename, "w")
	for k, v in dictionary.items():
		v1 = v[0]
		v2 = v[1]
		file3.writelines(k + ", " + str(v1) + ", " + str(v2) + "\n")
	file3.close()
