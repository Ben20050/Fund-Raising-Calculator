def numbers_only(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Invalid answer, please enter an integer")


# main routine goes here
age = numbers_only("Please enter your age: ")
print(age)
