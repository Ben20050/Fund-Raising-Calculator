# functions go here


def not_empty(question):
    while True:

        response = input(question)

        if response == "":
            print("Please enter a valid response")
        else:
            return response


# main routine goes here
dol_per = not_empty("Are you going to donate a percentage or dollar amount")
print(dol_per)
