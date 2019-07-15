## 6.0001 Pset 1: Part c
## Name: Shirin Amouei
## Time Spent: 3:00
## Collaborators: None

##############################################
## Get user input for initial_deposit below ##
##############################################

initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

total_cost = 750000
down_payment = total_cost * 0.25
number_of_months = 36
current_savings = 0
epsilon = 100 # $100 margin
steps = 0
low = 0 # Lowest interest rate (r) is 0%
high = 100 # Lowest interest rate (r) is 100%

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

# Check if there is need to save!
# r is interest rate
if initial_deposit >= down_payment + epsilon: 
    r = 0.0
    print("Best savings rate: " , r)
    print("Steps in bisection search: " , steps)

# Check if initial_deposit will ever be enough even with 100% return rate  
# 100% interest rate multiplies initial_deposit by 2**n in n years
elif (initial_deposit * (2 ** (number_of_months / 12))) < down_payment:   
    r = None
    print("Best savings rate: " , r)
    print("Steps in bisection search: " , steps)

# Bisection search
else:
    r = ((low + high) / 2.0)     
    current_savings = initial_deposit * ((1 + r/1200) ** number_of_months)        
    
    # Keep bisecting the range till epsilon range is reached
    while abs(current_savings - down_payment) >= epsilon:
        steps += 1
        if current_savings <= down_payment - epsilon:
            low = r       
        else:
            high = r
        r = (low + high) / 2.0  
        current_savings = initial_deposit * ((1 + r/1200) ** number_of_months)
        
    # Return final interest rate
    r = r / 100        
    print("Best savings rate: " , r)
    print("Steps in bisection search: " , steps)
    
