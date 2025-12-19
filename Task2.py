
text = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text + "\n")


print("Data successfully written to output.txt.")

additional_text = input("\nEnter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(additional_text + "\n")


print("Data successfully appended.\n")
print("Final content of output.txt:\n")


with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())