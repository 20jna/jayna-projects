# inputs x,y from user, outputs x*y
# author: Jay Na

def main():
	fullName=input("What is your name?")
	
	# input x,y as integers
	x=input("x: ")
	y=input("y: ")
	sum=0

	x=int(x)
	y=int(y)
	sum=int(sum)
	
	#calculate sum=x*y
	for i in range(x):
		sum=sum+y
	print("x*y= ",sum)
	print("Thanks for playing,", fullName)
	
main()