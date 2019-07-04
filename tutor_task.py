# Printing the program title
print("To collect pairs of integers whose product is even and sum is odd from given input list")

# Declaring a list and a flag to read user input
user_input = []
input_flag = 'Y'

# Recursively reading input until user wishes to terminate
while(input_flag.upper() == 'Y'):
    
	# Using the int() function to throw errors intuitively without any additional code from the new programmer
    value = int(input("Please enter an integer: "))
    
	# Appending the new input to list
    user_input.append(value)
    
	# Prompting for new inputs from user
    input_flag = input("Would you like to enter another input (Y/N)? ")

# Capturing the length of the final user input	
input_count = len(user_input)

# Displaying stats about the user input and the input list
print("\nThere are",input_count,"numbers in the entered input.")
print("The entered input is:",user_input)

# Declaring place holder lists for product, sum and both constraints
product_list = []
sum_list = []
both_list = []

# Checking the product and sum for every pair of numbers in the list
for i in range(input_count):
    
	# Extracting the first number
    num1 = user_input[i]
    
	# Iterating through the list from the second to last number
    for j in range(i+1,input_count):
        
		# Extracting the second number
        num2 = user_input[j]
        
		# Calculating the product and sum (total as sum is a reserved word) 
        product = num1*num2
        total = num1+num2
        
        # Check if the pair's product is even and sum is odd
        if((product%2 == 0) and (total%2 != 0)):
            
			# Appending corresponding pairs to the respective list
            both_pair = "(" + str(num1) + "," + str(num2) + ")"
            both_list.append(both_pair)
        
		# Check if the pair's product is even
        elif(product%2 == 0):
            
			# Appending corresponding pairs to the respective list
            product_pair = "(" + str(num1) + "," + str(num2) + ")"
            product_list.append(product_pair)
        
		# Check if the pair's total is even		
        elif(total%2 != 0):
            
			# Appending corresponding pairs to the respective list
            sum_pair = "(" + str(num1) + "," + str(num2) + ")"
            sum_list.append(sum_pair)
		
# Collecting number of pairs in each category		
both_len = len(both_list)
product_len = len(product_list)
sum_len = len(sum_list)

# Displaying the summary if there are pairs with both conditions satisfied
if(both_len > 0):
    print("The are ",both_len," pairs of numbers in the user input whose product is even and sum is odd.")
    print("The pairs are",both_list)

# Displaying the summary if there are pairs with individual conditions satisfied but not both    
elif(product_len > 0 and sum_len > 0):
    
    print("There are no pairs with an even product and odd sum.")
    print("But there are ",product_len," pairs with an even product.")
    print("And there are ",sum_len," pairs with an odd sum.")
    print("The product pairs are",product_list)
    print("The sum pairs are",sum_list)

# Displayin the summary if there are pairs only with product even    
elif(product_len > 0):
    
    print("There are no pairs with an even product and odd sum or with just an odd sum.")
    print("But there are ",product_len," pairs with an even product.")
    print("The pairs are",product_list)

# Displayin the summary if there are pairs only with total odd    
elif(sum_len > 0):
    
    print("There are no pairs with an even product and odd sum or with just an even product.")
    print("But there are ",sum_len," pairs with an odd sum.")
    print("The pairs are",sum_list)