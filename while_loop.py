#1.print numbers from 7 - 19
print ("Numbers from 7 - 19")
i=7
while (i<=19):
    print (1)
    i += 1
    print ("")
    
    
    
    
    
#2.print even numbers between 12 and 20
print ("Even Numbers Between 12 and 29")
a=13
while a<20:
    if a%2!=0:
        a += 1
    else:
        print(a)
        a += 1
print ("")





#3.function that takes two numbers and inputs even numbers between them
print ("Determine Even Numbers in the Inputs")
def even():
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    
    while a==0:
        return print ( 
    
    while a%2==0 and b%2!=0:
        return print ("'",a,"' ""is an even number"" '",b,"' ""is not")
    
    while a%2!=0 and b%2==0:
        return print ("'",b,"' ""is an even number"" '",a,"' ""is not")
    
    while a%2==0 and b%2==0:
        return print ("'",a,"' ""and"" '",b,"' ""are even numbers")
    
print (even())
    