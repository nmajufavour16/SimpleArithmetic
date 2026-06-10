# Collect user input
A = input("Enter the first number: ")
B = input("Enter the second number: ")

# Write a code to do the following: the code takes in two numbers A and B.
# It the subtracts B from A if A is greater than B with the message"A-B='A-B' 
# " where 'A-B' is the difference of A and B. If B is greater than A., 
# it then subtracts A from B and gives the message"B-A='B-A'
# " where 'B-A' the the difference between B and A. 
# However if A and B are same, the program gives a message "A and B are the same". 

if A > B:
    print(f"{A} - {B} = {int(A) - int(B)}")
elif B > A:
    print(f"{B} - {A} = {int(B) - int(A)}")
else:
    print("A and B are the same")