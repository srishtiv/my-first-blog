a=input("enter no: ")
b=input("enter no: ")
ch=input("enter choice: ")
switcher={
	1:a+b,
	2:a-b,
	3:a*b,
	4:a/b,
}
print(switcher.get(ch,"nothing"))