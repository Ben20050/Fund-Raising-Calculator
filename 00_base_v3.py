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
            return num_response

        except ValueError:
            print("Invalid answer, please enter an integer")


# makes sure users only enters integers
def allow_decimal(question):

    while True:

        try:
            num_response = float(input(question))
            return num_response

        except ValueError:
            print("Invalid answer, please enter a number")


# rounds numbers to two decimal values
def currency(x):
    return "${:.2f}".format(x)


# setting up panda
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

# main routine starts here
print()

product_name = not_empty("What is your product name? ")

# loop ensuring the users enters a whole number that isn't 0 or negative
while True:

    product_amount = numbers_only("How many products are you going to sell? ")

    if product_amount >= 1:
        break

    else:
        print("Please enter a whole number higher than 0")


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

# sets the frame
variables_frame = pandas.DataFrame(variables_dict)
variables_frame = variables_frame.set_index('Name')

# calculates the total cost per variable
variables_frame['Expense'] = variables_frame['Quantity'] * variables_frame['Price']

# sums up all the expenses into a single cost
total_expenses = variables_frame['Expense'].sum()

# Currency Formatting (uses currency function)
add_dollars = ['Price', 'Expense']
for var_item in add_dollars:
    variables_frame[var_item] = variables_frame[var_item].apply(currency)

# change frame to a string, so we can import it to a file
variables_frame_string = pandas.DataFrame.to_string(variables_frame)

# setting variables for printing
variable_frame_heading = "\n ---- VARIABLE COSTS TABLE ----"
variable_costs_heading = "\n----- Variable Costs -----"
total_variable_costs = "Total Variable Costs: ${:.2f}".format(total_expenses)


# list holding content to print and write to file
to_write = [variable_frame_heading, variables_frame_string, variable_costs_heading, total_variable_costs]

# print output
for item in to_write:
    print(item)
