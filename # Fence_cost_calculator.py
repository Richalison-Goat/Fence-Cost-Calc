# Auther: Felipe
# Date 24/05/2024
# version 1.0

# Code that tests that a valid number is enterd (V1)
#while not done: # While loop that runs untill a valid number is entered
#    print("please enter your value: ") # Ask user for a number 
#    try: # Try for a valid input
 #       num = float (input()) # Stroing user inut to number variable 
 #       done = True # If user the user enters a valid number, the while loop will break
 #   except ValueError: # If the user enters a string, restart the loop
 #       print ("That is not a valid number.") # This is my error message to the user 
 #       continue 

# print ("The number you entered is",num) # Old formatting 
# print (f"The number you entered is {num}") # New way

# Vesion 2, Creats a function to call every time I ask a user for a number
def test_float_num(question):
    done = False
    error = "That is not a valid number."
    while not done: 
        print(question) # the question part is a place holder
        try:
            num = float(input())
            if num >0:
                done = True
            else:
              print (error)
        except ValueError:
            print (error)
    return(num) # Gives me back the value of num do that I can use it outside the function


# Main routine
print("Welcome to my conversion calculator.")
width = test_float_num("Please enter your width (in meters):")
print(f'You entered {width}m') 

length = test_float_num("\nPlease enter your length(in meters):")
print(f"You entered {length}m")

cost = test_float_num("\nPlease enter cost per meter") 
print(f'The cost per meter value you entered is ${cost}')

perimeter = 2 * (width + length) 
fencecost = perimeter *cost

print(f"The perimeter of your fence is {perimeter}m")
print(f"The cost to build your fence will be ${fencecost}")

keep_going = input("Press enter to complete another calculation, any other key to end the program")

print("Thank you for using my conversion calculator hope it helped :)")