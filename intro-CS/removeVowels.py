#take out vowels in word

s = input("enter some string: ")

news = " "
for c in s:
	if c in "aeiou":
		pass
	else:
		#print(c, end="")
		news += c
		#another way to subtract the vowels

print()


#can do it this way as well
news = " "
for c in s:
	if c not in "aeiou":
		news += c
		
print(news)