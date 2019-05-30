from sys import argv

script, filename = argv
text = open(filename)
print(f"Here's your file {filename}")
print(text.read())

print("Type the filename again:")
file_name = input('>')
txt = open(file_name)
print(txt.read())
