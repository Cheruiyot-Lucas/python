# File Read & Write Challenge 
try:
    # Open the original file in read mode
    with open("input.txt", "r") as infile:
        content = infile.read()

    # Modify the content (example: make all text uppercase)
    modified_content = content.upper()

    # Write the modified content into a new file
    with open("output.txt", "w") as outfile:
        outfile.write(modified_content)

    print(" File has been read and modified successfully. Check 'output.txt'!")

except FileNotFoundError:
    print(" Error: 'input.txt' does not exist.")


# Error Handling Lab 
filename = input("\nEnter the filename to read: ")

try:
    with open(filename, "r") as file:
        print("\n File content:\n")
        print(file.read())

except FileNotFoundError:
    print(f" Error: The file '{filename}' was not found.")
except PermissionError:
    print(f" Error: You don’t have permission to read '{filename}'.")
except Exception as e:
    print(f" An unexpected error occurred: {e}")
