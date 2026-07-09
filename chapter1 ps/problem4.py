import os

# Specify the directory path
path = "/chrome"

# Get and print the contents of the directory
contents = os.listdir(path)

for item in contents:
    print(item)