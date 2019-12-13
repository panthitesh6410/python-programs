# writing text into a file :
# it deletes previous text
f = open("file.txt", 'w')
f.write("writing a text into a file")
f.close()


# alter way is to append mode:
# here we just add text to previous text

f = open("file.txt", "a")
f.write("\nadding/ appending new line")
f.close()