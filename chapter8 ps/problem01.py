
def greatest_number():
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter a number: "))
    n3 = int(input("Enter a number: "))

    if(n1 == n2 == n3):
        print("The numbers are equal")
        

    elif(n1 > n2 and n1 > n3):
        print("The greatest number is:",n1)
        

    elif(n2 > n1, n2 > n3):
        print("The greatest number is:",n2)
        
        
    elif(n3 > n1, n3 > n2):
        print("The greatest number is:",n3)
        
    

greatest_number()
greatest_number()
greatest_number()


# def greatest_number():
#     n1 = int(input("Enter a number: "))
#     n2 = int(input("Enter a number: "))
#     n3 = int(input("Enter a number: "))

#     if(n1 == n2 == n3):
#         return "equal"

#     elif(n1 > n2 and n1 > n3):
#         return n1

#     elif(n2 > n1, n2 > n3):
#         return n2
        
#     elif(n3 > n1, n3 > n2):
#         return n3
    
# print(greatest_number())
# print(greatest_number())
# print(greatest_number())