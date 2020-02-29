s = input("Enter a string: ")
char = input("Enter a character: ")


x = True
for c in s:
	if c == char:
		print("found")
		x = False
		break
if x:
	print("not found")		
	