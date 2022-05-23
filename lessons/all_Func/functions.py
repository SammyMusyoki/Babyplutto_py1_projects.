def greet_user(username):
    print('Hello, ' + username + '!')


greet_user('sammy')
greet_user('purity')


# passing a list as an argument


def greet_users(names):
    for name in names:
        msg = "Hello, " + name + "!"
        print(msg)


usernames = ['Hannah', 'ty', 'margot']
greet_users(usernames)

# Allowing a function to modify a list


def print_models(unprinted, printed):
    while unprinted:
        current_model = unprinted.pop()
        print("Printing " + current_model)
        printed.append(current_model)

# Store some unprinted designs, and print each of them


unprinted = ['phone case', 'pendant', 'ring']
printed = []
print_models(unprinted, printed)

print("\nUnprinted:", unprinted)
print("Printed:", printed, end='\n')

# Preventing a function from modifying a list


def print_models(unprinted, printed):
    while unprinted:
        current_model = unprinted.pop()
        print("Printing " + current_model)
        printed.append(current_model)


original = ['Bugatti', 'Ferrari', 'Range Rover']
printed = []

print_models(original[:], printed)
print("\nOriginal:", original)
print("Printed:", printed)

