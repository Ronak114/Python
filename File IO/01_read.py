# reading a file
# rb-read binary ,  rt/r -read text

f = open("ronak.txt", "r")
content = f.read()
print(content)
f.close()
