textfile = open('testfile.txt', 'w')


textfile.write("I am a test file.\n")
textfile.write("This is a new line of text. \n")
textfile.close()

t=open("textfile.txt", "a")
t.write("Akmal Razif")
t.close()

f=open('testfile.txt', 'r')
string = f.readlines()
print(string)
