
##########################################################################################
## Get user input for annual_salary, portion_saved, total_cost, semi_annual_raise below ##
##########################################################################################

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the portion of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

down_payment_percentage = 0.15
current_savings = 0
r = 0.04
months = 0
down_payment = total_cost * down_payment_percentage
monthly_salary_saving = (annual_salary * portion_saved) / 12 # 12 months in a year!

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

# Keep calculating current_savings with salary increase to reach the down_payment amount
while current_savings < down_payment:
    current_savings += monthly_salary_saving + current_savings* r/12
    months += 1
    if months % 6 == 0:
        monthly_salary_saving += monthly_salary_saving * semi_annual_raise 
        
print("Number of months: " + str(months))
