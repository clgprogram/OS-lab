# Open a file in write mode
file = open("myfile.txt", "w")

# List of strings to write to the file
L = ["This is Denish's\n", "This is perisin\n", "This is London\n"]

# Write the strings to the file
file.write('Hello\n')  # Write a simple string
file.writelines(L)  # Write multiple lines from the list

# Close the file after writing
file.close()

# Open the file again in read mode
file1 = open("myfile.txt", "r")

# Read the entire content of the file
print("Output of read() function:")
print(file1.read())
# Go back to the beginning of the file
file1.seek(0)

# Read one line using readline() function
print("\nOutput of readline() function is:")
print(file1.readline())

# Go back to the beginning of the file again
file1.seek(0)

# Read all lines using readlines() function
print("\nOutput of readlines() function is:")
print(file1.readlines())

# Close the file after reading
file1.close()
