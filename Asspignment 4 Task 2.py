# Step 1: Take user input
user_input = input("Enter text to write to the file: ")

# Step 2: Write input to file (create or overwrite)
with open("output.txt", "w") as file:
    file.write(user_input + "\n")
    print("Data successfull written to output.txt")
# Step 3: Take additional input to append
additional_input = input("Enter additional text to append: ")

# Step 4: Append new data to the same file
with open("output.txt", "a") as file:
    file.write(additional_input + "\n")
    print("Data successfull appended.")

# Step 5: Read and display final content
print("\n--- Final content of 'output.txt' ---")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())