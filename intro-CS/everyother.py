s = input("enter some string: ")
#print(s[::2])
for i in range(0,len(s),2):
	print(s[i])
	
news = s[:: -1]
if news == s:
	print("palindrome")