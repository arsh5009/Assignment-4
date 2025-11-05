# Assignment-4
Python Assignment Explaination - 

TASK 1 
	1.	try block → Used to catch any errors that may occur (like missing file).
	2.	open("sample.txt", "r") → Opens the file in read mode (r).
	3.	with statement → Ensures the file is automatically closed after use.
	4.	for line in file: → Reads the file line by line.
	5.	print(line.strip()) → Prints each line without extra blank lines.
	6.	except FileNotFoundError: → Displays an error message if the file doesn’t exist.

TASK 2
  1.	The program first asks the user to enter some data and stores it in a variable.
	2.	It opens a file named output.txt in write mode and writes the user’s input into it.
	3.	Then it asks for additional data to be added to the same file.
	4.	The file is opened again in append mode to add the new text without deleting old content.
	5.	Finally, the program opens the file in read mode and displays its full content line by line.
	6.	The with open() statement ensures files are automatically closed after each operation.

