try:
    print("Reading file content:\n")
    with open("Sample.txt", "r") as file:
        for index, line in enumerate(file, start=1):
            print(f"Line {index}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'Sample.txt' was not found.")
