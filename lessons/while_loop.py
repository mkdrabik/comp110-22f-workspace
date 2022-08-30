""" Example of a while loop """

counter: int = 0
maximum: int= int(input("Enter a number "))
while counter != maximum:
    counter_square: int= counter**2
    print("The sqaureed numbers " + str(counter_square))
    counter = counter + 1 

print("done")
