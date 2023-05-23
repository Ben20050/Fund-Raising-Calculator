# functions go here


# makes sure users answer is not empty
def not_empty(question):
    while True:

        empty_response = input(question)

        if empty_response == "":
            print("Please enter a valid response")
        else:
            return empty_response


# makes sure users only enter numbers
def numbers_only(question):

    while True:

        try:
            num_response = int(input(question))
            return num_response

        except ValueError:
            print("Invalid answer, please enter an integer")


# rounds numbers to two decimal values
def currency(x):
    return "${:.2f}".format(x)


# setting up panda
# List to hold details
item_names = []
all_quantities = []
all_prices = []

# Dictionary used to create data frame ie: column_name:list
mini_movie_dict = {
    "Item": item_names,
    "Quantity": all_quantities,
    "Surcharge": all_prices
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
        calc_profit_number = numbers_only("How much are you looking to profit ($) ")
        # choice stores whether the user is paying a dollar amount or percentage
        choice = "dollar"
        break

    elif dol_or_perc[0] == "p" or dol_or_perc[0] == "%":
        calc_profit_number = numbers_only("What percent are you looking to profit ")
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
    
    item_names.append(variable_name)

print(item_names)
