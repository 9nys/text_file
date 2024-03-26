file = open("file_txt", "r")

text = file.read()
words = text.split()
print(" ".join(words))
file.close()
