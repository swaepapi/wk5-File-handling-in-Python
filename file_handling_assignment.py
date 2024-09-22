# File Creation 
try:
    with open('my_file.txt', 'w') as file:
        # Writing three lines of text (including numbers and strings)
        file.write("Hello, my name is FIdel .\n")
        file.write("My age is : 24.\n")
        file.write("I love Python.\n")
    print("File created and written successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

# File Reading and Display
try:
    with open('my_file.txt', 'r') as file:
        # Reading and printing the file's content
        content = file.read()
        print("File content:")
        print(content)
except Exception as e:
    print(f"An error occurred: {e}")


# File Appending
try:
    with open('my_file.txt', 'a') as file:
        # Appending three more lines to the file
        file.write("Python is Fun.\n")
        file.write("Here’s another line with a number: 100.\n")
        file.write("Finally, this is the last appended line.\n")
    print("Content appended successfully.")
except Exception as e:
    print(f"An error occurred: {e}")


# Error Handling
# Step 4: Implementing error handling
try:
    # Step 1: Creating and writing to the file
    with open('my_file.txt', 'w') as file:
        file.write("Hello, my name is FIdel.\n")
        file.write("My age is : 24.\n")
        file.write("I love Python.\n")
    
    # Step 2: Reading the content of the file
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("File content after writing:")
        print(content)
    
    # Step 3: Appending more content to the file
    with open('my_file.txt', 'a') as file:
        file.write("Python is Fun.\n")
        file.write("Here is another line with a number: 100.\n")
        file.write("Finally, this is the last appended line.\n")

    # Reading the file again to show appended content
    with open('my_file.txt', 'r') as file:
        updated_content = file.read()
        print("File content after appending:")
        print(updated_content)

except FileNotFoundError:
    print("The file was not found.")
except PermissionError:
    print("You do not have permission to access this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File handling operation completed.")

