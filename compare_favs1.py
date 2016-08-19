def read_file(file_name):
	with open(file_name) as my_file:
		output_list = my_file.readlines()
		return output_list
# turns filename into a list


def compare_favs(list_1, list_2):
	if list_1[0] == list_2[0]:
		print "Our favorite foods are the same!"

	else:
		print "Our favorite foods are different."		

	# output_list = []
	# for item in my_file:
	# 	whitespace = item.strip()
	# 	favorite_foods = output_list.append(whitespace)
	# return favorite_foods

def main():
	Jasmin_list = read_file("jasmin_fav_foods.txt")
	Trushna_list = read_file("trushna_fav_foods.txt")


	# print read_file("jasmin_fav_foods.txt")
	# print read_file("trushna_fav_foods.txt")
	# print compare_favs("jasmin_fav_foods.txt")
	compare_favs(Jasmin_list, Trushna_list)


if __name__ == '__main__':
		main()	