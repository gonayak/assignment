#Write a function that accepts a file name and a string and writes the string to the file with the given file name.

def writetofile():
	file_name= raw_input("enter the filename : ")
	string_to_write= raw_input("enter the string to write to the file :")

	with open(file_name,'w') as f:
		f.write(string_to_write)

writetofile()