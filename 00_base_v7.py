# imports
import pandas

# functions go here


# makes sure users answer is not empty
def not_empty(question):
    while True:

        empty_response = input(question)

        if empty_response == "":
            print("Please enter a valid response")
        else:
            return empty_response


# makes sure users only enters integers
def numbers_only(question):

    while True:

        try:
            num_response = int(input(question))
            assert num_response > 0
            return num_response

        except ValueError:
            print("Invalid answer, please enter an integer")

        except AssertionError:
            print("Number MUST be positive")


# makes sure users only enters integers
def allow_decimal(question):

    while True:

        try:
            num_response = float(input(question))
            assert num_response >= 0
            return num_response

        except ValueError:
            print("Invalid answer, please enter a number")

        except AssertionError:
            print("Number MUST be positive")


# rounds numbers to two decimal values
def currency(x):
    return "${:.2f}".format(x)


# setting up panda
# VARIABLE TABLE
# List to hold details
all_variable_names = []
all_quantities = []
all_prices = []

# Dictionary used to create data frame ie: column_name:list
variables_dict = {
    "Name": all_variable_names,
    "Quantity": all_quantities,
    "Price": all_prices
}

# FIXED COST TABLE
# Lists to hold details for fixed costs
all_fixed_names = []
all_costs_fixed = []

# Fixed Cost Dict
fixed_dict = {
    "Name": all_fixed_names,
    "Cost": all_costs_fixed
}
# MAIN ROUTINE STARTS HERE
print()

product_name = not_empty("What is your product name? ")

# asks user how many products they will be selling
product_amount = numbers_only("How many products are you going to sell? ")


# loop that asks user if they are donating a dollar amount or percentage
while True:

    dol_or_perc = not_empty("Would you like to raise a percentage or dollar amount? ")
    dol_or_perc = dol_or_perc.lower()

    if dol_or_perc[0] == "d" or dol_or_perc[0] == "$":
        calc_profit_number = allow_decimal("How much are you looking to profit ($) ")
        # choice stores whether the user is paying a dollar amount or percentage
        choice = "dollar"
        break

    elif dol_or_perc[0] == "p" or dol_or_perc[0] == "%":
        calc_profit_number = allow_decimal("What percent are you looking to profit ")
        # choice stores whether the user is paying a dollar amount or percentage
        choice = "percentage"
        break
        pass

    else:
        print("That is not a valid answer, please try (Dollar / Percentage)")
        calc_profit_number = ""
        choice = ""
        continue

print()
print("Enter your variable name and costs (set name as 'xxx' to cancel)")

variable_name = ""
while True:

    variable_name = not_empty("Enter the variable name: ")
    if variable_name.lower() == "xxx":
        break

    variable_quantity = numbers_only("How many are you buying? ")
    variable_price = allow_decimal("How much do these cost (individually) $")
    print()

    # adds data to the table
    all_variable_names.append(variable_name)
    all_quantities.append(variable_quantity)
    all_prices.append(variable_price)

print()
print("Enter your FIXED name and costs (set name as 'xxx' to cancel)")
fixed_name = ""
while True:

    fixed_name = not_empty("Enter the variable name: ")
    if fixed_name.lower() == "xxx":
        break

    fixed_cost = allow_decimal("How much do these cost (individually) $")
    print()

    # adds data to the table
    all_fixed_names.append(fixed_name)
    all_costs_fixed.append(fixed_cost)

# sets the frame
# VARIABLE COSTS FRAME
variables_frame = pandas.DataFrame(variables_dict)
variables_frame = variables_frame.set_index('Name')

# FIXED COSTS FRAME
fixed_frame = pandas.DataFrame(fixed_dict)
fixed_frame = fixed_frame.set_index('Name')

# calculates the total cost per variable
# VARIABLES
variables_frame['Expense'] = variables_frame['Quantity'] * variables_frame['Price']

# sums up all the expenses into a single cost
# FOR VARIABLE TABLE
total_expenses = variables_frame['Expense'].sum()

# FOR FIXED TABLE
total_expenses_fixed = fixed_frame['Cost'].sum()

