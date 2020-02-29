

high = 0
high2 = 0
maxChar = 0
maxChar2 = 0


for i in range(97,123,1):
	counter = 0
	for k in readString:
		k_int = ord(k)
		if i == k_int:
			counter = counter + 1	
	if counter > high:
		high = counter
		maxChar  = i	
		
print(maxChar) #e
#101
shift = 101 - maxChar

for i in range(97, 123, 1):
	if (i != maxChar):
		counter = 0
		for k in readString:
			k_int = ord(k)
			if i == k_int:
				counter = counter + 1	
		if counter > high2:
			high2 = counter
			maxChar2  = i
		
			
print(maxChar2)

actualMaxChar2 = maxChar2 + shift
if actualMaxChar2 > 122:
	actualMaxChar2 = actualMaxChar - 26
	
	

#is actualMaxChar2 A or T? if not, that's a problem
# some check





dif1 = maxChar - maxChar2

print(high)
if high >= 108:
	if dif1 != 11 and dif1 != 4:
		print("Quitting...")
		exit() 
	
	elif high < 101:
	 	if dif1 != -22 and dif1 != -15:
	 		print("Quitting...")
	 		exit()

	elif high >= 101 and high < 108:
		if dif1 != 4 and dif1 != 15:
			print("Quitting...")
			exit()
	else:  
		outputFile = open("CaesarwikiDone.txt", "w")
		shift = 101 - high
		outputStr = ""
		print("got here")
		for i in readString:
	 	 	if ord(i) != 90:
	 	 		num = ord(i) + shift
	 	 		outputStr += chr(num)
		outputFile.write(outputStr)
		outputFile.close()




	
	
