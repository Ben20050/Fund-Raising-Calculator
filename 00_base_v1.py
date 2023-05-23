# functions go here


def not_empty(question):
    while True:

        empty_response = input(question)

        if empty_response == "":
            print("Please enter a valid response")
        else:
            return empty_response


def numbers_only(question):

    while True:

        try:
            num_response = int(input(question))
            return num_response

        except ValueError:
            print("Invalid answer, please enter an integer")


# main routine starts here
# loop that asks user if they are donating a dollar amount or percentage
while True:

    dol_or_perc = not_empty("Would you like to donate a Dollar amount or percentage of your profits to our charity? ")
    dol_or_perc = dol_or_perc.lower()

    if dol_or_perc[0] == "d" or dol_or_perc[0] == "$":
        print("Thank you for raising a dollar amount!")
        contribution = numbers_only("How much are you willing to donate in dollars (Please enter a whole number)")
        # choice stores whether the using is paying a dollar amount or percentage ( 1 is dollar, 2 is percent)
        choice = "dollar"
        break

    elif dol_or_perc[0] == "p" or dol_or_perc[0] == "%":
        print("Thank you for donating a percentage of your profits towards our charity!")
        contribution = numbers_only("What percent are you willing to donate (Please enter a whole value)")
        # choice stores whether the using is paying a dollar amount or percentage ( 1 is dollar, 2 is percent)
        choice = "percentage"
        break

    else:
        print("That is not a valid answer, please try (Dollar / Percentage)")
        contribution = ""
        choice = ""
        continue

print(contribution)
print(choice)