# VARIABLE SORTS TABLE BY COST HIGH TO LOW
variables_frame.sort_values(by=['Expense'], inplace=True, ascending=False)

# FIXED SORTS TABLE BY COST HIGH TO LOW
fixed_frame.sort_values(by=['Cost'], inplace=True, ascending=False)

# VARIABLE Currency Formatting (uses currency function)
add_dollars = ['Price', 'Expense']
for var_item in add_dollars:
    variables_frame[var_item] = variables_frame[var_item].apply(currency)

# FIXED Currency Formatting (uses currency function)
add_dollars = ['Cost']
for var_item in add_dollars:
    fixed_frame[var_item] = fixed_frame[var_item].apply(currency)

# setting variables for printing
print_product_name = "\n ***** {} *****".format(product_name)
# VARIABLE PRINTS
# change frame to a string, so I can import it to a file
variables_frame_string = pandas.DataFrame.to_string(variables_frame)
variable_frame_heading = "\n ---- VARIABLE COSTS TABLE ----"
variable_costs_heading = "\n----- Variable Costs -----"
total_variable_costs = "Total Expenses: ${:.2f}".format(total_expenses)


# FIXED PRINTS
# change frame to a string, so I can import it to a file
fixed_frame_string = pandas.DataFrame.to_string(fixed_frame)
fixed_frame_heading = "\n **** FIXED COSTS TABLE ****"
fixed_costs_heading = "\n ***** FIXED COSTS *****"
total_fixed_costs = "Total Cost: ${:.2f}".format(total_expenses_fixed)

# Final Calculations (Variables + Fixed)
overall_cost = total_expenses + total_expenses_fixed

# Gets users choice of dollar or percentage from the beginning code and does calculations
wanted_profit = ""
if choice == "dollar":
    wanted_profit = calc_profit_number

elif choice == "percentage":
    wanted_profit = overall_cost * (calc_profit_number/100)

# Continuing other calculations
# Total money needed to be raised to reach the profit goal
sales_needed = overall_cost + wanted_profit

# Calculating the price
min_sale_price = sales_needed/product_amount

# PRINTS FOR THE CALCULATIONS
print_costs_heading = "\n ##### OVERALL COSTS (VARIABLE AND FIXED) #####"
print_overall_cost = "Costs: ${:.2f}".format(overall_cost)

print_profit_heading = "\n #### PROFITS ####"
print_profit = "Profit wanted: ${:.2f}".format(wanted_profit)
print_total_sales = "Sales needed to reach profit goal: ${:.2f}".format(sales_needed)
print_sales_price = "Minimum Sale Price: ${:.2f}".format(min_sale_price)

# list holding content to print and write to file
to_write_product = [print_product_name]

# MAKE VARIABLE LIST EMPTY IF USER DID NOT INPUT DATA
if len(all_variable_names):

    to_write_variable = [variable_frame_heading, variables_frame_string, variable_costs_heading, total_variable_costs]

else:
    to_write_variable = []

# MAKE FIXED LIST EMPTY IF USER DID NOT INPUT DATA
if len(all_fixed_names):

    to_write_fixed = [fixed_frame_heading, fixed_frame_string, fixed_costs_heading, total_fixed_costs]

else:
    to_write_fixed = []

# PRINTS FINAL CALCULATIONS
to_write_final = [print_costs_heading, print_overall_cost,
                  print_profit_heading, print_profit,
                  print_total_sales, print_sales_price]
# print output
for item in to_write_product:
    print(item)

for item in to_write_variable:
    print(item)

for item in to_write_fixed:
    print(item)

for item in to_write_final:
    print(item)

# write output to file
# create file to hold data (add .txt extension)
write_to = "{}.txt".format(product_name)
text_file = open(write_to, "w+")

for item in to_write_product:
    text_file.write(item)
    text_file.write("\n")

for item in to_write_variable:
    text_file.write(item)
    text_file.write("\n")

for item in to_write_fixed:
    text_file.write(item)
    text_file.write("\n")

for item in to_write_final:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()
