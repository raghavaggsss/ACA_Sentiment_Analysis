'''lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)'''

fin = open("in.txt" , "r" )
text=fin.read()
a=' '
for i in range(len(text)):
	if text[i].isalnum():
		a=a+text[i].lower()
	else:
		a=a+' '
		
splitted=a.split()
print(splitted)

