file = open("python.pdf", "r")
print(file.read())
file.close()

modified_file = open("python.pdf", "a")
modified_file.write("\nThis is the modified file")

modified_file.close()

try :
    input_file = input("Enter the file name: ")
    file = open(input_file, "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
except Exception as e:
    print(f"An error occurred: {e}")

    