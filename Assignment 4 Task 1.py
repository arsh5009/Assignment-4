try:
    # Try to open and read the file
    with open("sample.txt", "r") as file:
        for line in file:
            print(line.strip())  # print each line without the newline character
except FileNotFoundError:
    # Handle the case when file doesn't exist
    print("Error: The file 'sample.txt' does not exist.")

