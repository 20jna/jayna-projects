#n = int(input("Give a number: "))
#n = n+96
#print(chr(n))

#c = input("Give lowercase letter: ")
#i = ord(c) - 96
#print(i)

c = input("Give a character: ")
L = ["abc", "def", "xyz", "bey"]
x = 0
for i in L:
	if c in i:
		print(c, "found!")
		x=1

if x==0:
	print("Not in L")